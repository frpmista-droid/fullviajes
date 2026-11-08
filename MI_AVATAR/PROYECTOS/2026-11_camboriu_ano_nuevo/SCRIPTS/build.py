import subprocess, json, sys
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))
V=['s1.mp4','s2.mp4','s3.mp4','s4.mp4','s5.mp4']
D=[dur(v) for v in V]; END=6.0
starts=[0]; 
for d in D: starts.append(starts[-1]+d)
T5=starts[4]; TE=starts[5]; TOT=TE+END
Z=starts[2]+6.45          # cero
nums=[(n,starts[2]+t) for n,t in zip('543210',[0.55,1.8,3.0,4.1,5.2,6.45])]
print('durs',D,'zero',Z,'total',TOT)
inp=[]; 
for v in V: inp+=['-i',v]
inp+=['-loop','1','-t',str(END),'-i','endcard.png']
txts=[('txt/t1.png',0.5,4.6),('txt/t2.png',starts[1]+0.5,starts[2]-0.4),('txt/t4.png',Z+0.25,starts[3]+1.6),('txt/sub5.png',T5+0.6,TE-0.2)]
for n,t in nums: txts.append((f'txt/n{n}.png',t-0.05,t+0.85 if n!='0' else t+0.6))
for f,_,_ in txts: inp+=['-loop','1','-i',f]
inp+=['-i','music.mp3']
fc=[]
# video: scale each to 1080x1920 30fps, short crossfades via concat with fade-through-black minimal
for i in range(5):
    fc.append(f"[{i}:v]scale=1080:1920:flags=lanczos,fps=30,setsar=1,format=yuv420p,setpts=PTS-STARTPTS[v{i}]")
fc.append(f"[5:v]fps=30,scale=1080:1920,setsar=1,format=yuv420p,zoompan=z='min(1+0.0006*on,1.035)':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d=1:s=1080x1920:fps=30,fade=t=in:st=0:d=0.4:color=white,fade=t=out:st={END-0.6}:d=0.6[v5]")
# small fades at cuts
fc.append(f"[v0]fade=t=in:st=0:d=0.5[a0v]")
fc.append(f"[v3]fade=t=in:st=0:d=0.15:color=white[a3v]")
fc.append(f"[v4]fade=t=in:st=0:d=0.35[a4v]")
fc.append("[a0v][v1][v2][a3v][a4v][v5]concat=n=6:v=1:a=0[base]")
cur='base'
for k,(f,a,b) in enumerate(txts):
    idx=6+k
    fade_in=0.12 if 'n' in f.split('/')[-1][:1] else 0.35
    fc.append(f"[{idx}:v]format=rgba,fade=t=in:st={a}:d={fade_in}:alpha=1,fade=t=out:st={b-0.25}:d=0.25:alpha=1[t{k}]")
    fc.append(f"[{cur}][t{k}]overlay=0:0:shortest=1:enable='between(t,{a},{b})'[o{k}]"); cur=f"o{k}"
fc.append(f"[{cur}]trim=0:{TOT},setpts=PTS-STARTPTS[vout]")
# audio from clips
gains=[0.55,0.6,1.0,0.95,1.0]
for i in range(5):
    fc.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,volume={gains[i]},apad=whole_dur={D[i]},atrim=0:{D[i]},asetpts=PTS-STARTPTS[ca{i}]")
fc.append(f"anullsrc=r=48000:cl=stereo,atrim=0:{END}[ca5]")
fc.append("[ca0][ca1][ca2][ca3][ca4][ca5]concat=n=6:v=0:a=1[amb]")
# music: loop beat-aligned segment, dynamic volume
mi=6+len(txts)
seg=f"atrim=0.58:22.66,asetpts=PTS-STARTPTS"
fc.append(f"[{mi}:a]aresample=48000,aformat=channel_layouts=stereo,asplit=3[m1][m2][m3]")
fc.append(f"[m1]{seg}[ma];[m2]{seg}[mb];[m3]{seg}[mc]")
fc.append("[ma][mb][mc]concat=n=3:v=0:a=1[mus0]")
vol=("volume='if(lt(t,{s2}),0.30+0.25*t/{s2},"
     "if(lt(t,{z0}),0.30,"
     "if(lt(t,{z}),0,"
     "if(lt(t,{t5}),0.95,"
     "if(lt(t,{te}),0.16,0.8)))))':eval=frame").format(s2=starts[2],z0=Z-0.45,z=Z,t5=T5,te=TE)
fc.append(f"[mus0]atrim=0:{TOT},asetpts=PTS-STARTPTS,lowpass=f=12000,{vol},afade=t=in:st=0:d=1.2,afade=t=out:st={TOT-1.5}:d=1.5[mus]")
fc.append(f"[amb][mus]amix=inputs=2:normalize=0,atrim=0:{TOT},loudnorm=I=-14:TP=-1.0:LRA=11,aresample=48000[aout]")
cmd=['ffmpeg','-v','error','-y']+inp+['-filter_complex',';'.join(fc),'-map','[vout]','-map','[aout]','-r','30','-c:v','libx264','-preset','medium','-crf','17','-pix_fmt','yuv420p','-profile:v','high','-c:a','aac','-b:a','256k','-movflags','+faststart','final.mp4']
subprocess.run(cmd,check=True)
json.dump({'starts':starts,'zero':Z,'total':TOT},open('timeline.json','w'))
