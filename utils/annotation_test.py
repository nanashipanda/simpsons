import os
from PIL import Image

data_path = '/home/maa/ecs_20180904/data/'
trim_path = os.path.join(data_path, 'trim_test')
annotation_txt = os.path.join(data_path, 'annotation_test.txt')

with open(annotation_txt, encoding='utf8') as f:
    for line in f:
        line = line.lstrip('./').rstrip().split(',')
        img_path = line[0]
        left = int(line[1])
        up = int(line[2])
        right = int(line[3])
        down = int(line[4])
        name = line[5]

        # Pattern 1
        print(os.path.join(data_path, img_path))
        img = Image.open(os.path.join(data_path, img_path))
        if left >= right:
            right = left+1
        if up >= down:
            down = up+1
        trim = img.crop((left, up, right, down))
        trim.save(os.path.join(trim_path, img_path[-12:]), quality=95)

        ## ToDo ##
        ## Confirm Pattern2 ##
        ## right = left + right ## 
