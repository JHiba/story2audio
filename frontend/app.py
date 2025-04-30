

# ### TTS
# import gradio as gr
# import requests
# from datetime import datetime  # IMPORTANT: must be imported

# # Function to call the backend API
# def generate_audio(text, filename):
#     url = "http://127.0.0.1:8000/generate-audio/"

#     if not filename:
#         filename = f"story_audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.wav"  # Change to .wav extension
#     else:
#         filename = filename if filename.endswith('.wav') else filename + '.wav'  # Change to .wav extension

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
#         gr.Textbox(label="Enter Filename (without .wav)")  # Adjusted to accept .wav filenames
#     ],
#     outputs="text",
#     title="Story2Audio Generator",
#     description="Enter your story and a filename, and get the generated audio!"
# )

# # Launch Gradio app
# iface.launch()

##using grpc
import gradio as gr
import grpc
from datetime import datetime
from app.grpc_generated import story2audio_pb2, story2audio_pb2_grpc

def generate_audio(text, filename):
    if not filename:
        filename = f"story_audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.wav"
    else:
        filename = filename if filename.endswith('.wav') else filename + '.wav'

    try:
        # Connect to gRPC server
        channel = grpc.insecure_channel("localhost:50051")
        stub = story2audio_pb2_grpc.StoryToAudioStub(channel)

        response = stub.GenerateAudio(
            story2audio_pb2.AudioRequest(text=text, filename=filename)
        )

        if response.status == "SUCCESS":
            return f"{response.message} (Saved as: {response.file_path})"
        else:
            return f"Failure: {response.message}"

    except grpc.RpcError as e:
        return f"RPC failed: {e.details()} (Code: {e.code()})"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

# Launch Gradio UI
iface = gr.Interface(
    fn=generate_audio,
    inputs=[
        gr.Textbox(lines=5, label="Enter Text"),
        gr.Textbox(label="Filename (optional)")
    ],
    outputs="text",
    title="Story2Audio (gRPC)",
    description="Generate audio from story text using gRPC microservice."
)

iface.launch()
