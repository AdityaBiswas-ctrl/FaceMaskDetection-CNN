import os
from typing import List

IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}

def list_images(path: str) -> List[str]:
    if os.path.isfile(path):
        return [path]
    files = []
    for root, _, fns in os.walk(path):
        for fn in fns:
            if os.path.splitext(fn)[1].lower() in IMAGE_EXTS:
                files.append(os.path.join(root, fn))
    return sorted(files)
