import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# Variables de transformación
translate_x = 0.0
translate_y = 0.0
scale_factor = 1.0
rotate_x = 0.0
rotate_y = 0.0

# Velocidades de transformación
TRANSLATION_SPEED = 0.1
SCALE_SPEED = 0.05
ROTATION_SPEED = 2.0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    
    # Configuración de la luz
    light_position = [0.0, 0.0, 5.0, 1.0]
    light_ambient = [0.2, 0.2, 0.2, 1.0]
    light_diffuse = [1.0, 1.0, 1.0, 1.0]
    light_specular = [1.0, 1.0, 1.0, 1.0]
    
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_diffuse)
    
    # Materiales
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialfv(GL_FRONT, GL_SHININESS, [50.0])
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glEnable(GL_COLOR_MATERIAL)

def draw_eyeball():
    # Esclerótica (parte blanca del ojo)
    glPushMatrix()
    glColor3f(0.95, 0.95, 0.95)
    glutSolidSphere(1.0, 50, 50)
    glPopMatrix()
    
    # Iris (parte coloreada)
    glPushMatrix()
    glColor3f(0.4, 0.2, 0.1)  # color café
    glTranslatef(0, 0, 0.8)
    glutSolidSphere(0.4, 50, 50)
    glPopMatrix()
    
    # Pupila
    glPushMatrix()
    glColor3f(0.0, 0.0, 0.0)
    glTranslatef(0, 0, 0.85)
    glutSolidSphere(0.2, 50, 50)
    glPopMatrix()
    
    # Reflejo en el ojo
    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glTranslatef(0.2, 0.2, 0.9)
    glutSolidSphere(0.1, 50, 50)
    glPopMatrix()
    
    # Córnea (capa transparente)
    glPushMatrix()
    glColor4f(0.8, 0.8, 1.0, 0.3)
    glutSolidSphere(0.9, 50, 50)
    glPopMatrix()

def draw_eyelids():
    # Párpado superior
    glPushMatrix()
    glColor3f(0.87, 0.72, 0.53)  # color piel
    glTranslatef(0, 0.7, 0)
    glScalef(1.5, 0.3, 1.2)
    glutSolidSphere(0.8, 50, 50)
    glPopMatrix()
    
    # Párpado inferior
    glPushMatrix()
    glColor3f(0.87, 0.72, 0.53)  # color piel
    glTranslatef(0, -0.7, 0)
    glScalef(1.5, 0.3, 1.2)
    glutSolidSphere(0.8, 50, 50)
    glPopMatrix()

def draw_eyebrow():
    # Ceja
    glPushMatrix()
    glColor3f(0.3, 0.2, 0.1)  # color café oscuro
    glTranslatef(0, 1.3, 0.5)
    glRotatef(20, 1, 0, 0)
    glScalef(1.5, 0.1, 0.3)
    glutSolidCube(1.0)
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Posición de la cámara
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)
    
    # Aplicar transformaciones globales
    glTranslatef(translate_x, translate_y, 0)
    glScalef(scale_factor, scale_factor, scale_factor)
    glRotatef(rotate_x, 1, 0, 0)
    glRotatef(rotate_y, 0, 1, 0)
    
    # Dibujar el ojo completo
    draw_eyebrow()
    draw_eyelids()
    draw_eyeball()
    
    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, float(w)/float(h), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def special_keys(key, x, y):
    global translate_x, translate_y, rotate_x, rotate_y, scale_factor
    
    # Teclas de flecha para traslación
    if key == GLUT_KEY_LEFT:
        translate_x -= TRANSLATION_SPEED
    elif key == GLUT_KEY_RIGHT:
        translate_x += TRANSLATION_SPEED
    elif key == GLUT_KEY_UP:
        translate_y += TRANSLATION_SPEED
    elif key == GLUT_KEY_DOWN:
        translate_y -= TRANSLATION_SPEED
    
    glutPostRedisplay()

def keyboard(key, x, y):
    global rotate_x, rotate_y, scale_factor
    
    key = key.decode('utf-8').lower()
    
    # Rotación con teclas WASD
    if key == 'a':
        rotate_y -= ROTATION_SPEED
    elif key == 'd':
        rotate_y += ROTATION_SPEED
    elif key == 'w':
        rotate_x -= ROTATION_SPEED
    elif key == 's':
        rotate_x += ROTATION_SPEED
    
    # Escalamiento con teclas + y -
    elif key == '+':
        scale_factor += SCALE_SPEED
    elif key == '-':
        scale_factor = max(0.1, scale_factor - SCALE_SPEED)
    
    # Resetear transformaciones
    elif key == 'r':
        reset_transformations()
    
    # Salir con ESC
    elif key == '\x1b':
        sys.exit()
    
    glutPostRedisplay()

def reset_transformations():
    global translate_x, translate_y, scale_factor, rotate_x, rotate_y
    translate_x = 0.0
    translate_y = 0.0
    scale_factor = 1.0
    rotate_x = 0.0
    rotate_y = 0.0

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Ojo Humano 3D con Controles")
    
    init()
    
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_keys)  # Para las teclas especiales (flechas)
    
    # Instrucciones de control
    print("Controles:")
    print("Flechas: Mover el ojo (traslación)")
    print("WASD: Rotar el ojo")
    print("+/-: Escalar el ojo")
    print("R: Resetear transformaciones")
    print("ESC: Salir")
    
    glutMainLoop()

if __name__ == "__main__":
    main()