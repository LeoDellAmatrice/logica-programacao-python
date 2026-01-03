from app.services.desafio_service import DesafioService
import customtkinter as ctk


class EditorFrame(ctk.CTkFrame):
    def __init__(self, master, desafio_service: DesafioService, on_output: callable):
        super().__init__(master)


        self.grid(row=1, column=1, rowspan=2, sticky="nsew", padx=(5, 16), pady=(5, 16))

        self.desafio_service = desafio_service
        self.on_output = on_output

        self.editor = self.build_frame()



    def build_frame(self) -> ctk.CTkTextbox:
        ctk.CTkLabel(self, text="Editor").pack()
        ctk.CTkButton(self, text="executar", command=self.executar).pack()
        editor = ctk.CTkTextbox(self, height=10, width=60)
        editor.configure(wrap="none")
        editor.pack(fill="both", expand=True, padx=8, pady=8)

        return editor

    def executar(self):
        codigo = self.editor.get("1.0", "end").strip()
        resultado = self.desafio_service.validar_codigo(codigo)
        self.on_output(resultado)
