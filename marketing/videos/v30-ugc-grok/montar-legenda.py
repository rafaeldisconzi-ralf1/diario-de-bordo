from PIL import Image, ImageDraw, ImageFont
W,H=1080,1920
F='barlow-condensed-latin-800-normal.ttf'
YEL=(242,183,5); WH=(244,243,238); GR=(95,211,154)
caps=[("CAMINHONEIRO, PRESTA ATENÇÃO:",{"CAMINHONEIRO,":YEL},0.0,1.8),
("ESSE APP FAZ A CONTA DO FRETE PRA VOCÊ.",{"CONTA":YEL,"DO":YEL,"FRETE":YEL},1.8,4.4),
("ABASTECEU?",{"ABASTECEU?":YEL},4.4,5.45),
("É SÓ FALAR QUE ELE ANOTA.",{"FALAR":YEL},5.45,7.1),
("E NO FIM MOSTRA QUANTO SOBROU.",{"SOBROU.":GR},7.1,8.9)]
def draw(text,hl,path,size=100,y0=1600):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    f=ImageFont.truetype(F,size)
    words=text.split(); lines=[]; cur=[]
    for w in words:
        t=' '.join(cur+[w])
        if d.textlength(t,font=f)>980 and cur: lines.append(cur); cur=[w]
        else: cur.append(w)
    lines.append(cur)
    y=y0
    for ln in lines:
        tw=d.textlength(' '.join(ln),font=f); x=(W-tw)/2
        for w in ln:
            col=hl.get(w,WH)
            for dx in range(-6,7,2):
                for dy in range(-6,7,2):
                    d.text((x+dx,y+dy),w,font=f,fill=(0,0,0,255))
            d.text((x,y),w,font=f,fill=col+(255,))
            x+=d.textlength(w+' ',font=f)
        y+=size*1.0
    im.save(path)
for i,(t,h,a,b) in enumerate(caps): draw(t,h,f'cap{i}.png')
# phones
S='/home/claude/diario-de-bordo/marketing/videos/v29-pack-27-11/telas/'
def phone(n,out):
    s=Image.open(S+n+'.png').convert('RGB').resize((340,736))
    m=Image.new('RGBA',(360,756),(0,0,0,0)); d=ImageDraw.Draw(m)
    d.rounded_rectangle((0,0,359,755),radius=34,fill=(20,20,20,255),outline=YEL+(255,),width=4)
    mask=Image.new('L',(340,736),0); ImageDraw.Draw(mask).rounded_rectangle((0,0,339,735),radius=26,fill=255)
    m.paste(s,(10,10),mask); m.save(out)
for n,o in [('06-chat-frete','p0.png'),('03-form-preenchido','p1.png'),('02-ouvindo','p2.png'),('05-chat-sobrou','p3.png')]: phone(n,o)
# outro card
im=Image.new('RGBA',(W,H),(22,24,27,255)); d=ImageDraw.Draw(im)
ic=Image.open('/home/claude/diario-de-bordo/marketing/videos/v29-pack-27-11/icon-512.png').convert('RGBA').resize((300,300))
im.paste(ic,(390,430),ic)
def ct(t,y,s,c): 
    f=ImageFont.truetype(F,s); d.text(((W-d.textlength(t,font=f))/2,y),t,font=f,fill=c)
ct("DIÁRIO DE BORDO",800,130,WH)
ct("Veja quanto SOBROU",960,84,GR)
ct("7 DIAS DE GARANTIA",1130,96,YEL)
ct("Toque em Saiba mais",1300,84,WH)
im.save('outro.png')
