from PIL import Image
filename = "image.png"
with Image.open(filename) as image: 
    width, height = image.size 
print(width,height)  

