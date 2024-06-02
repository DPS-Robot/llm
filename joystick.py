from time import sleep
from pygame.constants import JOYBUTTONDOWN, JOYAXISMOTION
import pygame
pygame.init()

#window = tk.Tk()
#canvas = tk.Canvas(window, width=500, height=500)
#canvas.pack()

joysticks = []
if(pygame.joystick.get_count() == 0):
    print("No joystick detected")
    exit()

for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()
    print("Detected", pygame.joystick.get_count(),"joysticks on ", joysticks[-1].get_name(), "'")
# Print the name of the controller
print(joysticks[0].get_name())

while(True):
    sleep(0.2)
    x = pygame.joystick.Joystick(0).get_axis(0)
    y = 0-pygame.joystick.Joystick(0).get_axis(1)
    print("X-axis: ", x, "Y-axis: ", y)
    # canvas.coords(circle, 250+x*100, 250+y*100, 260+x*100, 260+y*100)
    # window.update()    
    for event in pygame.event.get():
        if event.type == JOYBUTTONDOWN:
            if(event.button == 0):
                print("Exit button pressed!")
                exit()
