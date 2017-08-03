import os
from PIL import Image

FORMATS = ["1024x768", "768x1024", "320x50", "728x90", "336x280", "300x600", "300x250", "120x600", "160x600",
           "375x667", "667x375", "200x200", "250x250", "300x600", "468x60", "1200x627"]
OUTPUT_DIRECTORY = "/generated"

class Entry(object):
    def __init__(self, filename):
        self.im = Image.open(filename)
        self.filename = filename
        self.width, self.height = self.im.size

    def __str__(self):
        return self.filename + " " + self.size()

    def size(self):
        return str(self.width) + "x" + str(self.height)

    def convert(self, format, dirPath):
        width, height = map(int, format.split("x"))

        if float(width)/float(height) < self.ratio():
            target_height = int(width/self.ratio())
            target_width = width
        else:
            target_width = int(height*self.ratio())
            target_height = height

        resized_im = self.im.resize((target_width, target_height), Image.ANTIALIAS)
        new_im = Image.new("RGB",(width,height))
        new_im.paste(resized_im, ((width-target_width)//2, (height-target_height)//2))

        if not os.path.exists(dirPath + OUTPUT_DIRECTORY):
            os.makedirs(dirPath + OUTPUT_DIRECTORY)

        new_im.save(dirPath + OUTPUT_DIRECTORY+"/"+format+".jpg")

        return ("For [%s]:\n   resized %s -> %s\n" %(str(width)+"x"+str(height), self.size(), str(target_width)+"x"+str(target_height)))

    def ratio(self):
        return float(self.width)/float(self.height)


def resize(dirPath):
    filenames = [os.path.abspath(os.path.join(dirPath, filename)) for filename in os.listdir(dirPath)]
    msg = ""
    image_files = []
    for filename in filenames:
        ext = os.path.splitext(filename)[-1].lower()
        if ext == ".jpeg" or ext == ".jpg" or ext == ".png":
            image_files.append(Entry(filename))

    for format in FORMATS:
        if format not in (entry.size() for entry in image_files):
            w, h = map(float, format.split("x"))
            ratio = w/h
            best_entry = None
            best_ratio = 999.9
            for entry in image_files:
                if (best_ratio > abs(ratio-entry.ratio())):
                    best_ratio = abs(ratio-entry.ratio())
                    best_entry = entry
            if best_entry:
                msg += best_entry.convert(format, dirPath)
    if not msg:
        msg = "No images have been resized"
    return msg