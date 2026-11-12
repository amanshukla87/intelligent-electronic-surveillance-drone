from ultralytics import YOLO
import cv2

# Model configuration
MODEL_PATH = "yolo11n.pt"
CAMERA_INDEX = 0
CONFIDENCE_THRESHOLD = 0.25


def main():
    # Load YOLO model
    try:
        model = YOLO(MODEL_PATH)
        print(f"YOLO model loaded successfully: {MODEL_PATH}")
    except Exception as error:
        print(f"Error loading YOLO model: {error}")
        return

    # Initialize webcam
    cap = cv2.VideoCapture(CAMERA_INDEX)

    if not cap.isOpened():
        print("Error: Unable to open the webcam.")
        cap.release()
        return

    print("Live YOLO detection started.")
    print("Press 'Q' to exit.")

    try:
        while True:
            ret, frame = cap.read()

            if not ret:
                print("Error: Unable to read frame from camera.")
                break

            # Perform object detection
            results = model.predict(
                source=frame,
                conf=CONFIDENCE_THRESHOLD,
                verbose=False
            )

            # Draw bounding boxes, labels, and confidence scores
            annotated_frame = results[0].plot()

            # Display detection output
            cv2.imshow("YOLO Live Object Detection", annotated_frame)

            # Exit when Q is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    except KeyboardInterrupt:
        print("\nDetection stopped by user.")

    except Exception as error:
        print(f"Runtime error: {error}")

    finally:
        # Release camera and close windows
        cap.release()
        cv2.destroyAllWindows()
        print("Camera released. Detection session ended.")


if __name__ == "__main__":
    main()
