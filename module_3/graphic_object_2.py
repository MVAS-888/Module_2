class GraphicObject:
    def draw(self):
        print("Drawing a graphic object.")


class Rectangle(GraphicObject):
    def draw(self):
        print("Drawing a rectangle.")


class Clickable:
    def on_click(self):
        print("The object has been clicked.")


class Button(Rectangle, Clickable):
    def draw(self):
        print("Drawing a button.")


rect = Rectangle()
btn = Button()

rect.draw()
btn.draw()
btn.on_click()
