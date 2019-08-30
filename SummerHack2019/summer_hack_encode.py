import base64
import text_to_image


f = open("sample.png", 'br') #add files here
b64_img = base64.b64encode(f.read())
#print(str(b64_img)) 
f = open("sample2b64.txt", "w") #name txt file
f.write(b64_img.decode())

encoded_image_path = text_to_image.encode_file("sample2b64.txt", "s2b2e.png") #export txt file and name encoded picture