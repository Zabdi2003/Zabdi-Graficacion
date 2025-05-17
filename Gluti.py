import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective, gluLookAt
import sys
import math

def init():
    """Configuración inicial de OpenGL"""
    glClearColor(0.5, 0.8, 1.0, 1.0)  # Fondo azul cielo
    glEnable(GL_DEPTH_TEST)           # Activar prueba de profundidad
    glEnable(GL_LIGHTING)             # Habilitar iluminación
    glEnable(GL_LIGHT0)               # Habilitar luz 0
    glEnable(GL_COLOR_MATERIAL)       # Permitir colores con iluminación

    # Configuración de la perspectiva
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 1.0, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def draw_cube():
    """Dibuja el cubo (base de la casa) con ventana y puerta"""
    glBegin(GL_QUADS)
    # Color base de la casa
    glColor3f(0.8, 0.5, 0.2)  # Marrón
    
    # Frente (sin puerta y ventana)
    glVertex3f(-1, 0, 1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    # Atrás
    glVertex3f(-1, 0, -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)

    # Izquierda
    glVertex3f(-1, 0, -1)
    glVertex3f(-1, 0, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)

    # Derecha
    glVertex3f(1, 0, -1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)

    # Arriba
    glColor3f(0.9, 0.6, 0.3)  # Color diferente para el techo
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    # Abajo
    glColor3f(0.6, 0.4, 0.2)  # Suelo más oscuro
    glVertex3f(-1, 0, -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 0, 1)
    glVertex3f(-1, 0, 1)
    glEnd()

    # Dibujar puerta
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.2, 0.0)  # Marrón oscuro para la puerta
    glVertex3f(-0.3, 0, 1.001)
    glVertex3f(0.3, 0, 1.001)
    glVertex3f(0.3, 0.7, 1.001)
    glVertex3f(-0.3, 0.7, 1.001)
    glEnd()
    
    # Manija de la puerta
    glPushMatrix()
    glColor3f(0.1, 0.1, 0.1)  # Color negro
    glTranslatef(0.25, 0.35, 1.002)
    glScalef(0.05, 0.05, 0.05)
    gluSphere(gluNewQuadric(), 1, 10, 10)
    glPopMatrix()

    # Dibujar ventana
    glBegin(GL_QUADS)
    glColor3f(0.7, 0.9, 1.0)  # Azul claro para el vidrio
    glVertex3f(0.5, 0.5, 1.001)
    glVertex3f(0.9, 0.5, 1.001)
    glVertex3f(0.9, 0.8, 1.001)
    glVertex3f(0.5, 0.8, 1.001)
    
    # Marco de la ventana
    glColor3f(0.1, 0.1, 0.1)  # Negro para el marco
    # Marco horizontal inferior
    glVertex3f(0.48, 0.48, 1.002)
    glVertex3f(0.92, 0.48, 1.002)
    glVertex3f(0.92, 0.52, 1.002)
    glVertex3f(0.48, 0.52, 1.002)
    # Marco horizontal superior
    glVertex3f(0.48, 0.78, 1.002)
    glVertex3f(0.92, 0.78, 1.002)
    glVertex3f(0.92, 0.82, 1.002)
    glVertex3f(0.48, 0.82, 1.002)
    # Marco vertical izquierdo
    glVertex3f(0.48, 0.48, 1.002)
    glVertex3f(0.52, 0.48, 1.002)
    glVertex3f(0.52, 0.82, 1.002)
    glVertex3f(0.48, 0.82, 1.002)
    # Marco vertical derecho
    glVertex3f(0.88, 0.48, 1.002)
    glVertex3f(0.92, 0.48, 1.002)
    glVertex3f(0.92, 0.82, 1.002)
    glVertex3f(0.88, 0.82, 1.002)
    # Marco cruzado vertical
    glVertex3f(0.69, 0.48, 1.002)
    glVertex3f(0.71, 0.48, 1.002)
    glVertex3f(0.71, 0.82, 1.002)
    glVertex3f(0.69, 0.82, 1.002)
    # Marco cruzado horizontal
    glVertex3f(0.48, 0.64, 1.002)
    glVertex3f(0.92, 0.64, 1.002)
    glVertex3f(0.92, 0.66, 1.002)
    glVertex3f(0.48, 0.66, 1.002)
    glEnd()

def draw_roof():
    """Dibuja el techo (pirámide) con textura de tejas"""
    glBegin(GL_TRIANGLES)
    glColor3f(0.7, 0.1, 0.1)  # Rojo más oscuro

    # Frente
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(0, 2, 0)

    # Atrás
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(0, 2, 0)

    # Izquierda
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(0, 2, 0)

    # Derecha
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(0, 2, 0)
    glEnd()

def draw_ground():
    """Dibuja un plano para representar el suelo con césped y camino"""
    # Césped
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.6, 0.2)  # Verde para el césped
    glVertex3f(-10, 0, 10)
    glVertex3f(10, 0, 10)
    glVertex3f(10, 0, -10)
    glVertex3f(-10, 0, -10)
    glEnd()
    
    # Camino a la casa
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.4, 0.4)  # Gris para el camino
    glVertex3f(-0.5, 0.01, 10)
    glVertex3f(0.5, 0.01, 10)
    glVertex3f(0.3, 0.01, 1)
    glVertex3f(-0.3, 0.01, 1)
    glEnd()

def draw_tree(x, z):
    """Dibuja un árbol en la posición especificada"""
    # Tronco
    glPushMatrix()
    glColor3f(0.4, 0.2, 0.0)
    glTranslatef(x, 0, z)
    glScalef(0.2, 1.5, 0.2)
    gluCylinder(gluNewQuadric(), 0.3, 0.3, 1, 10, 10)
    glPopMatrix()
    
    # Copa del árbol (esfera verde)
    glPushMatrix()
    glColor3f(0.0, 0.5, 0.0)
    glTranslatef(x, 1.5, z)
    gluSphere(gluNewQuadric(), 0.8, 20, 20)
    glPopMatrix()

def draw_sun():
    """Dibuja un sol en el cielo"""
    glPushMatrix()
    glColor3f(1.0, 1.0, 0.0)
    glTranslatef(5, 8, -5)
    gluSphere(gluNewQuadric(), 0.8, 20, 20)
    glPopMatrix()

def draw_house():
    """Dibuja una casa con entorno detallado"""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Configuración de la cámara
    gluLookAt(4, 3, 8,  # Posición de la cámara
              0, 1, 0,  # Punto al que mira
              0, 1, 0)  # Vector hacia arriba

    # Configurar luz
    light_pos = [5.0, 5.0, 5.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)

    draw_sun()       # Dibuja el sol
    draw_ground()    # Dibuja el suelo con césped
    draw_cube()      # Dibuja la base de la casa
    draw_roof()      # Dibuja el techo
    
    # Dibujar árboles alrededor
    draw_tree(-3, 3)
    draw_tree(3, 4)
    draw_tree(4, -2)
    draw_tree(-4, -3)

    glfw.swap_buffers(window)

def main():
    global window

    # Inicializar GLFW
    if not glfw.init():
        sys.exit()
    
    # Crear ventana de GLFW
    width, height = 800, 600
    window = glfw.create_window(width, height, "Casa 3D con Ventana, Puerta y Entorno", None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    glViewport(0, 0, width, height)
    init()

    # Bucle principal
    while not glfw.window_should_close(window):
        draw_house()
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()