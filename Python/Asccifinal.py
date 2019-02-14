from PIL import Image

def makegrey(imgname, extension):
    photo = Image.open(imgname+extension)
    photo = photo.convert('1')
    return photo
def readpixels(img, x, y):
    pixel = img.load()
    return pixel[x,y]
def converter(img, imgname):
    width, height = img.size
    x = 0
    y = 0
    chars = {0: '$', 255: ' '}
    text_file = open(imgname+'.txt', 'w')
    while y <= height - 1:
        rgb = readpixels(img, x, y)
        text_file.write(chars[rgb])
        x += 1
        if x == width - 1:
            text_file.write('\n')
            x = 0
            y += 1
    text_file.close()

imgname = input("File name? ")
extension = input("File extension? ")
converter(makegrey(imgname, extension), imgname)
print("Jobs done!")
