from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H=1080,1920
F='/usr/share/fonts/opentype/montserrat/Montserrat-%s.otf'
GOLD=(232,190,92); WHITE=(255,255,255)
def font(w,s): return ImageFont.truetype(F%w,s)
def block(lines, y, out, shadow=True):
    """lines: list of (text, weight, size, color)"""
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    cy=y
    pos=[]
    for t,w,s,c in lines:
        f=font(w,s); bb=d.textbbox((0,0),t,font=f); tw=bb[2]-bb[0]; th=bb[3]-bb[1]
        pos.append((t,f,(W-tw)//2-bb[0],cy-bb[1],c)); cy+=th+int(s*0.35)
    if shadow:
        sh=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(sh)
        for t,f,x,yy,c in pos: sd.text((x+3,yy+4),t,font=f,fill=(0,0,0,200))
        sh=sh.filter(ImageFilter.GaussianBlur(8)); im=Image.alpha_composite(sh,im); d=ImageDraw.Draw(im)
    for t,f,x,yy,c in pos: d.text((x,yy),t,font=f,fill=c+(255,))
    im.save(out)
block([("ESTE AÑO NUEVO","ExtraBold",84,WHITE),("SE VIVE EN BRASIL","Black",92,GOLD)],1380,'txt/t1.png')
block([("IMAGINATE RECIBIR","ExtraBold",76,WHITE),("EL 2027","Black",120,GOLD),("FRENTE AL MAR...","ExtraBold",76,WHITE)],1300,'txt/t2.png')
block([("¡FELIZ","Black",130,WHITE),("AÑO NUEVO!","Black",130,GOLD)],330,'txt/t4.png')
for n in ['5','4','3','2','1','0']:
    block([(n,"Black",520,GOLD if n!='0' else WHITE)],620,f'txt/n{n}.png')
block([("¡Vos qué estás esperando","Bold",58,WHITE),("para ir a pasar Año Nuevo así!","Bold",58,WHITE)],1560,'txt/sub5.png')
