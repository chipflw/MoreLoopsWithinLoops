"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Chip Daniel.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------

    p1x = rectangle.corner_1.x
    p1y = rectangle.corner_1.y
    p2x = rectangle.corner_2.x
    p2y = rectangle.corner_2.y
    width = p1y - p2y
    height = p2x - p1x

    dx = -(width / 2)
    dy = height

    rectangle.attach_to(window)

    for k in range(1, n):
        p1x = p1x - dx
        p2x = p2x - dx
        p1y = p1y - dy
        p2y = p2y - dy
        newp1 = rg.Point(p1x, p1y)
        newp2 = rg.Point(p2x, p2y)
        newrec = rg.Rectangle(newp1, newp2)
        newrec.attach_to(window)

        np1x = p1x - width
        np2x = p2x - width
        newerp1 = rg.Point(np1x, p1y)
        newerp2 = rg.Point(np2x, p2y)
        newerrec = rg.Rectangle(newerp1, newerp2)
        newerrec.attach_to(window)

        for i in range(k - 1):
            np1x = np1x - width
            np2x = np2x - width
            newerp1 = rg.Point(np1x, p1y)
            newerp2 = rg.Point(np2x, p2y)
            newerrec = rg.Rectangle(newerp1, newerp2)
            newerrec.attach_to(window)




    window.render()
# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
