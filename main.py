from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

for x in xrange(5):
    draw_line(0, x * 100, 500, 0, screen, color)
    draw_line(0, x * 100, 500, 500, screen, color)
    draw_line(x * 100, 0, 500, 500, screen, color)
    draw_line(x * 100, 0, 0, 500, screen, color)
    draw_line(500, x * 100, 0, 0 , screen, color)
    draw_line(500, x * 100, 0, 500, screen, color)
    draw_line(x * 100, 500, 0, 0, screen, color)
    draw_line(x * 100, 500, 500, 0, screen, color)

    #vertical/horizontal lines
    draw_line(x * 100, 0, x * 100, 500, screen, color)
    draw_line(0, x * 100, 500, x * 100, screen, color)

    #m=1/m=-1 lines are already included

display(screen)
save_extension(screen, 'img.png')
