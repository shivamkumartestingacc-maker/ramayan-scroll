import base64
e=lambda f:'data:image/jpeg;base64,'+base64.b64encode(open(f,'rb').read()).decode()
t=open('template.html').read()
for k,f in [('__SNAKED__','snaked.jpg'),('__SNAKE__','snake.jpg'),('__DEVD__','dev_dens.jpg'),('__DEV__','dev_col.jpg'),('__DENS__','dens.jpg'),('__IMG__','src.jpg')]: t=t.replace(k,e(f))
open('index.html','w').write(t)
