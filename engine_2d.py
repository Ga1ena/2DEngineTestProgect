

class Engine2D:
    def __init__(self):
        self.canvas = []
        self.color = "black"  # Default color

    def set_color(self, color: str):
        self.color = color

    def add_shape(self, shape):
        self.canvas.append(shape)

    def draw(self):
        for shape in self.canvas:
            shape.draw(self.color)
        self.canvas.clear()  # Clean canvas after drawing


class Circle:
    def __init__(self, x: int, y: int, radius: int):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, color: str):
        print(f"Drawing Circle: ({self.x}, {self.y}) with radius {self.radius} in color {color}")


class Triangle:
    def __init__(self, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int):
        self.vertices = (x1, y1, x2, y2, x3, y3)

    def draw(self, color: str):
        print(f"Drawing Triangle: {self.vertices} in color {color}")


class Rectangle:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, color: str):
        print(f"Drawing Rectangle: ({self.x}, {self.y}) with width {self.width} and height {self.height} in color {color}")


'''Example of use'''
if __name__ == "__main__":
    engine = Engine2D()
    engine.add_shape(Circle(0, 1, 5))
    engine.add_shape(Triangle(0, 0, 1, 1, 2, 0))
    engine.add_shape(Rectangle(1, 1, 4, 3))

    engine.set_color("red")
    engine.draw()  # All figures should be drawn by red

    engine.set_color("blue")
    engine.add_shape(Circle(2, 3, 10))
    engine.draw()  # The circle should be drawn in blue.
