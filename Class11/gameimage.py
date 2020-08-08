from PIL import Image
from PIL import ImageFilter
im = Image.open('spaceship.png')

im.show()

print(im.format, im.size, im.mode)

# thumbnail

size = (64, 64)
im.thumbnail(size)

im.show()

im.save('spaceshipthumbnail.png', 'PNG')