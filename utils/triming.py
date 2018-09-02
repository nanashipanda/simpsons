import os
from PIL import Image

'''
characters bounding box coordinates. 
Format : filepath,x1,y1,x2,y2,character 
x1,y1 : upper left corner 
x2,y2 : lower right corner
'''

data_path = '/home/maa/ecs_20180904/data/'
trim_path = os.path.join(data_path, 'trim_data')
annotation = os.path.join(data_path, 'annotation.txt')

with open(annotation, encoding='utf8') as f:
    for line in f:
        line = line.lstrip('./').rstrip().split(',')
        img_path = line[0]
        left = int(line[1])
        upper = int(line[2])
        right = int(line[3])
        lower = int(line[4])
        name = line[5]

        print(os.path.join(data_path, img_path))
        img = Image.open(os.path.join(data_path, img_path))
        
        # 上下左右それぞれ100px以下のものは捨てる(仮)
        if left >= right - 100:
            print(img_path, ' is width too small.')
            continue
        if upper >= lower - 100:
            print(img_path, ' is height too small.')
            continue
        trim = img.crop((left, upper, right, lower))
        if not os.path.isdir(os.path.join(trim_path, name)):
            os.mkdir(os.path.join(trim_path, name))
        trim.save(os.path.join(trim_path, name, img_path[-12:]), quality=95)
