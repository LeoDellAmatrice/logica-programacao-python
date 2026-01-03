from app.assets.loader_assets import load_logo
import customtkinter as ctk


class HeaderFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=0, column=0, sticky="ew", padx=0, pady=(0, 5), columnspan=2)

        self.grid_propagate(False)

        self.configure(height=75)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.image = load_logo(size=(60, 60))

        self.build_frame()

    def build_frame(self):
        # Logo
        ctk.CTkLabel(
            self,
            image=self.image,
            text=""
        ).grid(
            row=0,
            column=0,
            padx=(15, 10),
            sticky="w",
            rowspan=2
        )

        # Título
        ctk.CTkLabel(
            self,
            text="CheetahPy",
            font=ctk.CTkFont(size=22, weight="bold")
        ).grid(
            row=0,
            column=1,
            sticky="w",
            pady=(12, 0)
        )

        # Subtítulo
        ctk.CTkLabel(
            self,
            text="Aprenda lógica e Python de forma prática",
            font=ctk.CTkFont(size=13),
            text_color="gray"
        ).grid(
            row=1,
            column=1,
            sticky="w",
            pady=(0, 12)
        )


