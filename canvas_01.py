# -*- coding: utf-8 -*-


from PIL import Image,ImageEnhance
img=Image.open('doggy.jpg')
#img.show()
img=img.convert('RGB')

enh=ImageEnhance.Brightness(img)
images=[]

for i in range(10):
    images.append(enh.enhance(i/10))
    #images[i].show()
    
#print(images)
#images[0].show()
    
out=images[0]

canvas=Image.new(out.mode, (3*out.width,3*out.height))

x,y=0,0

for i in images[1:]:
    canvas.paste(i,(x,y))
    
    if x+i.width==canvas.width:
        x=0
        y+=i.height
    else:
        x+=i.width
        
canvas.show()
canvas.save('doggy_canvas.png')