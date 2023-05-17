import xmltodict
from os import listdir, remove

path = './dataset/train/'
for filename in [f for f in listdir(path) if 'xml' in f]:
    with open(path+filename) as f:
        data = f.read()
        ln = xmltodict.parse(data)
        bndbox = ln['annotation']['object']['bndbox']
        image_width = int(ln['annotation']['size']['width'])
        image_height = int(ln['annotation']['size']['height'])

        width = int(bndbox['xmax']) - int(bndbox['xmin'])
        height = int(bndbox['ymax'])-int(bndbox['ymin'])
        x = height / 2
        y = width / 2

        text = f"0 {x / image_width} {y / image_height} {width / image_width} { height / image_height}"

        with open(path+filename.replace('xml', 'txt'), 'w') as f:
            f.write(text)

    remove(path+filename)
