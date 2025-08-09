import whisper


def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)

    transcribed_text = result["text"]
    print(transcribed_text[:100])

    output_file_path = "transcription.txt"
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(transcribed_text)

    return transcribed_text
