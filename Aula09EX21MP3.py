"""
Faca um programa em Python que reproduza o audio de um MP3
"""

import pygame
pygame.mixer.init()
pygame.mixer.music.load('themeofprontera.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()