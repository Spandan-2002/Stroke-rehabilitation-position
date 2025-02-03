# Stroke-rehabilitation-position

## Overview

This project implements an Stroke-rehabilitation-position pipeline using OpenCV, Google MediaPipe, and SAM 2. The system detects and tracks hand movements in a video, generating segmentation masks for each frame and producing an output video with masked hands. Also, In this project I have used Google Colab, as SAM 2 pretrained model requires high computational power.

## Features

- Detect hands in the first frame using Google MediaPipe
- Generate hand masks for each frame using SAM 2

## Installation

### 1. Set Up Environment

```sh
conda create -n sam2 python=3.12
conda activate sam2
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

If PyTorch installation fails, refer to the [official installation guide](https://pytorch.org/get-started/locally/).

### 2. Install Dependencies

```sh
pip install -q mediapipe
pip install opencv-python
```

Follow the [SAM 2 setup instructions](https://github.com/google/sam2) for further installation steps.

## Usage

### 1. Run Hand Detection on the First Frame

This step detects hands in the first frame and provides prompts (bounding boxes, clicks, or key points) for SAM 2.

### 2. Track Hands Across Video Frames

Using the prompts from step 1, SAM 2 generates segmentation masks for all frames.

### 3. Generate Output Video

The processed video with masked hands is saved to the specified output path.

## Running the Pipeline

```sh
python main.py --input test.mp4 --output masked_video.mp4
```

## Repository Structure

```
.
├── Data/                                # Data
    ├── test.mp4                         # Sample Input Video 
├── Output/                              # Output Data
    ├── tracked_output.mp4               # Sample Output Video
├── src/                                 # Source code
│   ├── detect_hands.py                  # Hand detection with MediaPipe
│   ├── track_hands.py                   # Hand tracking using SAM 2 
├── Stroke_rehabilitation_position.ipynb # Sample input video
├── requirements.txt                     # Required dependencies
├── README.md                            # Project documentation
```

## Credits

Developed using:

- OpenCV
- Google MediaPipe
- SAM 2
- PyTorch

## License

MIT License. See `LICENSE` for details.

---

For any issues or improvements, feel free to submit a pull request or open an issue.

