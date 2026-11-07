# Pixhawk Firmware Installation

This folder documents the installation of ArduPilot firmware on the **Pixhawk 2.4.8** flight controller used in the S550 hexacopter surveillance-drone platform.

## Purpose

Install and verify the flight-controller firmware before configuring the vehicle frame, calibrating sensors, or setting up flight outputs and safety functions.

## Hardware and software

- **Flight controller:** Pixhawk 2.4.8
- **Vehicle:** S550 hexacopter
- **Ground control station:** Mission Planner
- **Firmware family:** ArduPilot Copter

> **Important:** Pixhawk 2.4.x boards can use different sensor components or board variants. Confirm the exact board/firmware target and check for sensor compatibility before flashing. Do not assume every board sold as Pixhawk 2.4.8 is identical.

## Installation procedure

1. **Prepare the vehicle.** Remove all propellers before connecting or configuring the flight controller. Keep the battery and motor power disconnected during USB firmware installation.
2. **Connect the Pixhawk.** Connect the flight controller directly to the computer using a suitable USB cable. Avoid USB hubs where possible.
3. **Open Mission Planner.** Allow the computer to detect the board. In Mission Planner, leave the vehicle disconnected; firmware installation is performed from the disconnected state.
4. **Open the firmware page.** Navigate to **SETUP / Initial Setup → Install Firmware**.
5. **Select the firmware.** Choose the **ArduCopter** firmware appropriate for the Pixhawk board. Select the stable release offered by Mission Planner unless the project specifically requires another verified version. If Mission Planner asks for a vehicle/frame option, choose the appropriate hexacopter option where available.
6. **Confirm and flash.** Accept the installation prompt and follow Mission Planner's instructions. Do not unplug the USB cable or interrupt the process while the firmware is being erased, programmed, and verified.
7. **Wait for completion.** Confirm that Mission Planner reports a successful upload (for example, **Upload Done**). Allow the flight controller time to reboot.
8. **Reconnect and verify.** Reconnect to the Pixhawk and confirm that Mission Planner identifies the flight controller and reports the expected ArduCopter firmware information. Record the displayed firmware version and date in the project notes.

## After installation

Continue with the setup documentation in this repository:

1. [Frame Type Configuration](../Frame_Type/README.md) — configure the S550 as a hexacopter using the appropriate frame class and frame type.
2. [Calibration](../../Calibration/README.md) — complete the required accelerometer, compass, radio, and ESC procedures.
3. [Output Configuration](../../Output_Configuration/README.md) — verify motor/servo output assignments and serial-port settings.
4. [Flight Safety](../../Flight_Safety/README.md) — configure flight modes and failsafes.

Firmware installation alone does not make the aircraft ready to fly. Complete and verify all required configuration, calibration, and pre-arm checks before any powered test or flight.

## Screenshots to add

Store project-specific Mission Planner screenshots in this folder, using clear filenames such as:

- `01_Mission_Planner_Install_Firmware.png` — Install Firmware page before flashing
- `02_ArduCopter_Firmware_Selection.png` — selected firmware/vehicle option
- `03_Firmware_Upload_Complete.png` — successful upload status
- `04_Pixhawk_Firmware_Verification.png` — connected board and detected firmware version

Only add screenshots captured from the actual project setup. Do not use illustrative screenshots as evidence that firmware was installed on this flight controller.

## Troubleshooting notes

- If the board is not detected, check the USB cable, USB port, and device/driver recognition before attempting another flash.
- If Mission Planner cannot load firmware, identify whether the board has a compatible ArduPilot bootloader. Boards without one may require the separate bootloader/DFU procedure documented by ArduPilot; do not attempt that procedure unless the exact board and loading method are confirmed.
- If the upload fails or the board reports unexpected sensor/pre-arm errors, stop and verify the board variant and firmware target rather than repeatedly flashing different builds.

## References

- [ArduPilot: Loading Firmware](https://docs.ardupilot.org/planner/docs/common-loading-firmware.html)
- [ArduPilot: Loading Firmware to Boards with an ArduPilot-Compatible Bootloader](https://ardupilot.org/planner/docs/common-loading-firmware-onto-pixhawk.html)
- [Mission Planner: Initial Setup](https://ardupilot.org/planner/docs/mission-planner-initial-setup.html)
