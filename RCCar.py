from control import Commands
import pygame
from pygame.locals import JOYAXISMOTION
from joyStick import JoyStick
import math
from control import TCP


pygame.init()

class RCCar():
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
            self.controller = JoyStick()

    def update(self, socket):
        command = ""
        for event in pygame.event.get():
            if event.type == JOYAXISMOTION:
                print("something")
                self.controller.update(event)
                # print ("Joystick '",self.joysticks[event.joy].get_name(),"' axis",event.axis,"motion.")
                command = self.get_joystick_command()
                print(command)

        socket.send(command.encode())

        self.screen.fill((255,255,255))
        pygame.draw.circle(self.screen, (0,0,255), (self.width*self.controller.x,self.height*self.controller.y), 75)

        pygame.display.flip()


    def run(self):
        self.connect_socket()

    def get_joystick_command(self):
        d = 0
        r, theta = self.controller.get_polar_coords()
        joy_d = math.floor(((theta+22.5)%360)/45)
        if (r < 0.5):
            d = 0
        elif (joy_d == 0):
            d = 1
        elif (joy_d == 1):
            d = 6
        elif (joy_d == 2):
            d = 4
        elif (joy_d == 3):
            d = 8
        elif (joy_d == 4):
            d = 2
        elif (joy_d == 5):
            d = 7
        elif (joy_d == 6):
            d = 3
        elif (joy_d == 7):
            d = 4

        return Commands.JoystickMovement(d)



    def connect_socket(self):
        Robot_ip = "192.168.4.1"
        Robot_port = 100

        socket_timeout = 5

        Robot_socket = TCP.OpenSocket(Robot_ip, Robot_port, socket_timeout)
        TCP.Interact(Robot_socket, self.update)



if __name__ == "__main__":
    car = RCCar()
    car.run()
