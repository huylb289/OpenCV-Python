from PIL import Image
import os

#Create Thumbnails
infile = '../Images/baboon.png'
outfile = os.path.splitext(infile)[0] + "_thumbnail" + ".jpg"
pil_im = Image.open(infile)
pil_im.thumbnail((128,128))
pil_im.save(outfile)


#Copy and Paste Regions
infile = '../Images/baboon.png'
outfile = os.path.splitext(infile)[0] + "_copy_and_paste" + ".jpg"
pil_im = Image.open(infile)
box = (100, 100, 400, 400) #(left, upper, right, lower)
region = pil_im.crop(box)
region = region.transpose(Image.ROTATE_270)
pil_im.paste(region,box)
pil_im.save(outfile)

#Resize and Rotate
infile = '../Images/baboon.png'
outfile = os.path.splitext(infile)[0] + "_resize_and_rotate" + ".jpg"
pil_im = Image.open(infile)
pil_im.resize((128,128))
pil_im.rotate(155)
pil_im.save(outfile)
