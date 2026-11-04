# Intelligent Electronic Surveillance with Camera-Integrated Drones

**Summer Research Internship | Indian Institute of Technology Jodhpur (IIT Jodhpur) | 2026**

A research and engineering project focused on the development of a camera-integrated hexacopter platform for aerial surveillance, combining drone hardware integration, embedded computing, computer vision and deep-learning-based object detection.

---

## Internship Overview

| Detail | Information |
|---|---|
| Internship | Summer Research Internship 2026 |
| Institute | Indian Institute of Technology Jodhpur |
| Department | Electrical Engineering |
| Role | Summer Research Intern |
| Project Title | Intelligent Electronic Surveillance with Camera-Integrated Drones |
| Project Supervisor | Dr. Binod Kumar |
| Duration | June 2026 – July 2026 |
| Location | Jodhpur, Rajasthan, India |

## Project Overview

The project involved the development and experimental evaluation of an intelligent aerial surveillance system using a camera-equipped multirotor drone. The work covered the complete engineering workflow, beginning with drone hardware assembly and system integration, followed by flight testing, image acquisition, deep-learning model development and deployment on an onboard embedded computing platform.

An S550 hexacopter equipped with a Pixhawk flight controller and Raspberry Pi 4 was used as the experimental platform. A Raspberry Pi Camera Module V3 provided the visual input for image acquisition and processing.

For object detection, the YOLO11n model was trained using the VisDrone dataset and subsequently evaluated through image-processing experiments and deployment on the Raspberry Pi 4.

The project provided practical exposure to the integration of unmanned aerial systems, embedded hardware, computer vision and lightweight deep-learning models for aerial surveillance applications.

## Project Objectives

- Assemble and integrate a functional camera-equipped hexacopter platform.
- Configure the flight controller and associated drone hardware.
- Establish camera-based image acquisition for aerial surveillance.
- Study and implement computer-vision techniques for processing captured images.
- Prepare and use an aerial-image dataset for object detection model development.
- Evaluate lightweight deep-learning models for the intended application.
- Train and assess the selected YOLO11n model using standard object detection metrics.
- Deploy the trained model on Raspberry Pi 4 and examine its processing performance.
- Conduct hardware, flight and image-processing experiments to evaluate the integrated system.

## System Architecture

The experimental system consisted of three primary components:

**1. Aerial Platform**
- S550 Hexacopter Frame
- Pixhawk 2.4.8 Flight Controller
- Electronic Speed Controllers (ESCs)
- Brushless DC Motors and Propellers
- GPS, Compass and Radio Control System

**2. Embedded Computing and Imaging**
- Raspberry Pi 4 Model B
- Raspberry Pi Camera Module V3
- Python-based image acquisition and processing
- OpenCV

**3. Deep-Learning-Based Object Detection**
- VisDrone Dataset
- PyTorch
- Ultralytics YOLO11n
- Model training, evaluation and Raspberry Pi deployment

## Model Development and Experimental Results

The YOLO11n model was trained using the VisDrone dataset for aerial object detection.

The following results were obtained during model development and evaluation:

| Parameter | Observed Result |
|---|---:|
| Model | YOLO11n |
| Training Epochs | 40 |
| Model Size | Approximately 5.4 MB |
| mAP@50 | 28.1% |
| Precision | 38.9% |
| Recall | 31.9% |
| Raspberry Pi 4 Processing Time | Approximately 1.45 seconds per image |

The trained model was deployed on Raspberry Pi 4 for image-processing experiments. These measurements represent the observed results of the model and deployment setup used during the internship.

## Work Undertaken

The internship involved work across multiple stages of the project:

- **Drone Assembly and Hardware Integration:** Assembly of the S550 hexacopter and integration of the flight controller, propulsion system, GPS and associated hardware.
- **Flight Controller Configuration and Testing:** Initial configuration, calibration and testing of the drone platform.
- **Camera Integration and Image Acquisition:** Integration of Raspberry Pi Camera Module V3 and development of image-capture workflows.
- **Dataset Preparation:** Study and preparation of the VisDrone dataset for aerial object detection.
- **Model Selection and Training:** Exploration of object detection approaches and training of the selected YOLO11n model.
- **Model Evaluation:** Analysis of precision, recall, mAP and other available model evaluation results.
- **Embedded Deployment:** Deployment and testing of the trained model on Raspberry Pi 4.
- **Experimental Validation:** Hardware testing, drone flight experiments, image acquisition and deployment observations.

## Repository Structure

This repository maintains the technical implementation, experimental documentation and supporting material developed or collected during the internship.

| Directory / File | Description |
|---|---|
| `Documents/` | Internship reports, project documentation, problem statements, certificates and supporting research documents |
| `Hardware/` | Drone assembly, hardware components, circuit diagrams and system block diagrams |
| `Software/` | Source code, image processing, camera capture, drone integration and deployment scripts |
| `Model_Development/` | Dataset preparation, model selection, training, evaluation and experimental results |
| `Media/` | Project photographs, demonstration videos and flight-testing recordings |
| `Research_Studies/` | Additional technical studies and research projects undertaken during the internship |

## Additional Research Studies

Alongside the primary drone-surveillance project, the internship also provided an opportunity to explore other robotics and autonomous-system topics.

Supporting material and technical documentation for these studies will be maintained separately under `Research_Studies/`.

## Acknowledgement

I would like to express my sincere gratitude to **Indian Institute of Technology Jodhpur** for providing the opportunity to undertake this summer research internship.

I am thankful to **Dr. Binod Kumar**, my project supervisor, for his guidance, technical discussions and support throughout the internship. The experience provided valuable practical exposure to drone systems, embedded computing, computer vision and deep-learning-based applications.

---

## Author

**Aman Shukla**  
B.Tech – Electronics Engineering  
Bharat Ratna Sardar Vallabh Bhai Patel Rajkiya Engineering College, Basti

- GitHub: [@amanshukla87](https://github.com/amanshukla87)

---

*This repository serves as a technical record of the work, implementation, experiments and learning outcomes from the Summer Research Internship at IIT Jodhpur (2026).*
