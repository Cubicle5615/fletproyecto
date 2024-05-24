from flet import *
from models.Mapa.Mapa import Mapa

class Componente6(UserControl):
    def __init__(self, page):
        super().__init__(page)
        self.mapa = [
            Mapa('Hot', 'Grande', '32', 'Dificil', 'Si'),
            Mapa('Geonosis', 'Chico', '32', 'Facil', 'No'),
        ]
        self.personajes_cards = GridView(
            runs_count=5,
            max_extent=350,
            spacing=5,
            run_spacing=5,
        )
        self.input_mapaElegido = Dropdown(
            width=100,
            options=[
                dropdown.Option("Hot"),
                dropdown.Option("Geonosis"),
                dropdown.Option("Mustafar"),
                dropdown.Option("Endor"),
            ],
        )
        self.input_tamanoMapa = TextField(label="Tamaño del Mapa")
        self.input_numerojugadores = TextField(label="Número de Jugadores")
        self.input_dificultadIA = TextField(label="Dificultad de la IA")
        self.input_activarIA = TextField(label="Activar IA")

        self.agregarMapa = ElevatedButton(text="Agregar nuevo", on_click=self.open_dlg)
        self.dlg = AlertDialog(modal=True,
                               title=Text("Nuevo Mapa"),
                               content=Column(width=600, controls=[
                                   self.input_mapaElegido,
                                   self.input_tamanoMapa,
                                   self.input_numerojugadores,
                                   self.input_dificultadIA,
                                   self.input_activarIA
                               ]),
                               actions=[
                                   ElevatedButton(text="Crear Mapa", on_click=self.crearNuevo),
                                   ElevatedButton(text="Cancelar", on_click=self.close_dlg)
                               ],
                               on_dismiss=lambda e: print("Se cerro la ventana")
                               )

    def crearNuevo(self, e):
            self.mapa.append(Mapa(self.input_mapaElegido.value,
                                  self.input_tamanoMapa.value,
                                  self.input_numerojugadores.value,
                                  self.input_dificultadIA.value,
                                  self.input_activarIA.value
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
        for mapa in self.mapa:
            self.personajes_cards.controls.append(
                Container(
                    border_radius=20,
                    bgcolor=colors.GREEN_ACCENT_100,
                    padding=10,
                    content=Column(
                        spacing=5,
                        controls=[
                            Text(f"Mapa :{mapa.mapaElegido}", size=30, text_align=TextAlign.LEFT),
                            Text(f"Tamaño :{mapa.tamanoMapa}", text_align=TextAlign.CENTER, weight=FontWeight.BOLD),
                            Text(f"Jugadores :{mapa.numerojugadores}", text_align=TextAlign.CENTER, weight=FontWeight.BOLD),
                            Text(f"Dificultad :{mapa.dificultadIA}", text_align= TextAlign.CENTER, weight=FontWeight.BOLD),
                            Text(f"IA :{mapa.activarIA}", text_align=TextAlign.CENTER, weight=FontWeight.BOLD),
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
                    Text('Mapas', size=50, weight=FontWeight.BOLD),
                    Text('Aqui encontraras informacion relevante sobre Mapas'),
                    self.agregarMapa,
                    self.personajes_cards,

                    self.dlg
                ]
            )
        )
