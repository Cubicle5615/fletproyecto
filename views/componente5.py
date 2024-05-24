from flet import *
from models.Usuario.Usuario import Usuario

class Componente5(UserControl):
    def __init__(self, page):
        super().__init__(page)
        self.usuario = [
            Usuario('user', '422', '32', 'luke', 'eu'),
            Usuario('jhon', '3442', '332', 'Darth Revan', 'lat'),
        ]
        self.usuario_cards = GridView(
            runs_count=5,
            max_extent=350,
            spacing=5,
            run_spacing=5,
        )
        self.input_nombre = TextField(label="Nombre")
        self.input_numeroDeKills = TextField(label="Kills")
        self.input_personajeFav = TextField(label="Personaje favorito")
        self.input_servidor = TextField(label="Servidor")

        self.agregarUsuarios = ElevatedButton(text="Agregar nuevo", on_click=self.open_dlg)
        self.dlg = AlertDialog(modal=True,
                               title=Text("Nuevo Usuario"),
                               content=Column(width=600, controls=[
                                   self.input_nombre,
                                   self.input_numeroDeKills,
                                   self.input_personajeFav,
                                   self.input_servidor
                               ]),
                               actions=[
                                   ElevatedButton(text="Crear Usuario", on_click=self.crearNuevo),
                                   ElevatedButton(text="Cancelar", on_click=self.close_dlg)
                               ],
                               on_dismiss=lambda e: print("Se cerro la ventana")
                               )

    def crearNuevo(self, e):
        if self.input_servidor.value is not None:
            self.usuario.append(Usuario(self.input_nombre.value,
                                        self.input_numeroDeKills.value,
                                        self.input_personajeFav.value,
                                        self.input_servidor.value
                                        ))
            self.llenarusuario()
            self.close_dlg(e)
            self.update()

    def open_dlg(self, e):
        self.dialog = self.dlg
        self.dlg.open = True
        self.update()

    def close_dlg(self, e):
        self.dlg.open = False
        self.update()

    def llenarusuario(self):
        if self.usuario_cards.controls:
            self.usuario_cards.controls.clear()
        for usuario in self.usuario:
            self.usuario_cards.controls.append(
                Container(
                    border_radius=20,
                    bgcolor=colors.BLUE_ACCENT_100,
                    padding=10,
                    content=Column(
                        spacing=5,
                        controls=[
                            Text(f"Nombre :{usuario.nombre}", size=30, text_align=TextAlign.LEFT),
                            Text(f"Kills :{usuario.numeroDeKills}", text_align=TextAlign.CENTER, weight=FontWeight.BOLD),
                            Text(f"Personaje favorito :{usuario.personajeFav}", text_align= TextAlign.CENTER, weight=FontWeight.BOLD),
                            Text(f"Servidor :{usuario.servidor}", text_align=TextAlign.CENTER, weight=FontWeight.BOLD),
                        ]

                    )
                )
            )

    def build(self):
        self.llenarusuario()
        return Container(
            margin=10,
            padding=10,
            content=Column(
                alignment=alignment.center,
                controls=[
                    Text('Usuarios', size=50, weight=FontWeight.BOLD),
                    Text('Aqui encontraras informacion relevante sobre Usuarios'),
                    self.agregarUsuarios,
                    self.usuario_cards,
                    self.dlg
                ]
            )
        )