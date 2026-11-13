# Trained Model Weights

This directory stores the trained YOLO object-detection model checkpoints.

## Main checkpoint

Place the selected, validated model checkpoint here:

```text
best.pt
```

The expected path is:

```text
Model_Development/Training/weights/best.pt
```

Use the `best.pt` file from the specific training run whose configuration and evaluation results are documented in this directory. Verify that its architecture, class names, and training run match the accompanying `args.yaml` and `results.csv` before deployment.

Do not commit unrelated checkpoints or duplicate model files.