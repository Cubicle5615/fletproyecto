import flet as ft
def NavBar (page):
    NavBar = ft.AppBar(
            leading_width=40,
            title=ft.Text("StarWars Projecto"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.OutlinedButton(text="Inicio",icon=ft.icons.HOME, on_click=lambda _: page.go('/')),
                ft.OutlinedButton(text="Facciones",icon=ft.icons. PERSON_ROUNDED, on_click=lambda _: page.go('/facciones')),
                ft.OutlinedButton(text="Personajes",icon=ft.icons. SETTINGS_ROUNDED, on_click=lambda _: page.go('/personajes')),
                ft.OutlinedButton(text="Mapa",icon=ft.icons. SETTINGS_ROUNDED, on_click=lambda _: page.go('/mapa')),
                ft.OutlinedButton(text="Usuario",icon=ft.icons. SETTINGS_ROUNDED, on_click=lambda _: page.go('/usuario')),
            ]
            
    )
    return NavBar