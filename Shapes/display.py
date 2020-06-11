import turtle

class Display_shape:
    def __init__ (self, side_lengths, angles):
        self.side_lengths = side_lengths
        self.angles = angles
    # Declaring the window and the pen
    wn = turtle.Screen()
    pen = turtle.Turtle()
    # Setting up the display/screen
    def screen_set(self):
        self.wn.title("Shapes by Westley Martin-Root")
        self.wn.bgcolor("white")
        self.wn.setup(width=1000, height=720)
    # Setting up the pen/tracer
    def tracer_set(self):
        self.pen.color("black", "white")
        self.pen.shape("classic")
        self.pen.width(5)
    # Drawing a triangle
    def draw_triangle(self):
        for x in range(3):
            self.pen.forward(self.side_lengths[x])
            self.pen.left(self.angles[x])