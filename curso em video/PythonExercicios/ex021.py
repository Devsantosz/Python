import pygame

pygame.init()
pygame.mixer.music.load('curso em video/PythonExercicios/ex021.mp3')
pygame.mixer.music.play()

input('Tocando música, aperte ENTER para parar')
pygame.mixer.music.stop()