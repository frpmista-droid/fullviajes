import subprocess, json, os
def run(c): subprocess.run(c,check=True)
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))
GRADE="eq=contrast=1.06:saturation=1.07:gamma=0.98,colorbalance=rs=0.02:bs=-0.02:rm=0.01:bm=-0.01,vignette=PI/5,noise=alls=4:allf=t+u"
SEG=[('A','clean_a.mp4',0.0,4.0),('B','clean_b.mp4',0.0,4.9),('C1','clean_c.mp4',0.3,2.2),('C2','clean_d.mp4',0.6,3.4),
     ('D1','V_hola2025.mp4',0.8,1.8),('D2','V_hola2025.mp4',6.0,2.0),('D3','V_hola2025.mp4',11.6,1.4),('D4','V_hola2025.mp4',24.0,1.8),
     ('E','mariano.mp4',0.0,7.2)]
os.makedirs('parts',exist_ok=True); lst=[]; t=0; starts={}
for name,src,ss,d in SEG:
    if d is None: d=dur(src)
    out=f'parts/{name}.mp4'
    sharpen=',unsharp=5:5:0.6' if 'hola' in src or 'clean' in src else ''
    run(['ffmpeg','-v','error','-y','-ss',str(ss),'-i',src,'-t',str(d),'-an','-vf',
         f"scale=1080:1920:flags=lanczos{sharpen},fps=30,setsar=1,{GRADE},format=yuv420p",
         '-c:v','libx264','-crf','14','-preset','fast',out])
    starts[name]=t; t+=d; lst.append(out)
END=3.6
run(['ffmpeg','-v','error','-y','-loop','1','-t',str(END),'-i','endcard.png','-vf',
     f"fps=30,scale=1080:1920,zoompan=z='min(1+0.0007*on,1.04)':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d=1:s=1080x1920:fps=30,fade=t=in:st=0:d=0.35,format=yuv420p",
     '-c:v','libx264','-crf','14','-preset','fast','parts/F.mp4'])
starts['F']=t; TOT=t+END; lst.append('parts/F.mp4')
open('parts/list.txt','w').write(''.join(f"file '{os.path.basename(x)}'\n" for x in lst))
run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','parts/list.txt','-c','copy','parts/base.mp4'])
Z=starts['B']+4.75
E0=starts['E']; F0=starts['F']; D40=starts['D4']
print(json.dumps({k:round(v,2) for k,v in starts.items()}),'zero',Z,'total',TOT)
# overlays
ov=[('txt/loc.png',starts['B']+0.05,starts['D1']),('txt/a.png',0.6,3.8),('txt/z.png',Z+0.12,Z+2.6),('txt/sub.png',E0+0.35,F0-0.15)]
inp=['-i','parts/base.mp4']
for f,_,_ in ov: inp+=['-loop','1','-i',f]
# audio inputs
A0=len(ov)+1
inp+=['-i','mariano.mp4','-i','amb.mp3','-i','boom.mp3','-i','clink.mp3','-i','music2.mp3','-i','v1_s3.mp4']
fc=[]; cur='0:v'
for k,(f,a,b) in enumerate(ov):
    fc.append(f"[{k+1}:v]format=rgba,fade=t=in:st={a}:d=0.25:alpha=1,fade=t=out:st={b-0.3}:d=0.3:alpha=1[t{k}]")
    fc.append(f"[{cur}][t{k}]overlay=0:0:shortest=1:enable='between(t,{a},{b})'[o{k}]"); cur=f'o{k}'
fc.append(f"[{cur}]fade=t=in:st=0:d=0.5,trim=0:{TOT},setpts=PTS-STARTPTS[vout]")
def place(label,src,delay,vol,extra=''):
    fc.append(f"[{src}]aresample=48000,aformat=channel_layouts=stereo{extra},volume={vol},adelay={int(delay*1000)}|{int(delay*1000)}[{label}]")
mi,ai,bi,ci,mu,s3=A0,A0+1,A0+2,A0+3,A0+4,A0+5
# ambience loop 0..Z and low under D/E
fc.append(f"[{ai}:a]aresample=48000,aformat=channel_layouts=stereo,aloop=loop=3:size=480000,atrim=0:{TOT},volume='if(lt(t,{Z}),0.85,0.35)':eval=frame[amb]")
# countdown shouts (from v1 crowd), aligned to wheel numbers
shouts=[(0.45,1.45),(1.70,2.70),(2.90,3.90),(4.00,5.00),(5.10,6.10)]
wheel=[0.0,0.7,1.7,2.7,3.7]
fc.append(f"[{s3}:a]aresample=48000,aformat=channel_layouts=stereo,asplit=5"+''.join(f'[sh{i}]' for i in range(5)))
for i,((a,b),w) in enumerate(zip(shouts,wheel)):
    d=starts['B']+w-0.05
    fc.append(f"[sh{i}]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.03,afade=t=out:st={b-a-0.15}:d=0.15,aecho=0.8:0.6:60|110:0.25|0.15,volume={0.9+0.08*i},adelay={int(d*1000)}|{int(d*1000)}[c{i}]")
place('boom',f'{bi}:a',Z-0.08,1.0,f",atrim=0:12,volume='if(lt(t,{E0-Z+0.08}),1,0.30)':eval=frame,afade=t=out:st=11:d=1")
place('clk',f'{ci}:a',D40+0.4,0.8)
fc.append(f"[{mu}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=1.25,asetpts=PTS-STARTPTS,atrim=0:{TOT},volume='if(lt(t,{Z-0.2}),0.55+0.35*t/{Z},if(lt(t,{Z}),0.15,if(lt(t,{E0}),0.85,if(lt(t,{F0}),0.16,0.8))))':eval=frame,afade=t=out:st={TOT-1.4}:d=1.4[mus]")
fc.append(f"[{mi}:a]aresample=48000,aformat=channel_layouts=stereo,highpass=f=80,equalizer=f=3500:t=q:w=1:g=2.5,acompressor=threshold=-22dB:ratio=3:attack=10:release=150,volume=2.4,adelay={int(E0*1000)}|{int(E0*1000)}[voz]")
fc.append("[amb][c0][c1][c2][c3][c4][boom][clk][mus][voz]amix=inputs=10:normalize=0,atrim=0:"+str(TOT)+",alimiter=limit=0.89,loudnorm=I=-14:TP=-1.0:LRA=11,aresample=48000[aout]")
run(['ffmpeg','-v','error','-y']+inp+['-filter_complex',';'.join(fc),'-map','[vout]','-map','[aout]','-r','30','-c:v','libx264','-preset','medium','-crf','20','-maxrate','14M','-bufsize','28M','-pix_fmt','yuv420p','-profile:v','high','-c:a','aac','-b:a','256k','-movflags','+faststart','final_v2.mp4'])
json.dump({'starts':starts,'zero':Z,'total':TOT},open('timeline_v2.json','w'))
