from edit import *
L='/home/claude/ugc/lib/'
build(dict(dir='/home/claude/ugc/c/build',video='/home/claude/ugc/c/c.mp4',out='/home/claude/ugc/c/ugc-c-final.mp4',
icon='/home/claude/diario-de-bordo/marketing/videos/v29-pack-27-11/icon-512.png',
caps=[("OLHA COMO É SIMPLES.",{"SIMPLES.":"Y"},0,1.1),
("ABASTECEU,",{"ABASTECEU,":"Y"},1.1,2.15),
("APERTA O MICROFONE E FALA O VALOR.",{"MICROFONE":"Y","VALOR.":"Y"},2.15,4.5),
("PRONTO,",{},4.5,5.15),
("O APP ANOTA E MOSTRA QUANTO",{"ANOTA":"Y"},5.15,6.75),
("SOBROU.",{"SOBROU.":"G"},6.75,8.3)],
overlays=[dict(png=L+'p1.png',x=690,y=840,a=1.1,b=2.15),dict(png=L+'p2.png',x=690,y=840,a=2.15,b=4.5),dict(png=L+'p3.png',x=690,y=840,a=4.5,b=8.3)],
outro=[("DIÁRIO DE BORDO",130,WH),("Veja quanto SOBROU",84,GR),("7 DIAS DE GARANTIA",96,YEL),("Toque em Saiba mais",84,WH)],
outro_at=8.3,
sfx=[('whoosh',1.05),('pop',1.15),('whoosh',2.1),('pop',2.2),('click',3.4),('whoosh',4.45),('pop',4.55),('whoosh',5.1),('whoosh',6.7),('ding',6.85),('coin',6.9),('whoosh',8.2),('pop',8.4)]))
