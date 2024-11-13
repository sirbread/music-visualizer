# music-visualizer

A music visualizer application built with Python that has a many different visual effects to images or videos based on audio input. The visualizer allows you to input an image or video file, an audio file, and output a video file that syncs effects with the audio. Uses spectograms, zoom, and noise effects. These can be tweaked to your liking. (i.e. number/color of spectogram bars, noise bands, pixel sorting, etc)

## Features

- Uses librosa to filter and process the audio in order to translate the beats and sounds into visual effect intensity.
- The animation was specifically designed to work well out-of-the-box for most types of music, no tweaking needed.
- Accepts various image and video formats (e.g., JPEG, PNG, MP4, MKV) for the background plaster.
- Accepts audio formats like MP3, WAV, and FLAC for the background music.
- Uses different effects for different frequencies to create more dynamic and responsive animations, like:
  - Sine Wave Distortion: Shifts rows in the image based on a sine wave.
  - Chromatic Aberration: Adds a horizontal offset effect to color channels.
  - Noise Bands: Adds bands of noise across the image for a glitchy effect.
  - Pixel Sort: Sorts pixels horizontally based on their luminance.
  - Zoom Effect: Adds a zoom in/out effect centered on the image.

## Installation

1. Clone thy repo or download.
   
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

    Or use pip install for the following libs:
   ```bash
    pip install PySimpleGUI, numpy, pillow, matplotlib, moviepy, scipy, pydub
   ```
3. Download ffmpeg using the drive link in `ffmpeg-download.txt` for the supported version. (`music-visualizer/bin/ffmpeg-download.txt`)
4. Move this file into bin. (`music-visualizer/bin`)

## Usage

1. Run the visualizer as a lib:
    ```bash
    python -m music-visualizer
    ```
2. Input the required files in the GUI:
   - Choose an image or video file as background plaster.
   - Choose an audio file to sync the visuals.
   - **Output Video**: Specify the name of the output file (automatically saves as `.mp4`).
3. Click **Animate** to make the magic happen. (this can take upwards of 20 minutes based on your pc specs and the length of the audio file)

The application will save the input paths for each session in `save.json` and will auto-load these paths in subsequent uses.

## Requirements

- `Python 3.8+`
- `PySimpleGUI`
- `numpy`
- `matplotlib`
- `Pillow`

## "gib star pls"
