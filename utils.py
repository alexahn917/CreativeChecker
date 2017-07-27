import struct
import imghdr

def required_native_img_sizes():
    sizes = {
        tuple([1200, 627]),
        tuple([80, 80]),
        tuple([128, 128]),
    }
    return sizes

def required_img_sizes():
    sizes = {
        tuple([1024, 768]),
        tuple([768, 1024]),
        tuple([480, 320]),
        tuple([320, 480]),
        tuple([320, 50]),
        tuple([728, 90]),
        tuple([336, 280]),
        tuple([300, 600]),
        tuple([300, 250])
    }
    return sizes

def optional_img_sizes():
    sizes = {
        tuple([120, 600]),
        tuple([160, 600]),
        tuple([468, 60]),
        tuple([200, 200]),
        tuple([250, 250])
    }
    return sizes

def get_image_size(fname):
    '''Determine the image type of fhandle and return its size.
    from draco'''
    with open(fname, 'rb') as fhandle:
        head = fhandle.read(24)
        if len(head) != 24:
            return
        if imghdr.what(fname) == 'png':
            check = struct.unpack('>i', head[4:8])[0]
            if check != 0x0d0a1a0a:
                return
            width, height = struct.unpack('>ii', head[16:24])
        elif imghdr.what(fname) == 'gif':
            width, height = struct.unpack('<HH', head[6:10])
        elif imghdr.what(fname) == 'jpeg':
            try:
                fhandle.seek(0)  # Read 0xff next
                size = 2
                ftype = 0
                while not 0xc0 <= ftype <= 0xcf:
                    fhandle.seek(size, 1)
                    byte = fhandle.read(1)
                    while ord(byte) == 0xff:
                        byte = fhandle.read(1)
                    ftype = ord(byte)
                    size = struct.unpack('>H', fhandle.read(2))[0] - 2
                # We are at a SOFn block
                fhandle.seek(1, 1)  # Skip `precision' byte.
                height, width = struct.unpack('>HH', fhandle.read(4))
            except Exception:  # IGNORE:W0703
                return
        else:
            return
        return tuple([width, height])