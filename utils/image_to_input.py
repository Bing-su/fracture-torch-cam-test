from typing import Union

import torch
from PIL import Image
from torchvision.transforms import InterpolationMode
from torchvision.transforms.functional import normalize, resize, to_tensor


def image_to_input(img: Union[str, Image.Image]) -> "torch.Tensor":
    if isinstance(img, str):
        img = Image.open(img).convert("L")
    img = resize(img, (512, 512), interpolation=InterpolationMode.BICUBIC)
    img = to_tensor(img)
    img = normalize(img, mean=[0.445], std=[0.269])
    return img
