# import gradio as gr
# from app.tts_engine import TextToSpeechEngine

# # Initialize TTS engine
# tts_engine = TextToSpeechEngine()

# # Function to generate audio from text
# def generate_audio(text):
#     output_file = tts_engine.text_to_audio(text)
#     return output_file

# # Gradio interface
# interface = gr.Interface(
#     fn=generate_audio,  # function to call
#     inputs="text",  # input type
#     outputs="audio",  # output type (audio file)
#     live=True  # to process as you type
# )

# # Launch the interface
# interface.launch()





# import gradio as gr
# import requests

# API_URL = "http://localhost:8000/generate-audio/"

# def generate_audio(text):
#     try:
#         response = requests.post(
#             API_URL,
#             json={"text": text},
#             headers={"Content-Type": "application/json"}
#         )
#         if response.status_code == 200:
#             return response.json()["file_path"]  # Path to generated audio
#         else:
#             return f"Error: {response.json()['detail']}"
#     except Exception as e:
#         return f"Connection error: {str(e)}"

# interface = gr.Interface(
#     fn=generate_audio,
#     inputs="text",
#     outputs="audio",
#     live=True,
#     title="Story2Audio - Connected to Backend"
# )

# interface.launch()


### STREAMLIT

# import streamlit as st
# import requests
# import os

# # Configuration
# BACKEND_URL = "http://localhost:8000/generate-audio/"
# AUDIO_FOLDER = "audio_output"

# st.title("📖 Story to Audio Converter")
# st.caption("Powered by FastAPI backend")

# # Create audio folder if not exists
# os.makedirs(AUDIO_FOLDER, exist_ok=True)

# def generate_audio(text):
#     """Call backend API to generate audio"""
#     try:
#         response = requests.post(
#             BACKEND_URL,
#             json={"text": text},
#             headers={"Content-Type": "application/json"}
#         )
#         if response.status_code == 200:
#             return response.json()["file_path"]
#         else:
#             st.error(f"Backend error: {response.json().get('detail', 'Unknown error')}")
#             return None
#     except requests.exceptions.ConnectionError:
#         st.error("⚠️ Backend server not running! Start it with:\n\n`uvicorn app.main:app --reload`")
#         return None

# # UI Components
# text_input = st.text_area("Enter your story:", height=200)
# generate_btn = st.button("Generate Audio")

# if generate_btn and text_input.strip():
#     with st.spinner("Generating audio..."):
#         audio_path = generate_audio(text_input)
        
#         if audio_path:
#             st.success("🎧 Audio generated!")
#             st.audio(os.path.join(AUDIO_FOLDER, "output_audio.mp3"))  # Directly use known path
            
#             # Display API response details
#             with st.expander("Backend Response Details"):
#                 st.json({
#                     "audio_path": audio_path,
#                     "full_url": f"http://localhost:8000/{audio_path}"
#                 })
# elif generate_btn:
#     st.warning("Please enter some text first!")



##almost finaliyed with pyttsx3

# import gradio as gr
# import requests
# from datetime import datetime  # IMPORTANT: must be imported

# # Function to call the backend API
# def generate_audio(text, filename):
#     url = "http://127.0.0.1:8000/generate-audio/"

#     if not filename:
#         filename = f"story_audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp3"
#     else:
#         filename = filename if filename.endswith('.mp3') else filename + '.mp3'

#     payload = {"text": text, "filename": filename}
#     try:
#         response = requests.post(url, json=payload)
#         if response.status_code == 200:
#             data = response.json()
#             if "message" in data:
#                 return data["message"] + f" (Saved as: {filename})"
#             elif "error" in data:
#                 return f"Error from backend: {data['error']}"
#             else:
#                 return "Unexpected response format."
#         else:
#             return f"Error: {response.text}"
#     except Exception as e:
#         return f"Exception occurred: {str(e)}"

# # Gradio interface
# iface = gr.Interface(
#     fn=generate_audio,
#     inputs=[
#         gr.Textbox(lines=5, label="Enter Text to Generate Audio"),
#         gr.Textbox(label="Enter Filename (without .mp3)")
#     ],
#     outputs="text",
#     title="Story2Audio Generator",
#     description="Enter your story and a filename, and get the generated audio!"
# )

# # Launch Gradio app
# iface.launch()



### TTS
import gradio as gr
import requests
from datetime import datetime  # IMPORTANT: must be imported

# Function to call the backend API
def generate_audio(text, filename):
    url = "http://127.0.0.1:8000/generate-audio/"

    if not filename:
        filename = f"story_audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.wav"  # Change to .wav extension
    else:
        filename = filename if filename.endswith('.wav') else filename + '.wav'  # Change to .wav extension

    payload = {"text": text, "filename": filename}
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            if "message" in data:
                return data["message"] + f" (Saved as: {filename})"
            elif "error" in data:
                return f"Error from backend: {data['error']}"
            else:
                return "Unexpected response format."
        else:
            return f"Error: {response.text}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

# Gradio interface
iface = gr.Interface(
    fn=generate_audio,
    inputs=[
        gr.Textbox(lines=5, label="Enter Text to Generate Audio"),
        gr.Textbox(label="Enter Filename (without .wav)")  # Adjusted to accept .wav filenames
    ],
    outputs="text",
    title="Story2Audio Generator",
    description="Enter your story and a filename, and get the generated audio!"
)

# Launch Gradio app
iface.launch()
