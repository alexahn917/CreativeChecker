import os
from PIL import Image

FORMATS = ["1024x768", "768x1024", "320x50", "728x90", "336x280", "300x600", "300x250", "120x600", "160x600",
           "375x667", "667x375", "200x200", "250x250", "300x600", "468x60"]
OUTPUT_DIRECTORY = "generated"

class Entry(object):
    def __init__(self, filename):
        self.im = Image.open(filename)
        self.filename = filename
        self.width, self.height = self.im.size

    def __str__(self):
        return self.filename + " " + self.size()

    def size(self):
        return str(self.width) + "x" + str(self.height)

    def convert(self, format):
        width, height = map(int, format.split("x"))
        print("For "+ str(width) + "x" + str(height) + " : ")

        if width/height < self.ratio():
            target_height = int(width/self.ratio())
            target_width = width
        else:
            target_width = int(height*self.ratio())
            target_height = height

        print("Converting : "+self.size() + " -> " + str(target_width) + "x" + str(target_height))

        resized_im = self.im.resize((target_width, target_height), Image.ANTIALIAS)
        new_im = Image.new("RGB",(width,height))
        new_im.paste(resized_im, ((width-target_width)//2, (height-target_height)//2))

        if not os.path.exists(OUTPUT_DIRECTORY):
            os.makedirs(OUTPUT_DIRECTORY)

        new_im.save(OUTPUT_DIRECTORY+"/"+format+".jpg")
        new_im.show()
        print()

    def ratio(self):
        return float(self.width)/float(self.height)


def resize(filenames):
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
                # print ratio-entry.ratio()
                if ( entry.width>=w or entry.height>=h ) and ( best_ratio > abs(ratio-entry.ratio())):
                    best_ratio = abs(ratio-entry.ratio())
                    best_entry = entry
            best_entry.convert(format)
            msg += ("Resized [%s] -> [%s]\n" %(str(best_entry).split(" ")[1], format))
    return msg