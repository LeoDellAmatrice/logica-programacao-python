import sys
import os
from PIL import Image
import customtkinter as ctk


def resource_path(relative_path: str) -> str:
    if hasattr(sys, "_MEIPASS"):
        try:
            base_path = sys._MEIPASS  # type: ignore[attr-defined]
        except AttributeError:
            base_path = "."
        return os.path.join(base_path, relative_path) # type: ignore[attr-defined]
    return relative_path


def load_logo(size=(80, 80)) -> ctk.CTkImage:
    path = resource_path("assets/images/cheetahpy.png")

    return ctk.CTkImage(
        light_image=Image.open(path),
        dark_image=Image.open(path),
        size=size
    )
