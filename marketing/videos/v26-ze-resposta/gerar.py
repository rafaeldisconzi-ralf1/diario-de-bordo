ze=open('ze.svg').read()
b=open('base.html').read().replace('%%ZE%%',ze)
open('index-C.html','w').write(b)
