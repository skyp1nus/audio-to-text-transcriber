# Audio Transcription Tool

This project uses the Whisper model to transcribe audio files into text. It can detect the language of the audio and provide a transcription along with the detected language.

## Features

- Transcribe audio files to text
- Detect the language of the audio
- Save transcription results to a text file

## Requirements

- Python 3.6+
- whisper library
- ffmpeg

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/audio-transcription-tool.git
   cd audio-transcription-tool
   ```

2. Install the required dependencies:
   ```
   pip install whisper
   pip install ffmpeg
   ```

## Usage

1. Place your audio file in the project directory or specify the full path to your audio file.

2. Modify the `audio_file` variable in the script to point to your audio file:
   ```python
   audio_file = "Audio/*.mp3"
   ```

3. Run the script:
   ```
   python __main__.py
   ```

4. The transcription will be saved in `output.txt` by default.

## Function Parameters

The `transcribe_audio` function accepts the following parameters:

- `audio_path` (str): Path to the audio file
- `model_size` (str, optional): Size of the Whisper model to use. Default is "base"
- `output_file` (str, optional): Name of the output file. Default is "output.txt"

## Output

The script will create a text file containing:
- The detected language
- The full transcription of the audio

## Note

This script uses the Whisper model, which requires significant computational resources. Depending on the length of your audio file and the model size chosen, transcription may take some time.

## License

MIT

## Contributing

[Add your contributing guidelines here]

## Contact

[Your contact information or how to reach out for questions/issues]