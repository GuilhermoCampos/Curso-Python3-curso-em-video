import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021b.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
