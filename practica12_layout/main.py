import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config
Config.set('graphics', 'width', 350)
Config.set('graphics', 'height', 350)

class Peliculas():
    def __init__(self, titulo, genero, anio):
        self.title = titulo
        self.genere = genero
        self.year = anio
    def __str__(self):
        return """
        Titulo: {}
        Genero: {}
        Año: {}
        """.format(self.title, self.genere, self.year)

class Control(BoxLayout):
    list_peliculas = []
    def __init__(self):
        super(Control, self).__init__()

    """def add(self):
        if self.name.text == "" or self.g.text == "" or self.y.text=="":
            self.lbl.text = "Tienes que rellenar los campos que se te piden"
        else: 
            self .list_peliculas.append(Peliculas(self.name.text, self.g.text, self.y.text))
    def search(self):
        for p in self.list_peliculas:
            self.lbl.text = self.lbl.text + print(p)"""
    
class MainApp(App):
    title = "Hola mundo"
    def build(self):
        return Control()

if __name__ == '__main__':
    MainApp().run()