from ultralytics import YOLO

# Configuration
MODEL_PATH = "yolo11n.pt"
IMAGE_SOURCE = "https://ultralytics.com/images/bus.jpg"
CONFIDENCE_THRESHOLD = 0.25


def main():
    # Load YOLO model
    try:
        model = YOLO(MODEL_PATH)
        print(f"YOLO model loaded successfully: {MODEL_PATH}")
    except Exception as error:
        print(f"Error loading YOLO model: {error}")
        return

    # Run object detection on the input image
    try:
        results = model.predict(
            source=IMAGE_SOURCE,
            conf=CONFIDENCE_THRESHOLD,
            verbose=False
        )
    except Exception as error:
        print(f"Error during image inference: {error}")
        return

    # Display detected object names and confidence scores
    total_detections = 0

    for result in results:
        if result.boxes is None or len(result.boxes) == 0:
            print("No objects detected.")
            continue

        for box in result.boxes:
            class_id = int(box.cls[0].item())
            confidence = float(box.conf[0].item())
            class_name = result.names[class_id]

            print(
                f"Detected: {class_name} | "
                f"Confidence: {confidence:.2%}"
            )
            total_detections += 1

    print(f"\nTotal objects detected: {total_detections}")


if __name__ == "__main__":
    main()
