# YouTube Video Downloader and Audio Extractor

A Python script for downloading YouTube videos, extracting audio, and performing audio-to-text transcription using OpenAI's Whisper model. This tool is designed to work seamlessly in both Google Colab and local environments.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/GCollab/blob/main/YT_DLP_Extract_Audio_Audio_to_Text.ipynb)

## Features

- 🎥 **Video Download**
  - Download YouTube videos in various qualities (720p, 1080p, 4K)
  - Automatic quality selection based on availability
  - Smart format detection and selection
  - Progress tracking during download

- 🎵 **Audio Extraction**
  - Extract high-quality MP3 audio (192kbps)
  - Direct audio extraction without video download
  - Optional local file download
  - Support for various audio formats

- 🗣️ **Audio Transcription**
  - Transcribe audio using OpenAI's Whisper model
  - Multiple model size options (tiny, base, small, medium, large)
  - Save transcriptions to text files
  - Progress tracking during transcription

## Prerequisites

```bash
# Install required packages
pip install yt-dlp
pip install torch
pip install git+https://github.com/openai/whisper.git
```

Additional requirements:
- FFmpeg (for audio processing)
- Python 3.6 or higher
- Internet connection

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/GCollab.git
cd GCollab
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Script

```bash
python yt_dlp_extract_audio_audio_to_text.py
```

### Main Menu Options

1. **Download Video**
   - Enter YouTube URL
   - Select video quality from available options
   - Video will be saved as 'downloaded_video.mp4'

2. **Extract Audio Only**
   - Enter YouTube URL
   - Choose whether to download locally
   - Audio will be saved as 'output_audio.mp3'

3. **Transcribe Audio**
   - Automatically processes extracted audio
   - Saves transcription to 'transcription.txt'

### Example Usage

```python
# Import the script
from yt_dlp_extract_audio_audio_to_text import extract_audio, transcribe_audio

# Extract audio from a YouTube video
output_audio = extract_audio("https://youtube.com/watch?v=VIDEO_ID", enable_local_download=True)

# Transcribe the audio (if needed)
transcribed_text = transcribe_audio(
    audio_path=output_audio,
    output_path="transcription.txt",
    model_size="base"
)
```

## Function Documentation

### extract_audio(video_url, enable_local_download=False)
Downloads and extracts audio from a YouTube video.
- `video_url`: YouTube video URL
- `enable_local_download`: Boolean to enable local file download

### download_video(url, selected_format)
Downloads a YouTube video in the specified quality.
- `url`: YouTube video URL
- `selected_format`: Dictionary containing format specifications

### transcribe_audio(audio_path, output_path, model_size="base")
Transcribes audio file to text using Whisper.
- `audio_path`: Path to audio file
- `output_path`: Path for saving transcription
- `model_size`: Whisper model size (tiny/base/small/medium/large)

## Error Handling

The script includes comprehensive error handling for:
- Invalid YouTube URLs
- Network connection issues
- Unavailable video formats
- File download/save errors
- Transcription failures

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for video downloading capabilities
- [OpenAI Whisper](https://github.com/openai/whisper) for audio transcription
- FFmpeg for audio processing

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---
**Note**: This tool is for personal use only. Please respect YouTube's terms of service and content creators' rights when using this tool.
