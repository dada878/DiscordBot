from PIL import Image,ImageFont,ImageDraw
import requests

def download_image(url):
    r=requests.get(url)
    with open('./imger/image.png','wb') as f:
        f.write(r.content)


def image_border(img_ori, width=3, color=(0, 0, 0)):
    # 读取图片
    w = img_ori.size[0]
    h = img_ori.size[1]

    # 添加边框
    w += 2*width
    h += 2*width
    img_new = Image.new(mode='RGB', size=(w, h), color=color)   # 创建一张新图
    img_new.paste(img_ori, box=(width, width))    # 将原图粘贴到新图

    # 保存图片
    return img_new

def text_border(text ,draw, x, y, font, shadowcolor, fillcolor, border_size):
    # thin border
    draw.text((x - border_size, y), text, font=font, fill=shadowcolor)
    draw.text((x + border_size, y), text, font=font, fill=shadowcolor)
    draw.text((x, y - border_size), text, font=font, fill=shadowcolor)
    draw.text((x, y + border_size), text, font=font, fill=shadowcolor)
 
    # thicker border
    draw.text((x - border_size, y - border_size), text, font=font, fill=shadowcolor)
    draw.text((x + border_size, y - border_size), text, font=font, fill=shadowcolor)
    draw.text((x - border_size, y + border_size), text, font=font, fill=shadowcolor)
    draw.text((x + border_size, y + border_size), text, font=font, fill=shadowcolor)
 
    # now draw the text over it
    draw.text((x, y), text, font=font, fill=fillcolor)


def level_imger(name,level):
    font = ImageFont.truetype('./imger/GenYoGothic-B.ttc', 35, encoding='utf-8')
    font2 = ImageFont.truetype('./imger/GenYoGothic-B.ttc', 100, encoding='utf-8')

    image1 = Image.open('./imger/image.png')
    background = Image.open('./imger/background.png')

    size = 180,180
    image1.thumbnail(size) # 100x300

    image1 = image_border(image1)

    background.paste(image1, (10, 7))

    draw = ImageDraw.Draw(background)
    text_border(f"恭喜{name}升級！",draw,210,30,font,"white","#000",3)
    text_border(f"{level-1} → {level}",draw,210,80,font2,"yellow","#000",5)

    background.save("./imger/image.png")