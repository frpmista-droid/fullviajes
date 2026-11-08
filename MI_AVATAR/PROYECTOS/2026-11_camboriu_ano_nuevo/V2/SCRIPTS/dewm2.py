import cv2, numpy as np, subprocess, sys
src,dst=sys.argv[1],sys.argv[2]
cap=cv2.VideoCapture(src); fps=cap.get(5)
frames=[]
while True:
    ok,f=cap.read()
    if not ok: break
    frames.append(f)
H,W=frames[0].shape[:2]
M=np.zeros((H,W),np.uint8); cv2.rectangle(M,(212,852),(510,906),255,-1)
Md=cv2.dilate(M,np.ones((15,15),np.uint8))
orb=cv2.ORB_create(3000)
gray=[cv2.cvtColor(f,cv2.COLOR_BGR2GRAY) for f in frames]
feat=[orb.detectAndCompute(g,255-Md) for g in gray]
bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
def homog(i,j):
    k1,d1=feat[i]; k2,d2=feat[j]
    if d1 is None or d2 is None or len(k1)<30 or len(k2)<30: return None
    m=sorted(bf.match(d2,d1),key=lambda x:x.distance)[:400]
    if len(m)<30: return None
    p2=np.float32([k2[x.queryIdx].pt for x in m]); p1=np.float32([k1[x.trainIdx].pt for x in m])
    Hm,inl=cv2.findHomography(p2,p1,cv2.RANSAC,3.0)
    if Hm is None or inl.sum()<25: return None
    return Hm
out=[]
stats=[0,0]
offs=[o for k in range(3,46,2) for o in (k,-k)]
for i,f in enumerate(frames):
    need=(M>0).copy(); fill=f.copy().astype(np.float32); acc=np.zeros((H,W),bool)
    for o in offs:
        j=i+o
        if j<0 or j>=len(frames): continue
        Hm=homog(i,j)
        if Hm is None: continue
        wf=cv2.warpPerspective(frames[j],Hm,(W,H))
        wm=cv2.warpPerspective(Md,Hm,(W,H),borderValue=255)
        valid=need&(wm==0)&~acc
        if valid.sum()==0: continue
        fill[valid]=wf[valid]; acc|=valid
        if (need&~acc).sum()==0: break
    rest=need&~acc
    stats[0]+=acc.sum(); stats[1]+=rest.sum()
    res=fill.astype(np.uint8)
    if rest.any():
        res=cv2.inpaint(res,rest.astype(np.uint8)*255,5,cv2.INPAINT_TELEA)
    # feathered blend
    a=cv2.GaussianBlur(cv2.dilate(M,np.ones((7,7),np.uint8)).astype(np.float32)/255,(15,15),0)[...,None]
    o_=f*(1-a)+res*a
    out.append(np.clip(o_,0,255).astype(np.uint8))
print('filled temporal',stats[0],'telea',stats[1])
p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r',str(fps),'-i','-','-c:v','libx264','-crf','12','-preset','medium','-pix_fmt','yuv420p',dst],stdin=subprocess.PIPE)
for o_ in out: p.stdin.write(o_.tobytes())
p.stdin.close(); p.wait()
