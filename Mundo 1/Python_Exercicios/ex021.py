import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('sound.m4a')
pygame.music.play()
pygame.event.wait()