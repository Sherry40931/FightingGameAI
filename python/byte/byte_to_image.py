from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import io
import binascii
import numpy as np
from matplotlib import pyplot as plt

from pdb import set_trace as bp

# 640 x 960 x 3

#with open('byte/wb/output_252', 'rb') as f:
#    r_data = bytearray(f.read())
#with open('byte/wb/output_252') as f:
#    test = io.BytesIO(f.read())
with open('byte/output_DisplayInfo_101','rb') as f:
    rawData = f.read()
    data = np.array([c for c in rawData], dtype=np.uint8)
bp()
imgdata = np.reshape(data, (640, 960, 3))
imgdata = np.fliplr(imgdata)
imgdata = np.flipud(imgdata)
imgdata = np.fliplr(imgdata)
# plt.imshow(imgdata)
# plt.show()
#data = array.array( 'B',  )
# bp()
plt.imsave("byte/output_DisplayInfo_256.png", imgdata)


# stream = io.BytesIO(r_data)

# img = Image.open(stream)
# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype("arial.ttf",14)
# draw.text((0, 220),"This is a test11",(255,255,0),font=font)
# draw = ImageDraw.Draw(img)
# bp()
# img = Image.frombytes('RGBA', (128,128), r_data, 'raw')
#img = Image.open(io.BytesIO(r_data))
#img = Image.open(test)
# test = io.BytesIO( f.read() )
# test.seek(0)
# testimage=test.read()
# img = Image.open(testimage)
# img.save("byte/a_test.png")

#f = open('test.png','rb')
#data = array.array( 'B', [ord(c) for c in f.read()] ) # my file system, sorta
# f2 = open('test2.png','wb'); f2.write( data.tostring() ); f2.close() # test from above
