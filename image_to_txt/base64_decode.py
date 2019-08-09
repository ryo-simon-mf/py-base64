import base64
 
f = open("python-logo.txt", 'r')
data = f.read()
print(data)
 
img = base64.b64decode(data.encode())
f = open("output.png", 'bw')
f.write(img)
