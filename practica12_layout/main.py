from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle,Line
from functools import partial

class DrawingApp(App):

    def draw_tree(self, wid, *largs):
        wid.canvas.clear()
        with wid.canvas:
            Color(0.19,0.16,0.098)
            Rectangle(pos=(370,100), size=(60,110))
            Color(0.07,0.074,0.031)
            Line(rectangle=(370, 100, 60, 110),width=2)
            
            Color(0.24,0.89,0.19)
            Line(points=(320,240,470,240,390,350,320,240), width=45)

    def draw_star(self, wid, *largs):
        wid.canvas.clear()
        with wid.canvas:
            Color(0.92,1,0.14)
            Line(points=(300,110,390,400,490,110,270,300,520,300,300,110), width=45)
    
    def draw_house(self, wid, *largs):
        wid.canvas.clear()
        with wid.canvas:
            
            Color(0.34,0.94,0.61)
            Rectangle(pos=(280,100), size=(240,240))
            Color(0.16,0.53,0.33)
            Line(rectangle=(280, 100, 240, 240),width=2)
            
            Color(0.19,0.16,0.098)
            Rectangle(pos=(370,100), size=(60,100))
            Color(0.07,0.074,0.031)
            Line(rectangle=(370, 100, 60, 100),width=2)
            
            Color(0.19,0.16,0.098)
            Rectangle(pos=(310,240), size=(50,50))
            Color(0.07,0.074,0.031)
            Line(rectangle=(310, 240, 50, 50),width=2)
            Line(points=(335,240,335,290),width=2)
            Line(points=(310,265,360,265),width=2)
            
            Color(0.19,0.16,0.098)
            Rectangle(pos=(440,240), size=(50,50))
            Color(0.07,0.074,0.031)
            Line(rectangle=(440, 240, 50, 50),width=2)
            Line(points=(465,240,465,290),width=2)
            Line(points=(440,265,490,265),width=2)
            
            Color(0.92,1,0.14)
            Line(circle=(380,145,2),width=4)
            
            Color(0.37,0.4,0.38)
            Line(points=(270,350,520,350,390,400,270,350), width=35)
            

    def clear(self, wid, *largs):
        wid.canvas.clear()
        
    def close(self, *largs):
        DrawingApp().stop()

    def build(self):
        wid = Widget()
        
        label = Label(text='Selecciona la figura a dibujar')
        
        Color(0.07,0.074,0.031)
        btnTree = Button(text='Árbol',
                            on_press=partial(self.draw_tree,wid))

        btnStar = Button(text='Estrella',
                            on_press=partial(self.draw_star,wid))

        btnHouse = Button(text='Casa',
                            on_press=partial(self.draw_house,wid))

        btnClear = Button(text='Limpiar',
                           on_press=partial(self.clear, wid))
        
        btnClose = Button(text='Salir',
                           on_press=partial(self.close))

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(btnTree)
        layout.add_widget(btnStar)
        layout.add_widget(btnHouse)
        layout.add_widget(btnClear)
        layout.add_widget(btnClose)

        root = BoxLayout(orientation='vertical')
        root.add_widget(label)
        root.add_widget(wid)
        root.add_widget(layout)

        return root


if __name__ == '__main__':
    DrawingApp().run()