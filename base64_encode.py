import base64
 
f = open("images.jpeg", 'br')
b64_img = base64.b64encode(f.read())
print(str(b64_img)) # iVBORw0KGgoAAAANSUhEU・・・
 
f = open("python-logo.txt", "w")
f.write(b64_img.decode())
