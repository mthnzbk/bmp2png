from PIL import Image
import glob
import sys

files = glob.glob("*.bmp")
print(files)

for im in files:
	img = Image.open(im)
	if "--alpha" in sys.argv:
		img = img.convert("RGBA")
		data = img.getdata()
		new_data = []
		for item in data:
			if item[0] == 255 and item[1] == 255 and item[2] == 255:
				new_data.append((255, 255, 255, 0))

			else:
				new_data.append(item)

		img.putdata(new_data)
	img.save(im.split(".")[0]+".png", "PNG")