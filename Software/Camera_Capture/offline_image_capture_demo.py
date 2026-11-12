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
    raise SystemExit

print("[SUCCESS] Camera initialized.")
print("[INFO] Internet connection: NOT REQUIRED")
print("[INFO] VNC session: NOT REQUIRED")
print("[INFO] Storage:", SAVE_DIR)
print("=" * 55)

# ==========================================
# AUTOMATED IMAGE ACQUISITION
# ==========================================

try:

    for count in range(1, TOTAL_IMAGES + 1):

        ret, frame = camera.read()

        if not ret:
            print("[ERROR] Image acquisition failed.")
            break

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"Drone_Image_{count:03d}_{timestamp}.jpg"

        image_path = SAVE_DIR / filename

        # Save image directly to local storage
        cv2.imwrite(str(image_path), frame)

        print(f"[CAPTURED] Image {count:02d}/{TOTAL_IMAGES}")
        print(f"[SAVED] {filename}")
        print(f"[STORAGE] Local SD/Drive simulation")
        print("-" * 55)

        # Display captured camera frame
        cv2.imshow("Offline Image Capture - Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("[INFO] Capture stopped by user.")
            break

        if count < TOTAL_IMAGES:
            time.sleep(CAPTURE_INTERVAL)

    print("\n" + "=" * 55)
    print("       IMAGE CAPTURE COMPLETED")
    print("=" * 55)

    print("[SUCCESS] Images stored locally.")
    print("[TOTAL] Images captured:",
          len(list(SAVE_DIR.glob("*.jpg"))))
    print("[FOLDER]", SAVE_DIR)
    print("[STATUS] Offline storage demonstration complete.")

except KeyboardInterrupt:
    print("\n[INFO] Capture interrupted.")

finally:
    camera.release()
    cv2.destroyAllWindows()
    print("[INFO] Camera released successfully.")
