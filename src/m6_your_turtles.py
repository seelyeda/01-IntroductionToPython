"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Dave Seelye.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg

###############################################################################
# One window, for two examples.
###############################################################################
window = rg.TurtleWindow()

###############################################################################
# Example 1.
###############################################################################
blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('midnight blue', 3)
blue_turtle.speed = 20  # Fast

# The first square will be 300 x 300 pixels:
size = 150

# Do the indented code 6 times.  Each time draws a square.
for k in range(6):
    blue_turtle.draw_square(size)
    blue_turtle.pen_up()
    blue_turtle.right(45)
    blue_turtle.forward(10)
    blue_turtle.left(45)
    blue_turtle.pen_down()
    size = size - 12
another_turtle = rg.SimpleTurtle('triangle')
another_turtle.pen = rg.Pen('magenta', 1)
another_turtle.backward(50)
for k in range(500):
    another_turtle.left(91)
    another_turtle.forward(k)

window.close_on_mouse_click()
