import gradio as gr
import whisper
import os

model = whisper.load_model("base")

def transcribe_audio(audio_file):
    # Check file size (e.g., 25MB limit)
    if os.path.getsize(audio_file.name) > 25 * 1024 * 1024:
        return "Error: File size exceeds 25MB limit.", None

    result = model.transcribe(audio_file.name)
    output_filename = os.path.splitext(os.path.basename(audio_file.name))[0] + ".txt"
   
    with open(output_filename, "w") as text_file:
        text_file.write(result["text"])
   
    return result["text"], output_filename

iface = gr.Interface(
    fn=transcribe_audio,
    inputs=gr.File(label="Upload Audio File (Max 25MB)"),
    outputs=[
        gr.Textbox(label="Transcription"),
        gr.File(label="Download Transcript")
    ],
    title="Free Transcript Maker",
    description="Upload an audio file (WAV, MP3, etc.) up to 25MB to get its transcription. The transcript will be displayed and available for download. Please use responsibly."
)

iface.launch(share=True)