from app.ui.frames import desafio_frame, editor_frame, output_frame
from app.services.desafio_service import DesafioService
import customtkinter as ctk

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("SnakePy")

        self.minsize(800, 500)
        self.after(0, lambda: self.state("zoomed"))  # type: ignore[arg-type]

        self.bind("<F11>", lambda e: self.attributes(
            "-fullscreen",
            not self.attributes("-fullscreen")
        ))

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=4)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=5)

        self.desafios_service = DesafioService()

        self.frame_desafio = desafio_frame.DesafioFrame(master=self, desafio_service=self.desafios_service)
        self.frame_output = output_frame.OutputFrame(master=self)
        self.frame_editor = editor_frame.EditorFrame(master=self, desafio_service=self.desafios_service, on_output=self.frame_output.set_output)
