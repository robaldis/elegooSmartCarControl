from control import TCP
from control import Commands
import socket
import pygame
pygame.init()
screen = pygame.display.set_mode([500,500])

def main():

    Robot_ip = "192.168.4.1"
    Robot_port = 100

    socket_timeout = 5

    Robot_socket = TCP.OpenSocket(Robot_ip, Robot_port, socket_timeout)
    TCP.Interact(Robot_socket, callback)
    

def get_command(event):
    if event.key = pygame.K_w:
        return Commands.CarControl(4,255)


def callback(socket):
    # get all the keypress information
    command = ""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            command = get_command()

    socket.send(command.encode())



    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0,0,255), (250,250), 75)

    pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()
