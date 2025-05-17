import cv2
import mediapipe as mp
import numpy as np

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2)

# Función para determinar el gesto según la posición de los dedos
def reconocer_gesto(hand_landmarks, frame):
    dedos = [hand_landmarks.landmark[i] for i in range(21)]
    
    punta_pulgar = dedos[4]
    punta_indice = dedos[8]
    punta_medio = dedos[12]
    punta_anular = dedos[16]
    punta_meñique = dedos[20]
    
    base_pulgar = dedos[2]
    base_indice = dedos[5]
    base_medio = dedos[9]
    base_anular = dedos[13]
    base_meñique = dedos[17]
    
    # Determinar si están extendidos (basado en eje Y para casi todos, eje X para pulgar)
    pulgar_extendido = abs(punta_pulgar.x - base_pulgar.x) > 0.06
    indice_extendido = punta_indice.y < base_indice.y
    medio_extendido = punta_medio.y < base_medio.y
    anular_extendido = punta_anular.y < base_anular.y
    meñique_extendido = punta_meñique.y < base_meñique.y

    distancia_pulgar_indice = np.linalg.norm([punta_pulgar.x - punta_indice.x, punta_pulgar.y - punta_indice.y])
    distancia_pulgar_medio = np.linalg.norm([punta_pulgar.x - punta_medio.x, punta_pulgar.y - punta_medio.y])
    distancia_pulgar_anular = np.linalg.norm([punta_pulgar.x - punta_anular.x, punta_pulgar.y - punta_anular.y])
    
    # Letra I
    if not indice_extendido and not medio_extendido and not anular_extendido and meñique_extendido:
        return "I"
    
    # Letra S
    elif not indice_extendido and not medio_extendido and not anular_extendido and not meñique_extendido and punta_pulgar.y > base_indice.y:
        return "S"
    
    # Letra B
    elif indice_extendido and medio_extendido and anular_extendido and meñique_extendido and pulgar_extendido:
        return "B"
    
    # Número 6: pulgar y meñique extendidos, otros doblados
    elif indice_extendido and not medio_extendido and not anular_extendido and not pulgar_extendido and meñique_extendido:
        return "6"
    
    # Número 30: solo índice y medio extendidos
    elif indice_extendido and medio_extendido and not anular_extendido and not meñique_extendido:
        return "30"
    
    # Número 52: todos extendidos + pulgar cerca del anular (distancia ajustada)
    elif indice_extendido and medio_extendido and anular_extendido and meñique_extendido and distancia_pulgar_anular < 0.08:
        return "52"
    
    return "Desconocido"



# Función para reconocer la palabra "Papá" (necesita dos manos)
def reconocer_papa(hand_landmarks_list):
    if len(hand_landmarks_list) != 2:
        return False
    
    # "Papá" en LSM: Ambas manos haciendo el gesto de la letra P (similar a B pero con pulgar tocando la palma)
    mano1 = hand_landmarks_list[0]
    mano2 = hand_landmarks_list[1]
    
    gesto_mano1 = reconocer_gesto(mano1, None)
    gesto_mano2 = reconocer_gesto(mano2, None)
    
    return gesto_mano1 == "B" and gesto_mano2 == "B"

# Captura de video en tiempo real
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir a RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Procesar la imagen con MediaPipe
    results = hands.process(frame_rgb)

    # Dibujar puntos de la mano y reconocer gestos
    if results.multi_hand_landmarks:
        hand_landmarks_list = results.multi_hand_landmarks
        
        # Verificar si es la palabra "Papa"
        if reconocer_papa(hand_landmarks_list):
            cv2.putText(frame, "Palabra: Papa", (50, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        else:
            for hand_landmarks in hand_landmarks_list:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                # Identificar el gesto
                gesto_detectado = reconocer_gesto(hand_landmarks, frame)

                # Mostrar el gesto en pantalla
                cv2.putText(frame, f"Gesto: {gesto_detectado}", (50, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Mostrar el video
    cv2.imshow("Reconocimiento de LSM", frame)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()