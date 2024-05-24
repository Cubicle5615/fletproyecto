from flet import *
from models.Faccion.Faccion import Faccion

class Componente2(UserControl):
    def __init__(self, page):
        super().__init__(page)
        self.faccion = [
            Faccion('Republica',),
            Faccion('Separatistas', ),
            Faccion('Imperio Galactico', ),
            Faccion('Rebeldes', ),
        ]
        self.faccion_cards = GridView(
            runs_count=5,
            max_extent=350,
            spacing=5,
            run_spacing=5,
        )
        self.input_faccion = TextField(label="Faccion", hint_text="Faccion")

        self.agregarFacciones = ElevatedButton(text="Agregar nuevo", on_click=self.open_dlg)
        self.dlg = AlertDialog(modal=True,
                               title=Text("Nueva Faccion"),
                               content=Column(width=600, controls=[
                                   self.input_faccion,
                               ]),
                               actions=[
                                   ElevatedButton(text="Crear Faccion", on_click=self.crearNuevo),
                                   ElevatedButton(text="Cancelar", on_click=self.close_dlg)
                               ],
                               on_dismiss=lambda e: print("Se cerro la ventana")
                               )

    def crearNuevo(self, e):
        self.faccion.append(Faccion(self.input_faccion.value))
        self.llenarfaccion()
        self.close_dlg(e)
        self.update()

    def open_dlg(self, e):
        self.dialog = self.dlg
        self.dlg.open = True
        self.update()

    def close_dlg(self, e):
        self.dlg.open = False
        self.update()

    def llenarfaccion(self):
        if self.faccion_cards.controls:
            self.faccion_cards.controls.clear()
        for faccion in self.faccion:
            self.faccion_cards.controls.append(
                Container(
                    border_radius=20,
                    bgcolor=colors.RED_ACCENT_100,
                    padding=10,
                    content=Column(
                        spacing=5,
                        controls=[
                            Text(f"Faccion :{faccion.faccion}", text_align=TextAlign.CENTER, weight=FontWeight.BOLD),
                        ]
                    )
                )
            )

    def build(self):
        self.llenarfaccion()
        return Container(
            margin=10,
            padding=10,
            content=Column(
                alignment=alignment.center,
                controls=[
                    Text('Facciones', size=50, weight=FontWeight.BOLD),
                    Text('Aqui encontraras informacion relevante sobre Facciones'),
                    self.agregarFacciones,
                    self.faccion_cards,
                    self.dlg
                ]
            )
        )