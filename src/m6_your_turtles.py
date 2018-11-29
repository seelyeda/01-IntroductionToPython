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
window = rg.TurtleWindow()
dan = rg.SimpleTurtle('turtle')
dan.pen = rg.Pen('yellow', 3)
dan.speed = 10
size = 120
for k in range(6):
    dan.draw_square(size)
    dan.pen_up()
    dan.right(60)
    dan.forward(20)
    dan.left(60)
    dan.pen_down()
    size = size - 10
window.close_on_mouse_click()
import math
total = 0
for k in range(5):
    total = total + (k + 10)
    print(k, total)

print('The sum is:')
print(total)
total = 5
for k in range(3):
    total = total * k

print(total)