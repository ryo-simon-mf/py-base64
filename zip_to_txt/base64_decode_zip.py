import base64
 
f = open("python-logo_2.txt", 'r')
data = f.read()
print(data)
 
img = base64.b64decode(data.encode())
f = open("python-logo3.zip", 'bw')
f.write(img)
