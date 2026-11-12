"""
INTELLIGENT ELECTRONIC SURVEILLANCE WITH CAMERA-INTEGRATED DRONES

MODULE: OFFLINE IMAGE CAPTURE DEMONSTRATION
PLATFORM: Windows PC Webcam
PURPOSE: Demonstrate automated image acquisition
         and local storage without internet access.
"""

import cv2
import time
from datetime import datetime
from pathlib import Path

# ==========================================
# OFFLINE CAPTURE CONFIGURATION
# ==========================================

TOTAL_IMAGES = 10
CAPTURE_INTERVAL = 5

# Local storage directory
SAVE_DIR = Path.cwd() / "Offline_Captured_Images"
SAVE_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================
# CAMERA INITIALIZATION
# ==========================================

print("=" * 55)
print("       OFFLINE IMAGE CAPTURE SYSTEM")
print("=" * 55)

print("[INFO] Initializing local camera...")

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("[ERROR] Camera could not be accessed.")
    camera.release()
    raise SystemExit(1)

print("[SUCCESS] Camera initialized.")
print("[INFO] Internet connection: NOT REQUIRED")
print("[INFO] VNC session: NOT REQUIRED")
print("[INFO] Storage:", SAVE_DIR)
print("=" * 55)

# ==========================================
# AUTOMATED IMAGE ACQUISITION
# ==========================================

captured_count = 0
capture_completed = False

try:
    for count in range(1, TOTAL_IMAGES + 1):
        ret, frame = camera.read()

        if not ret:
            print("[ERROR] Image acquisition failed.")
            break

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        filename = f"Drone_Image_{count:03d}_{timestamp}.jpg"
        image_path = SAVE_DIR / filename

        # Save image directly to local storage
        if not cv2.imwrite(str(image_path), frame):
            print(f"[ERROR] Failed to save image: {filename}")
            break

        captured_count += 1

        print(f"[CAPTURED] Image {captured_count:02d}/{TOTAL_IMAGES}")
        print(f"[SAVED] {filename}")
        print("[STORAGE] Local computer filesystem")
        print("-" * 55)

        # Display captured camera frame
        cv2.imshow("Offline Image Capture - Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("[INFO] Capture stopped by user.")
            break

        if count < TOTAL_IMAGES:
            time.sleep(CAPTURE_INTERVAL)
    else:
        capture_completed = True

    print("\n" + "=" * 55)
    print("       IMAGE CAPTURE SUMMARY")
    print("=" * 55)
    print(f"[TOTAL] Images captured in this run: {captured_count}")
    print("[FOLDER]", SAVE_DIR)

    if capture_completed:
        print("[STATUS] All scheduled images captured successfully.")
    else:
        print("[STATUS] Capture ended before all scheduled images were captured.")

except KeyboardInterrupt:
    print("\n[INFO] Capture interrupted by user.")
    print(f"[TOTAL] Images captured in this run: {captured_count}")

except Exception as error:
    print(f"[ERROR] Unexpected capture error: {error}")
    print(f"[TOTAL] Images captured in this run: {captured_count}")

finally:
    camera.release()
    cv2.destroyAllWindows()
    print("[INFO] Camera released successfully.")
