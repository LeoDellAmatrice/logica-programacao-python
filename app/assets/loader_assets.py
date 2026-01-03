import customtkinter as ctk
from pathlib import Path
from PIL import Image
import sys


def resource_path(relative_path: str) -> str:
    if hasattr(sys, "_MEIPASS"):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(sys.argv[0]).resolve().parent

    return str(base_path / relative_path)


def load_logo(size=(80, 80)) -> ctk.CTkImage:
    path = resource_path("assets/images/cheetahpy.png")

    return ctk.CTkImage(
        light_image=Image.open(path),
        dark_image=Image.open(path),
        size=size
    )
