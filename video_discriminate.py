from moviepy.editor import *


clip = VideoFileClip("video-dataset/data1.mp4").set_duration(5)
clip.preview()
