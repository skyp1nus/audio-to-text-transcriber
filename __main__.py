import whisper

def transcribe_audio(audio_path, model_size="base", output_file="output.txt"):
    # Завантажуємо модель Whisper
    model = whisper.load_model(model_size)
    
    # Транскрибування аудіо
    result = model.transcribe(audio_path)
    
    # Отримуємо визначену мову та ймовірність
    language = result.get("language", "unknown")
    
    # Отримуємо текст транскрипції
    transcription = result.get("text", "")
    
    # Формуємо текст для запису у файл
    output_text = (
        f"Detected language: {language}\n\n"
        f"Transcription:\n{transcription}"
    )
    
    try:
        # Записуємо текст у файл
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(output_text)
        print(f"Transcription successfully written to file '{output_file}'.")
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    audio_file = "Audio/audio.mp3"  # Замініть на шлях до вашого аудіофайлу
    transcription = transcribe_audio(audio_file)
