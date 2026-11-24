# Gera index-A.html (orgânico) e index-B.html (anúncio) a partir de base.html
ze=open('ze.svg').read()
b=open('base.html').read().replace('%%ZE%%',ze)
for v in 'AB': open(f'index-{v}.html','w').write(b.replace('%%VER%%',v))
