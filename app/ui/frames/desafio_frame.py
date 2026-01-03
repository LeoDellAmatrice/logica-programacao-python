from app.services.desafio_service import DesafioService
from app.domain.desafio import Desafio
import customtkinter as ctk
from typing import Literal


class DesafioFrame(ctk.CTkFrame):
    def __init__(self, master, desafio_service: DesafioService):
        super().__init__(master)

        # Declaração dos atributos da instância
        self.btn_anterior: ctk.CTkButton | None = None
        self.btn_proximo: ctk.CTkButton | None = None
        self.num_desafio: ctk.CTkLabel | None = None
        self.titulo: ctk.CTkLabel | None = None
        self.instrucoes: ctk.CTkTextbox | None = None

        self.grid(row=1, column=0, sticky="nsew", padx=(16, 5), pady=5)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)

        self.build_frame()

        self.desafio_service = desafio_service

        self.load_desafio()

    def build_frame(self):
        top_bar = ctk.CTkFrame(self)
        top_bar.grid(row=0, column=0, sticky="ew", pady=5)

        top_bar.columnconfigure((0, 1, 2), weight=1)

        self.btn_anterior = ctk.CTkButton(
            top_bar, text="<<  Desafio Anterior", command=lambda: self.load_desafio("anterior")
        )
        self.btn_anterior.grid(row=0, column=0, sticky="w")

        self.num_desafio = ctk.CTkLabel(
            top_bar, text="Loading...",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.num_desafio.grid(row=0, column=1)

        self.btn_proximo = ctk.CTkButton(
            top_bar, text="Próximo Desafio >>", command=lambda: self.load_desafio("proximo")
        )
        self.btn_proximo.grid(row=0, column=2, sticky="e")

        self.titulo = ctk.CTkLabel(
            self, text="Aguarde um Momento...",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.titulo.grid(row=1, column=0, pady=(0, 5))

        subtitulo = ctk.CTkLabel(
            self, text="Instruções:",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        subtitulo.grid(row=2, column=0, sticky="w", padx=10)

        self.instrucoes = ctk.CTkTextbox(self)
        self.instrucoes.insert("1.0", "Carregando instruções...")
        self.instrucoes.configure(state="disabled")
        self.instrucoes.grid(row=3, column=0, sticky="nsew", padx=10, pady=(5, 10))


    def load_desafio(self, trocar_desafio: Literal["anterior", "proximo"] = None):
        match trocar_desafio:
            case "anterior":
                desafio: Desafio = self.desafio_service.anterior()
            case "proximo":
                desafio: Desafio = self.desafio_service.proximo()
            case _:
                desafio: Desafio = self.desafio_service.get_atual()

        self.num_desafio.configure(text=f"Desafio {desafio.id_desafio}")
        self.titulo.configure(text=f"{desafio.titulo}")

        self.instrucoes.configure(state="normal")
        self.instrucoes.delete("1.0", "end")
        self.instrucoes.insert("1.0", desafio.descricao)
        self.instrucoes.configure(state="disabled")
