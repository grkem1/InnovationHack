'''
Usage: python img_discriminate.py <subscription_key> <keywords_file> <img_path>
Example: python img_discriminate.py 3d2346c75192488998c306c79b60e634 /Users/oeken/Desktop/InnovationHack/kw.txt /Users/oeken/Desktop/InnovationHack/img-dataset/testing/at-kafasi.jpg
'''

import sys
from discriminator import discriminate, read_kw

subs_key = sys.argv[1]
kw_file = sys.argv[2]
img_path = sys.argv[3]

keywords = read_kw(kw_file)
print(discriminate(subs_key, keywords, img_path))
