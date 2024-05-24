import flet as ft

class Home(ft.UserControl):
    def __init__(self, page):
        super().__init__(page)

    def build(self):
        return ft.Column(
            controls=[
                ft.Container(
                 content=ft.Image(src=f"https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/5298bac0-b8bf-4c80-af67-725c1272dbb0/df4td7f-518bd788-ce19-4efc-9f39-6cafbc0f4074.jpg/v1/fill/w_1192,h_670,q_70,strp/may_the_4th_be_with_you_2022__star_wars_wallpaper_by_thekingblader995_df4td7f-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTA4MCIsInBhdGgiOiJcL2ZcLzUyOThiYWMwLWI4YmYtNGM4MC1hZjY3LTcyNWMxMjcyZGJiMFwvZGY0dGQ3Zi01MThiZDc4OC1jZTE5LTRlZmMtOWYzOS02Y2FmYmMwZjQwNzQuanBnIiwid2lkdGgiOiI8PTE5MjAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.TtAEPiYeUt-lgBhzknetcFoR2VGx23RZjB_dERsr63A")
                )
            ]
        )