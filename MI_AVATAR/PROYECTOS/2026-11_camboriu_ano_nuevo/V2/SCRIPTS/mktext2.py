from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H=1080,1920
F='/usr/share/fonts/opentype/montserrat/Montserrat-%s.otf'
GOLD=(232,190,92); WHITE=(255,255,255)
def block(lines, y, out):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); cy=y; pos=[]
    for t,w,s,c in lines:
        f=ImageFont.truetype(F%w,s); bb=d.textbbox((0,0),t,font=f)
        pos.append((t,f,(W-(bb[2]-bb[0]))//2-bb[0],cy-bb[1],c)); cy+=bb[3]-bb[1]+int(s*0.32)
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(sh)
    for t,f,x,yy,c in pos: sd.text((x+2,yy+3),t,font=f,fill=(0,0,0,210))
    sh=sh.filter(ImageFilter.GaussianBlur(7)); im=Image.alpha_composite(sh,im); d=ImageDraw.Draw(im)
    for t,f,x,yy,c in pos: d.text((x,yy),t,font=f,fill=c+(255,))
    im.save(out)
block([("ESTE AÑO NUEVO","ExtraBold",70,WHITE),("SE VIVE EN CAMBORIÚ","Black",78,GOLD)],1430,'txt/a.png')
block([("¡FELIZ","Black",150,WHITE),("2027!","Black",190,GOLD)],300,'txt/z.png')
block([("¡Vos qué estás esperando para venir","Bold",50,WHITE),("a pasar Año Nuevo así con Full Viajes!","Bold",50,WHITE)],1590,'txt/sub.png')
