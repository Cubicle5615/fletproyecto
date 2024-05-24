from flet import View
from views.home import Home
from views.componente2 import Componente2
from views.componente3 import Componente3
from views.componente4 import Componente4
from views.componente5 import Componente5
from views.componente6 import Componente6
from controls.NavBar import NavBar
#from views.reservaciones import Reservaciones
def routes_handler(page):
  return {
    '/':View(
        route='/',
        controls=[
          #escribe aqui el componente que corresponda
          NavBar(page),
          Home(page)
        ]
      ),
    '/facciones':View(
        route='/facciones',
        controls=[
          #escribe aqui el componente que corresponda
          NavBar(page),
          Componente2(page)
        ]
      ),
      '/personajes':View(
        route='/personajes',
        controls=[
          #escribe aqui el componente que corresponda
          NavBar(page),
          Componente3(page)
        ]
      ),
      '/mapa':View(
        route='/mapa',
        controls=[
          #escribe aqui el componente que corresponda
          NavBar(page),
          Componente4(page)
        ]
      ),
      '/usuario':View(
        route='/usuario',
        controls=[
          #escribe aqui el componente que corresponda
          NavBar(page),
          Componente5(page)
        ]
      ),
      '/mapasdisponibles':View(
        route='/mapasdisponibles',
        controls=[
          #escribe aqui el componente que corresponda
          NavBar(page),
          Componente6(page)
        ]
      ),
    #copia y pega a partir de esta jerarquía para añadir más rutas
  }