# pip install pillow #
from PIL import Image

# Upload original image #
img = Image.open('image.jpg')

# Mirror image and save #
mirror_img = img.transpose(Image.FLIP_LEFT_RIGHT)
mirror_img.save('mirror_image.png')
