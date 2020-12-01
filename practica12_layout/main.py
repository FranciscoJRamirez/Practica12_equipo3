from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle
from random import random
from functools import partial


class Practica12(App):

    def masCuadros(self, label, wid, count, *largs):
        label.text = str(int(label.text) + count)
        with wid.canvas:
            for x in range(count):
                Color(random(), 10, 10, mode='hsv')
                Rectangle(pos=(random() * wid.width + wid.x,
                               random() * wid.height + wid.y), size=(20, 20))

    def limpiarCuadros(self, label, wid, *largs):
        label.text = '0'
        wid.canvas.clear()

    def build(self):
        wid = Widget()

        label = Label(text='0')

        addTen = Button(text='Dibujar 10',
                            on_press=partial(self.masCuadros, label, wid, 10))

        addFifty = Button(text='Dibujar 50',
                            on_press=partial(self.masCuadros, label, wid, 50))

        limpiar = Button(text='Reset',
                           on_press=partial(self.limpiarCuadros, label, wid))

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(addTen)
        layout.add_widget(addFifty)
        layout.add_widget(limpiar)
        layout.add_widget(label)

        root = BoxLayout(orientation='vertical')
        root.add_widget(wid)
        root.add_widget(layout)

        return root


if __name__ == '__main__':
    Practica12().run()