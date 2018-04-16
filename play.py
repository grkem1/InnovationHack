import pylab
import matplotlib.pyplot as plt
import imageio
import time
filename = 'commercial.mp4'
vid = imageio.get_reader(filename,  'ffmpeg')
nums = range(1,5)
for num in nums:
    image = vid.get_data(num)
    fig = plt.figure()
    fig.suptitle('image #{}'.format(num), fontsize=20)
    plt.imshow(image)
    time.sleep(.1)
    plt.close()
# plt.show()
