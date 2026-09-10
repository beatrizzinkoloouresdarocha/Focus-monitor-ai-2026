import time

import cv2

from detector import FocusDetector


def run():
    cap = cv2.VideoCapture(0)
    detector = FocusDetector()

    print("Iniciando Focus Monitor... Pressione 'q' para sair.")

    # Variáveis para controle de tempo e estatísticas
    distraction_start_time = None
    prev_frame_time = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Erro ao acessar a câmera.")
            break

        # Espelhar a imagem para navegação intuitiva
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        # Detecta o nível de foco
        status, color = detector.process_frame(frame)

        # Lógica para cronometrar o tempo continuo de distração
        if status in ["Distraido", "Ausente"]:
            if distraction_start_time is None:
                distraction_start_time = time.time()
            current_distraction = int(time.time() - distraction_start_time)
        else:
            distraction_start_time = None
            current_distraction = 0

        # Cálculo de FPS (Frames por segundo)
        new_frame_time = time.time()
        fps = (
            int(1 / (new_frame_time - prev_frame_time))
            if (new_frame_time - prev_frame_time) > 0
            else 0
        )
        prev_frame_time = new_frame_time

        # 1. Exibe o Status principal
        cv2.putText(
            frame,
            f"Status: {status}",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            2,
            cv2.LINE_AA,
        )

        # 2. Exibe o Alerta de Tempo de Distração (se houver)
        if current_distraction > 0:
            cv2.putText(
                frame,
                f"Tempo Inativo: {current_distraction}s",
                (30, 90),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2,
                cv2.LINE_AA,
            )

        # 3. Exibe o FPS no canto superior direito
        cv2.putText(
            frame,
            f"FPS: {fps}",
            (w - 120, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            1,
            cv2.LINE_AA,
        )

        # Borda colorida ao redor do vídeo
        cv2.rectangle(frame, (0, 0), (w - 1, h - 1), color, 8)

        # Exibe a janela
        cv2.imshow("Focus Monitor - AI Productivity", frame)

        # Encerrar com a tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()