"""
Author: Jeong Juntae (bestjun111@gmail.com)
Description: python3 script for patching ida64.exe
"""

# read original binary
target = open('ida.exe','rb')
target_binary = target.read()
target.close()

patched_binary = target_binary[:]

# getting PNG positions
list_png_info = []
search_idx=0
while True:
    start_pos = target_binary.find(b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a',search_idx)
    end_pos = target_binary.find(b'\x49\x45\x4e\x44\xae\x42\x60\x82', start_pos+8)+8
    if start_pos == -1 or end_pos == -1:
        break
    file_size = end_pos - start_pos
    list_png_info.append({'pos':start_pos,'len':file_size})
    search_idx = end_pos


# patch `idx`th image (0-index) with given path. image size must fit.
def patch_img(idx,imgpath):
    global patched_binary
    assert(isinstance(imgpath,str))
    img_pos = list_png_info[idx]['pos']
    img_maxlen = list_png_info[idx]['len']

    image_file = open(imgpath,'rb')
    image_binary = image_file.read()
    image_file.close()

    if(len(image_binary)) <= img_maxlen:
        patched_binary = patched_binary[:img_pos] + image_binary + b'\0'*(img_maxlen-len(image_binary)) + patched_binary[img_pos+img_maxlen:]
    else:
        print(f"cannot patch {imgpath} at position {hex(img_pos)}, image size is {hex(len(image_binary))}, which is smaller than {hex(img_maxlen)}")


# patch icon images
patch_img(0,'res/ai_256.png')
patch_img(1,'res/ai_48.png')
patch_img(2,'res/ai_96.png')
patch_img(3,'res/ai_256.png')
patch_img(3,'res/ai_16.png')


# apply
destination = open('aida.exe', 'wb')
destination.write(patched_binary)
destination.close()