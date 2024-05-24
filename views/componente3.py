from flet import *
from models.Personaje.Personaje import Personaje


class Componente3(UserControl):
    def __init__(self, page):
        super().__init__(page)
        self.personajes = [
            Personaje('Separatistas', 'Blaster', 'Carga rapida', 'Vida extra', 'Pistola', 'Default'),
            Personaje('Republica', 'Espada', 'Carga normal', 'Estamina extra', 'Granada', 'Default2'),
        ]
        self.personajes_cards = GridView(
            runs_count=5,
            max_extent=350,
            spacing=5,
            run_spacing=5,
        )
        self.input_faccion = Dropdown(
            width=100,
            options=[
                dropdown.Option("Republica"),
                dropdown.Option("Separatistas"),
                dropdown.Option("Imperio Galactico"),
                dropdown.Option("Rebeldes"),
            ],
        )
        self.input_arma = TextField(label="Arma", hint_text="Arma")
        self.input_cartaHabilidad = TextField(label="Carta de Habilidad", hint_text="Carta de Habilidad")
        self.input_cartaBoosteo = TextField(label="Carta de Boosteo", hint_text="Carta de Boosteo")
        self.input_arma_secundaria = TextField(label="Arma secundaria")
        self.input_skin = TextField(label="Skin", hint_text="Skin")

        self.agregarPersonaje = ElevatedButton(text="Agregar nuevo", on_click=self.open_dlg)
        self.dlg = AlertDialog(modal=True,
                               title=Text("Nuevo personaje"),
                               content=Column(width=600, controls=[
                                   self.input_faccion,
                                   self.input_arma,
                                   self.input_cartaHabilidad,
                                   self.input_cartaBoosteo,
                                   self.input_arma_secundaria,
                                   self.input_skin
                               ]),

                               actions=[
                                   ElevatedButton(text="Crear personaje", on_click=self.crearNuevo),
                                   ElevatedButton(text="Cancelar", on_click=self.close_dlg)
                               ],
                               on_dismiss=lambda e: print("Se cerro la ventana")

                               )

    def crearNuevo(self, e):
        self.personajes.append(Personaje(self.input_faccion.value,
                                         self.input_arma.value,
                                         self.input_cartaHabilidad.value,
                                         self.input_cartaBoosteo.value,
                                         self.input_arma_secundaria.value,
                                         self.input_skin.value
                                         ))
        self.llenarPersonajes()
        self.close_dlg(e)
        self.update()

    def open_dlg(self, e):
        self.dialog = self.dlg
        self.dlg.open = True
        self.update()

    def close_dlg(self, e):
        self.dlg.open = False
        self.update()

    def llenarPersonajes(self):
        if self.personajes_cards.controls:
            self.personajes_cards.controls.clear()
        for personaje in self.personajes:
            self.personajes_cards.controls.append(
                Container(
                    border_radius=20,
                    bgcolor=colors.GREEN_ACCENT_100,
                    padding=10,
                    content=Column(
                        spacing=5,
                        controls=[
                            Text(f"Faccion :{personaje.faccion}", size=30, text_align=TextAlign.LEFT),
                            Text(f"Arma :{personaje.arma}", text_align=TextAlign.CENTER, weight=FontWeight.BOLD),
                            Text(f"Carta Habilidad :{personaje.cartaDeHabilidad}",  text_align=TextAlign.CENTER, weight=FontWeight.BOLD),
                            Text(f"Carta de boosteo :{personaje.cartaDeBoosteo}",  text_align=TextAlign.CENTER, weight=FontWeight.BOLD),
                            Text(f"Arma secundaria :{personaje.armaSecundaria}",  text_align=TextAlign.CENTER, weight=FontWeight.BOLD),
                        ]

                    )
                )
            )

    def build(self):
        self.llenarPersonajes()
        return Container(
            margin=10,
            padding=10,
            content=Column(
                alignment=alignment.center,
                controls=[
                    Text('Personajes', size=50, weight=FontWeight.BOLD),
                    Text('Aqui encontraras informacion relevante sobre personajes'),
                    self.agregarPersonaje,
                    self.personajes_cards,

                    self.dlg
                ]
            )
        )