import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

#    e-------f
#   /|      /|
#  / |     / |
# a-------b  |
# |  |    |  |
# |  g----|--h
# | /     | /
# c-------d

vertices = {}
vertices['a'] = [-1, 1, -1]
vertices['b'] = [1, 1, -1]
vertices['c'] = [-1, -1, -1]
vertices['d'] = [1, -1, -1]
vertices['e'] = [-1, 1, 1]
vertices['f'] = [1, 1, 1]
vertices['g'] = [-1, -1, 1]
vertices['h'] = [1, -1, 1]

vNames = ['a','b','c','d','e','f','h']
currentV = 0

edges = (
    ("a","b"),
    ("a","c"),
    ("a","e"),
    ("d","b"),
    ("d","c"),
    ("d","h"),
    ("g","c"),
    ("g","e"),
    ("g","h"),
    ("f","b"),
    ("f","e"),
    ("f","h")
    )

def checkKeyPressed(event):
    global currentV

    if event.key == pygame.K_ESCAPE:
        pygame.quit()

    elif event.key == pygame.K_RIGHT:
        vertices[vNames[currentV]][0]+=1
    elif event.key == pygame.K_LEFT:
        vertices[vNames[currentV]][0]-=1

    elif event.key == pygame.K_UP:
        vertices[vNames[currentV]][1]+=1
    elif event.key == pygame.K_DOWN:
        vertices[vNames[currentV]][1]-=1

    elif event.key == pygame.K_z:
        vertices[vNames[currentV]][2]+=1
    elif event.key == pygame.K_a:
        vertices[vNames[currentV]][2]-=1

    elif event.key == pygame.K_TAB:
        currentV = (currentV+1)%len(vNames)



def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                checkKeyPressed(event);

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
