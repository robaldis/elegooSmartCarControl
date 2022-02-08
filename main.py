from control import TCP
from control import Commands
import socket
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode([500,500])

def main():
    joysticks = []

    print(pygame.joystick.get_count())
    for i in range(pygame.joystick.get_count()):
        print("Joystick attached")
        joysticks.append(pygame.joystick.Joystick(i))
        joysticks[-1].init()

    width = 500
    height = 500
    x = y = 0
    while 1:
        game(joysticks, width, height, x, y)

    Robot_ip = "192.168.4.1"
    Robot_port = 100

    socket_timeout = 5

    Robot_socket = TCP.OpenSocket(Robot_ip, Robot_port, socket_timeout)
    TCP.Interact(Robot_socket, callback)
    

def get_command(event):
    if event.key == pygame.K_w:
        return Commands.CarControl(4,255)


def callback(socket):
    # get all the keypress information
    command = ""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            command = get_command()
        elif event.type == JOYAXISMOTION:
            print ("Joystick '",joysticks[event.joy].get_name(),"' axis",event.axis,"motion.")

    socket.send(command.encode())



    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0,0,255), (250,250), 75)

    pygame.display.flip()

class Game():
    def __init__(self):
        self.width = 500
        self.height = 500
        self.screen = pygame.display.set_mode([self.width,self.height])
        self.x = 0.5
        self.y = 0.5
        self.joysticks = []

        print(pygame.joystick.get_count())
        for i in range(pygame.joystick.get_count()):
            print("Joystick attached")
            self.joysticks.append(pygame.joystick.Joystick(i))
            self.joysticks[-1].init()



    def update(self):
        command = ""
        for event in pygame.event.get():
            if event.type == JOYAXISMOTION:
                print ("Joystick '",self.joysticks[event.joy].get_name(),"' axis",event.axis,"motion.")
                if (event.axis == 0):
                    self.x = (event.value+1)/2
                elif (event.axis == 1):
                    self.y = (event.value+1)/2




        screen.fill((255,255,255))
        pygame.draw.circle(screen, (0,0,255), (self.width*self.x,self.height*self.y), 75)

        pygame.display.flip()

    def run(self):
        while 1:
            self.update()

        
def game(joysticks, width, height, x, y):
    # get all the keypress information
    command = ""
    for event in pygame.event.get():
        if event.type == JOYAXISMOTION:
            print ("Joystick '",joysticks[event.joy].get_name(),"' axis",event.axis,"motion.", event.value)
            if (event.axis == 0):
                y = (event.value)
            elif (event.axis == 1):
                x = (event.value)
            """
            event.axis returns a int value from 0-4 0,1 are for y,x for left stick
            3,4 are for y,x for the right stick
            2,5 are for the left and right triggers
            event.value: returns a float value
            """


    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0,0,255), (width*x,height*y), 75)

    pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
    main()
    pygame.quit()
