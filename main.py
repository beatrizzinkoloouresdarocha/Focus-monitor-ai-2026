import cv2

from detector import FocusDetector


def run():
    # Inicializa a captura da webcam
    cap = cv2.VideoCapture(0)

    # Verifica se a câmera abriu corretamente
    if not cap.isOpened():
        print("Erro: Não foi possível acessar a câmera.")
        return

    # Instancia o detector
    detector = FocusDetector()
    print("Iniciando monitoramento de foco... Pressione 'q' ou feche a janela para sair.")

    window_name = "Focus Monitor AI"

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Erro ao capturar o frame da câmera.")
                break

            # Processa o frame com o detector
            status, color = detector.process_frame(frame)

            # Exibe o status na tela
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

            cv2.imshow(window_name, frame)

            # Encerra se pressionar 'q'
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

            # Encerra se o usuário clicar no "X" da janela
            if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
                break

    finally:
        # Garante a liberação dos recursos ao encerrar
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    run()