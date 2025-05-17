import cv2
import mediapipe as mp

# Inicializar MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Inicializar dibujador de MediaPipe
mp_drawing = mp.solutions.drawing_utils

# Especificaciones de dibujo para los puntos generales
general_drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1, color=(200, 100, 0))  # Puntos verdes

# Especificaciones de dibujo para los ojos y la boca
eye_mouth_drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1, color=(0, 0, 255))  # Puntos rojos

# Captura de video
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Espejo para mayor naturalidad
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Dibujar todos los landmarks con el color general
            mp_drawing.draw_landmarks(frame, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION, general_drawing_spec, general_drawing_spec)

            # Dibujar los puntos de los ojos y la boca con el color personalizado
            for idx, landmark in enumerate(face_landmarks.landmark):
                if idx in [33, 133, 159, 145, 386, 374, 263, 362]:  # Índices de los ojos
                    cv2.circle(frame, (int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])), 1, eye_mouth_drawing_spec.color, -1)
                elif idx in [61, 291, 0, 17, 269, 405]:  # Índices de la boca
                    cv2.circle(frame, (int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])), 1, eye_mouth_drawing_spec.color, -1)

    cv2.imshow("Puntos Faciales - MediaPipe", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()