from PIL import Image
from PIL import ImageFilter
im = Image.open('Preston.jpg')

im.show()

print(im.format, im.size, im.mode)

# thumbnail

size = (128, 128)
im.thumbnail(size)

im.show()

im.save('Preston thumbnail.jpg', 'JPEG')

# rotating
rotated = im.rotate(45)
rotated.save('Preston rotated.jpg', 'JPEG')

rotated.show()

# transpose
transposed = im.transpose(Image.FLIP_TOP_BOTTOM)
transposed.save('Preston upside down.jpg', 'JPEG')

transposed.show()

# filter
detail = im.filter(ImageFilter.DETAIL)
detail.save('Preston detail.jpg', 'JPEG')

detail.show()

# black and white
black_white = im.convert('L')
black_white.save('Preston black_white.jpg', 'JPEG')

black_white.show()