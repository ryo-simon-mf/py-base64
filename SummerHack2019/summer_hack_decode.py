import text_to_image
import base64

decoded_file_path = text_to_image.decode_to_file("s2b2e.png", "output_text_file.txt")


f = open("output_text_file.txt", 'r') #export txt file and read
data = f.read()
print(data)

img = base64.b64decode(data.encode())
f = open("aaaa.png", 'bw') #name original picture data
f.write(img)