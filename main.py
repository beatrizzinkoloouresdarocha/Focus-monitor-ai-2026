import cv2
from detector import FocusDetector


def run():
    cap = cv2.VideoCapture(0)
    detector = FocusDetector()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

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

        cv2.imshow("Focus Monitor AI", frame)

        # Pressione 'q' para sair
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()