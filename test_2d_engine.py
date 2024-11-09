from io import StringIO
from contextlib import redirect_stdout
from engine_2d import Engine2D, Circle, Triangle, Rectangle


def test_add_shape():
    engine = Engine2D()
    engine.add_shape(Circle(0, 0, 5))
    assert len(engine.canvas) == 1
    assert isinstance(engine.canvas[0], Circle)


def test_set_color():
    engine = Engine2D()
    engine.set_color("green")
    assert engine.color == "green"


def test_draw_shapes():
    engine = Engine2D()
    engine.set_color("yellow")
    engine.add_shape(Circle(1, 2, 3))
    engine.add_shape(Triangle(0, 0, 1, 1, 2, 0))
    engine.add_shape(Rectangle(2, 3, 4, 5))

    # Recognize the conclusion with the help of StringIO
    f = StringIO()
    with redirect_stdout(f):
        engine.draw()

    output = f.getvalue().strip().split('\n')

    assert len(output) == 3
    assert "Drawing Circle: (1, 2) with radius 3 in color yellow" in output
    assert "Drawing Triangle: (0, 0, 1, 1, 2, 0) in color yellow" in output
    assert "Drawing Rectangle: (2, 3) with width 4 and height 5 in color yellow" in output


def test_draw_clears_canvas():
    engine = Engine2D()
    engine.add_shape(Circle(0, 0, 5))
    engine.draw()
    assert len(engine.canvas) == 0  # Canvas should be cleared after drawing
