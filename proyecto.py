import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

#    a-------b
#   /|      /|
#  / |     / |
# e-------f  |
# |  |    |  |
# |  c----|--d
# | /     | /
# g-------h

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

surfaces = [
    ("g","h","f","e"),
    ("e","f","b","a"),
    ("h","d","b","f")
]

surfToMap = [
    (0,0),
    (1,0),
    (1,1),
    (0,1)
]

mode = True

def checkKeyPressed(event):
    global currentV, mode

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

    elif event.key == pygame.K_p:
        mode = not mode

def loadTexture():
    textureSurface = pygame.image.load('test.png')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid


def Cube(lines=True):
    if lines:
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()
    else:
        glBegin(GL_QUADS)
        for surface in surfaces:

            index=0
            for vertex in surface:
                glTexCoord2f(surfToMap[index][0], surfToMap[index][1])
                glVertex3fv(vertices[vertex])
                index += 1
        glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    loadTexture()

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

        Cube(mode)
        pygame.display.flip()
        pygame.time.wait(10)


main()
