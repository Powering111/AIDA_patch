target = open('ida64.exe','rb')

target_binary = target.read()

cnt=1
search_idx=0
list_png_pos = []
while True:
    start_pos = target_binary.find(b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a',search_idx)
    end_pos = target_binary.find(b'\x49\x45\x4e\x44\xae\x42\x60\x82', start_pos+8)+8
    if start_pos == -1 or end_pos == -1:
        break
    file_size = end_pos - start_pos
    with open(f"out/{str(cnt)}. {hex(start_pos)}-{hex(end_pos)} ({hex(file_size)}).png","wb") as export_img:
        export_img.write(target_binary[start_pos:end_pos])
    cnt+=1
    list_png_pos.append(start_pos)
    search_idx = end_pos
print(list_png_pos)
