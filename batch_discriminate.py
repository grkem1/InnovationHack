'''
Usage: python batch_discriminate.py <subscription_key> <keywords_file> <img_directory>
Example: python batch_discriminate.py 3d2346c75192488998c306c79b60e634 /Users/oeken/Desktop/InnovationHack/kw.txt /Users/oeken/Desktop/InnovationHack/img-dataset/testing
'''

import sys
from os import listdir
from discriminator import discriminate, read_kw


def is_image(filename):
    ext = filename.split('.')[-1]
    return ext == 'jpg' or ext == 'png' or ext == 'jpeg'


subs_key = sys.argv[1]
kw_file = sys.argv[2]
img_dir = sys.argv[3]

keywords = read_kw(kw_file)
filenames = listdir(img_dir)

for filename in filenames:
    if not is_image(filename):
        continue

    imgname = img_dir + '/' + filename
    res = discriminate(subs_key, keywords, imgname)
    print('{}: {}'.format(filename, res))


