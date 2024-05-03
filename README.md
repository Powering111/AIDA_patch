# AIDA Patcher
- The desired target is IDA Pro 7.7.
- This script changes application icon and startup image to Hoshino Ai (you can change image itself in res/ folder)
- It outputs modified binary `aida64.exe`.
- This program does not mutate original binary.


## Usage
copy the contents to the IDA program directory.
`ida64.exe` and `res/` should exist at the current working directory.
Run `patch_ida64.py` by either double-clicking it or using following command:

```
python3 patch_ida64.py
```
Then, `aida64.exe` will appear. You can use it as is, or overwrite existing `ida64.exe`.
You can patch `ida.exe` using `patch_ida.py`.


## Extra information
You can use `extract_png.py` script for extracting the PNG resources from the program. The result is stored at `out/` directory.

These code snippets can be applied to patch resources for arbitrary executable file.

This program only changes icon image embedded in the binary. Use Resource Hacker or other programs to change *.exe* icon.

## Contributor
- Jeong Juntae (bestjun111@gmail.com)