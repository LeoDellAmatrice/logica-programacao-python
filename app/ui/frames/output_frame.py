from customtkinter import CTkTextbox
import customtkinter as ctk


class OutputFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=2, column=0, sticky="nsew", padx=(16, 5), pady=(5, 16))

        self.output: CTkTextbox = self.build_frame()

    def build_frame(self):
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        ctk.CTkLabel(self, text="Output").grid(row=0, column=0, pady=(8, 4))

        output = ctk.CTkTextbox(self)
        output.grid(row=1, column=0, sticky="nsew", padx=8, pady=8)

        return output

    def set_output(self, text: tuple[bool, str]):
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", f"concluido: {text[0]}.\nMensagem: {text[1]}")
        self.output.configure(state="disabled")