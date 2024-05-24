from flet import *

class Componente4(UserControl):
    def __init__(self,page):
        super().__init__(page)

    def build(self):
        return Column(
        controls=[
            Container(
            content=Column(
                controls=[
                Text('Mapa y planetas'),
                Container(
                    on_click= lambda _: self.page.go('/mapasdisponibles'),
                    content=Column(
                        controls=[
                            Text('Click para ver los mapas disponibles',size=25,color='black'),
                            Image(src=f"https://static1.srcdn.com/wordpress/wp-content/uploads/2023/10/major-star-wars-planets-future-image.jpg?q=50&fit=contain&w=1140&h=&dpr=1.5")
                        ]
                    )
                )
                ]
            )
            )
            ]
        )