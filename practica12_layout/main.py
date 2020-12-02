from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Line, Ellipse
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.stencilview import StencilView
from random import random as r
from functools import partial


class StencilWidget(StencilView):

    def on_touch_down(self, touch):
        self.pos = touch.pos
        self.size = (1, 1)

    def on_touch_move(self, touch):
        self.size = (touch.x - touch.ox, touch.y - touch.oy)


class Practica12(App):

    def dibujarCirculos(self, label, wid, count, *largs):
        label.text = str(int(label.text) + count)
        with wid.canvas:
            for x in range(count):
                Color(r(), 10, 10, mode='hsv')
                Ellipse(pos=(r() * wid.width + wid.x, r() * wid.height + wid.y), size=(10,10))

    def nuevoBloque(self, wid, *largs):
        wid.pos = (0, 0)
        wid.size = Window.size

    def limpiarCirculos(self, label, wid, *largs):
        label.text = '0'
        wid.canvas.clear()

    def build(self):
        wid = StencilWidget(size_hint=(None, None), size=Window.size)

        label = Label(text='0')

        dibujar = Button(text='Dibujar Circulos')
        dibujar.bind(on_press=partial(self.dibujarCirculos, label, wid, 100))

        limpiar = Button(text='Limpiar circulos')
        limpiar.bind(on_press=partial(self.limpiarCirculos, label, wid))

        nuevo = Button(text='Mostrar toda la pantalla')
        nuevo.bind(on_press=partial(self.nuevoBloque, wid))

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(dibujar)
        layout.add_widget(limpiar)
        layout.add_widget(nuevo)
        layout.add_widget(label)

        root = BoxLayout(orientation='vertical')
        rfl = FloatLayout()
        rfl.add_widget(wid)
        root.add_widget(rfl)
        root.add_widget(layout)

        return root


if __name__ == '__main__':
    Practica12().run()