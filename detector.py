import importlib
import cv2
import numpy as np

# Importacao dinamica para evitar o erro reportMissingImports do Pylance no MediaPipe 1.0+
mp_face_mesh = importlib.import_module("mediapipe.python.solutions.face_mesh")


class FocusDetector:
    def __init__(self):
        self.face_mesh = mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        )

    def process_frame(self, frame):
        h, w, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)

        status = "Focado"
        color = (0, 255, 0)  # Verde

        if not results.multi_face_landmarks:
            return "Ausente", (0, 0, 255)  # Vermelho

        for face_landmarks in results.multi_face_landmarks:
            nose = np.array(
                [
                    face_landmarks.landmark[1].x * w,
                    face_landmarks.landmark[1].y * h,
                ]
            )
            left_eye = np.array(
                [
                    face_landmarks.landmark[33].x * w,
                    face_landmarks.landmark[33].y * h,
                ]
            )
            right_eye = np.array(
                [
                    face_landmarks.landmark[263].x * w,
                    face_landmarks.landmark[263].y * h,
                ]
            )

            eye_center = (left_eye + right_eye) / 2
            face_width = np.linalg_norm(left_eye - right_eye)

            if face_width == 0:
                continue

            horizontal_diff = abs(nose[0] - eye_center[0]) / face_width
            vertical_diff = (nose[1] - eye_center[1]) / face_width

            if (
                horizontal_diff > 0.35
                or vertical_diff > 0.65
                or vertical_diff < 0.20
            ):
                status = "Distraido"
                color = (0, 165, 255)  # Laranja

        return status, color