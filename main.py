from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(0, 250, 500, 0, screen, color)
draw_line(0, 250, 500, 500, screen, color)
draw_line(250, 0, 500, 500, screen, color)
draw_line(250, 0, 0, 500, screen, color)
draw_line(500, 250, 0, 0 , screen, color)
draw_line(500, 250, 0, 500, screen, color)
draw_line(250, 500, 0, 0, screen, color)
draw_line(250, 500, 500, 0, screen, color)

#vertical/horizontal lines
draw_line(250, 0, 250, 500, screen, color)
draw_line(0, 250, 500, 250, screen, color)

#m=1/m=-1 lines
draw_line(0, 0, 500, 500, screen, color)
draw_line(0, 500, 500, 0, screen, color)

display(screen)
save_extension(screen, 'img.png')
