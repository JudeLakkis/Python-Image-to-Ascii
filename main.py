from PIL import Image

img = Image.open('gradient.png')
basewidth = 200
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('compressed/gradient.png')

img = Image.open('compressed/gradient.png')
img_width, img_height= img.size
rgb_img = img.convert('RGB')


ascii_scale = "$@B%8&WM#*Xzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
scale = []
for i in ascii_scale:
    scale.append(i)

pixels = []
for height in range(4, img_height, 8):
    row = []
    for width in range(2, img_width, 4):
        r, g, b = rgb_img.getpixel((width, height))
        greyscale = (r + b + g)//3
        row.append((r, g, b, greyscale))
    pixels.append(row)

final = []
for i in pixels:
    line = ''
    # Failed attempt at terminal color :shrug:
    for j in i:
        # r, g, b = j[0], j[1], j[2]
        # line += '\x1b[38;2;' + str(r) + ';'+ str(g) +';'+ str(b) + 'm\\' + scale[(j[3]//5)-1] + 'x1b[0mh'
        line += scale[j[3]//5 - 1]
    final.append(line)

for i in final:
    print(i)

