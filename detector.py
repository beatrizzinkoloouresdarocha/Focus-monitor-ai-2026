import cv2
import mediapipe as mp
import numpy as np


class FocusDetector:

    def __init__(self):
        base_options = mp.tasks.BaseOptions(
            model_asset_path="face_landmarker.task"
        )
        options = mp.tasks.vision.FaceLandmarkerOptions(
            base_options=base_options,
            running_mode=mp.tasks.vision.RunningMode.IMAGE,
            num_faces=1,
        )
        self.landmarker = mp.tasks.vision.FaceLandmarker.create_from_options(
            options
        )

    def process_frame(self, frame):
        h, w, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB, data=rgb_frame
        )

        results = self.landmarker.detect(mp_image)

        status = "Focado"
        color = (0, 255, 0)  # Verde

        if not results.face_landmarks:
            return "Ausente", (0, 0, 255)  # Vermelho

        for face_landmarks in results.face_landmarks:
            nose = np.array(
                [
                    face_landmarks[1].x * w,
                    face_landmarks[1].y * h,
                ]
            )
            left_eye = np.array(
                [
                    face_landmarks[33].x * w,
                    face_landmarks[33].y * h,
                ]
            )
            right_eye = np.array(
                [
                    face_landmarks[263].x * w,
                    face_landmarks[263].y * h,
                ]
            )

            eye_center = (left_eye + right_eye) / 2
            # Correção feita aqui: np.linalg.norm
            face_width = np.linalg.norm(left_eye - right_eye)

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