import base64
from PIL import Image
from io import BytesIO

with open("test.png", "rb") as image_file:
    data = base64.b64encode(image_file.read())
    print(data)

# im = Image.open(BytesIO(base64.b64decode(data)))
# im.save('test2.png', 'PNG')
