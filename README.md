# Multimodal Customer Support Analysis

This project provides a comprehensive suite of tools for analyzing customer support interactions across multiple modalities: text, images, audio, and video. It's designed to help understand and process customer support data in various formats.

## Project Structure

```plaintext
multimodal-ch03/
├── README.md
├── data/
│   ├── mock_customer_support/  # Mock customer support interactions
│   │   └── index.html           # Example HTML file of customer support interaction video
│   ├── images/
│   │   └── sample_customer_images/ # Example screenshots
│   ├── video/
│   │   └── sample_video/          # Example video recordings
│   └── acronyms_config.json       # Configuration for acronym expansion
├── code/
│   ├── text_preprocessing/        # Text analysis modules
│   ├── image_preprocessing/       # Image processing modules
│   ├── audio_preprocessing/       # Audio analysis modules
│   ├── video_preprocessing/       # Video processing modules
│   └── integration/              # Feature fusion and summary generation
└── requirements.txt              # Project dependencies
```

## Features

### Text Processing

- Basic text cleaning and normalization
- Acronym expansion

### Image Processing

- Convert to grayscale
- Basic image resizing

### Audio Processing

- Simple audio transcription
- Audio transcription with timestamps

### Video Processing

- Keyframe extraction

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:stephenc222/multimodal-ch03.git
   cd multimodal-ch03
   ```

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Example How to run the code

To run the code, you can use the following commands once all the dependencies are installed and the virtual environment is activated:

```bash
python code/text_preprocessing/clean_text.py
```

```bash
python code/image_preprocessing/resize_and_normalize_image.py
```

```bash
python code/audio_preprocessing/transcribe_audio.py
```

```bash
python code/video_preprocessing/extract_keyframes.py
```
