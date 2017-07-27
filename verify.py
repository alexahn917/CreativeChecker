# -*- coding: utf-8 -*-

import os
from utils import *

nat_sizes = required_native_img_sizes()
req_sizes = required_img_sizes()
opt_sizes = optional_img_sizes()

def is_valid_zip_file(fileName):
    fileName = fileName.lower()
    if fileName and ".zip" in fileName:
        return True
    else:
        return False

def is_valid_image_file(fileName):
    fileName = fileName.lower()
    if fileName and ".jpg" in fileName:
        return True
    elif fileName and ".jpeg" in fileName:
        return True
    elif fileName and ".png" in fileName:
        return True
    elif fileName and ".gif" in fileName:
        return True
    else:
        return False

def verify_images_in_dir(dirPath):
    error_msg = ""
    for filename in os.listdir(dirPath)[1:]:
        abs_file_path = os.path.abspath(os.path.join(dirPath, filename))
        error_msg += verify_image(abs_file_path)
    error_msg += verify_required_image_sizes(dirPath)
    return error_msg

def verify_image(abs_file_path):
    file_name = abs_file_path.split("/")[-1]
    error_msg = ""
    if not is_valid_image_file(abs_file_path):
        error_msg += "[Invalid File Type Error] : " + str(abs_file_path.split("/")[-1]) + " is not a valid image file\n"
    size = get_image_size(abs_file_path)
    if size not in nat_sizes and size not in req_sizes and size not in opt_sizes:
        error_msg += "[Invalid Size Error] for " + file_name + " : " + str(size) + "\n"
    error_msg += verify_file_size_limit(abs_file_path)

    if error_msg == "":
        error_msg = "[OK] %s\n" %file_name

    return error_msg

def verify_required_image_sizes(dirPath):
    received_img_sizes = set()
    error_msg = ""

    for filename in os.listdir(dirPath)[1:]:
        abs_file_path = os.path.abspath(os.path.join(dirPath, filename))
        if is_valid_image_file(abs_file_path):
            received_img_sizes.add(get_image_size(abs_file_path))

    for req_size in nat_sizes:
        if req_size not in received_img_sizes:
            error_msg += "[Native Requirement Error] native image size " + str(req_size) + " is missing\n"

    for req_size in req_sizes:
        if req_size not in received_img_sizes:
            error_msg += "[Requirement Error] required image size " + str(req_size) + " is missing\n"
    return error_msg

def verify_file_size_limit(abs_file_path):
    size = os.path.getsize(abs_file_path)
    error_msg = ""
    if size > 1000000:
        error_msg += ("[File Size Error] file size is larger than 1MB: %d bytes\n" %size)
    return error_msg

def verify_gif(gif_file_name):
    pass