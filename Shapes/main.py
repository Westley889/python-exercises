import sys
from display import Display_shape
from triangle import trigo

# This function will set up the display for the triangle
def draw_desplay():
    shape = Display_shape(sides, angles)
    shape.screen_set()
    shape.tracer_set()
    shape.draw_triangle()
    shape.wn.mainloop()

sides = []
angles = [120, 120, 120]

for char in sys.argv:
    if char == sys.argv[0]:
        continue
    else:
        sides.append(int(char))

triangle = trigo(sorted(sides))
draw_desplay()