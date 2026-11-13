# Model Development

This directory documents the YOLO11n object-detection model developed for the **Intelligent Electronic Surveillance with Camera-Integrated Drones** project. The model was trained on aerial imagery from the VisDrone dataset to detect people and vehicles from an overhead viewpoint.

## Model Summary

| Item | Details |
|---|---|
| Architecture | YOLO11n (Ultralytics) |
| Task | Object detection |
| Input size | 640 × 640 pixels |
| Number of classes | 10 |
| Checkpoint | [`Training/weights/best.pt`](Training/weights/best.pt) (approximately 5.45 MB) |
| Training hardware | CPU |
| Framework | Ultralytics 8.4.84 |

**Detected classes:** pedestrian, people, bicycle, car, van, truck, tricycle, awning-tricycle, bus, motor.

## Dataset

The model uses the VisDrone-DET class set. The training labels contain approximately 343,000 annotated object instances. The class distribution is visualized in [`Training/labels.jpg`](Training/labels.jpg).

The distribution is imbalanced: cars (approximately 145,000 instances) and pedestrians (approximately 79,000) account for a large share of the annotations, while tricycle, awning-tricycle and bus each have fewer than 6,000 instances. Many objects occupy relatively few pixels, which is a characteristic challenge of aerial imagery.

The dataset itself is not included in this repository directory. Refer to the official VisDrone project and its license terms before obtaining or reusing the dataset.

## Training Configuration

Training was performed in two stages. The final stage fine-tuned the best checkpoint from the earlier run for a further 20 epochs. The repository's `args.yaml` and `results.csv` document this final 20-epoch stage; the project-level training summary reports 40 epochs across the two stages.

| Parameter | Final-stage configuration |
|---|---|
| Starting weights | Best checkpoint from the earlier training run |
| Epochs | 20 |
| Batch size | 8 |
| Image size | 640 |
| Optimizer | Auto (Ultralytics default) |
| Initial learning rate (`lr0`) | 0.01 |
| Final learning-rate factor (`lrf`) | 0.01 |
| Device | CPU |
| Augmentation | Mosaic, horizontal flip, HSV, RandAugment and random erasing |

The complete final-stage configuration is available in [`Training/args.yaml`](Training/args.yaml), and epoch-wise training and validation metrics are available in [`Training/results.csv`](Training/results.csv). The training curves are in [`Training/results.png`](Training/results.png).

## Validation Results

The following metrics are reported for the final epoch of the final training stage:

| Metric | Value |
|---|---:|
| mAP@0.5 | **0.281** |
| mAP@0.5:0.95 | 0.157 |
| Precision | 0.389 |
| Recall | 0.319 |
| Best F1 (all classes) | 0.34 at confidence 0.161 |

### Per-class AP@0.5

| Class | AP@0.5 |
|---|---:|
| car | 0.713 |
| bus | 0.403 |
| van | 0.319 |
| motor | 0.310 |
| pedestrian | 0.299 |
| truck | 0.263 |
| people | 0.210 |
| tricycle | 0.164 |
| awning-tricycle | 0.082 |
| bicycle | 0.047 |

### Evaluation observations

- Cars achieved the strongest per-class AP, consistent with their larger representation in the training annotations.
- Performance was weaker for bicycle, awning-tricycle, tricycle and people. These classes are less represented and/or difficult to distinguish in small, crowded aerial scenes.
- The normalized confusion matrix indicates that some vans are classified as cars (reported normalized value: 0.42).
- Training and validation losses were still decreasing at the end of the 20-epoch fine-tuning stage. Further training and additional representative samples for minority classes may improve performance; this should be confirmed experimentally.

Evaluation plots and validation-batch visualizations are stored in [`Evaluation/`](Evaluation/).

## Directory Structure

```text
Model_Development/
├── README.md
├── Training/
│   ├── args.yaml
│   ├── results.csv
│   ├── results.png
│   ├── labels.jpg
│   └── weights/
│       ├── README.md
│       └── best.pt
├── Evaluation/
│   ├── BoxF1_curve.png
│   ├── BoxP_curve.png
│   ├── BoxPR_curve.png
│   ├── BoxR_curve.png
│   ├── confusion_matrix.png
│   ├── confusion_matrix_normalized.png
│   └── val_batch{0,1,2}_{labels,pred}.jpg
├── Results/          # Reserved for sample detection outputs
├── Dataset/          # Reserved for dataset documentation/references
└── Model_Selection/  # Reserved for model-selection notes
```

## Sample Detections

The `Results/` directory is reserved for sample detections on aerial images. Add representative input/output examples there when they are available.

## Usage

Install the framework:

```bash
pip install ultralytics==8.4.84
```

From the repository root, load the trained checkpoint and run prediction:

```python
from ultralytics import YOLO

model = YOLO("Model_Development/Training/weights/best.pt")
results = model.predict(
    source="path/to/image.jpg",
    conf=0.25,
    save=True,
)
```

A confidence threshold in the approximate range of 0.15–0.30 can be explored, guided by the F1-confidence curve. Select the threshold using validation data appropriate to the intended application; it is not a universal operating threshold.

## Limitations

- The reported mAP@0.5 of 0.281 indicates modest validation performance.
- Detection of small, distant, overlapping and crowded objects remains challenging.
- Class imbalance may contribute to weaker results for less frequent categories.
- The model was trained using CPU hardware and a limited fine-tuning schedule.
- Validate the checkpoint on representative target-platform imagery and measure end-to-end inference performance before practical deployment. The validation metrics reported here do not, by themselves, establish real-time or flight-ready performance.

## Acknowledgements and Licensing

- **VisDrone:** The class set and image naming follow the VisDrone dataset associated with the AISKYEYE team, Lab of Machine Learning and Data Mining, Tianjin University, China. Consult the official VisDrone project for dataset access and license terms before reuse.
- **Ultralytics:** Training and evaluation used the Ultralytics YOLO11 framework. Review the applicable Ultralytics license and terms for the framework, pretrained components and any derived distribution, including model weights.
- **This repository:** Source code and documentation are subject to the license provided in the repository-root `LICENSE` file.
