

# ##works perfect with grpc too
# import gradio as gr
# import grpc
# from datetime import datetime
# from app.grpc_generated import story2audio_pb2, story2audio_pb2_grpc

# def generate_audio(text, filename):
#     if not filename:
#         filename = f"story_audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.wav"
#     else:
#         filename = filename if filename.endswith('.wav') else filename + '.wav'

#     try:
#         # Connect to gRPC server
#         channel = grpc.insecure_channel("localhost:50051")
#         stub = story2audio_pb2_grpc.StoryToAudioStub(channel)

#         response = stub.GenerateAudio(
#             story2audio_pb2.AudioRequest(text=text, filename=filename)
#         )

#         if response.status == "SUCCESS":
#             return f"{response.message} (Saved as: {response.file_path})"
#         else:
#             return f"Failure: {response.message}"

#     except grpc.RpcError as e:
#         return f"RPC failed: {e.details()} (Code: {e.code()})"
#     except Exception as e:
#         return f"Unexpected error: {str(e)}"

# # Launch Gradio UI
# iface = gr.Interface(
#     fn=generate_audio,
#     inputs=[
#         gr.Textbox(lines=5, label="Enter Text (make sure to use atleast 15-20 characters)"),
#         gr.Textbox(label="Filename (optional)")
#     ],
#     outputs="text",
#     title="Story2Audio (gRPC)",
#     description="Generate audio from story text using gRPC microservice."
# )

# iface.launch()



# # #prettier version of code above
# import gradio as gr
# import grpc
# from datetime import datetime
# from app.grpc_generated import story2audio_pb2, story2audio_pb2_grpc

# def generate_audio(text, filename):
#     if not filename:
#         filename = f"story_audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.wav"
#     else:
#         filename = filename if filename.endswith('.wav') else filename + '.wav'

#     try:
#         channel = grpc.insecure_channel("localhost:50051")
#         stub = story2audio_pb2_grpc.StoryToAudioStub(channel)

#         response = stub.GenerateAudio(
#             story2audio_pb2.AudioRequest(text=text, filename=filename)
#         )

#         if response.status == "SUCCESS":
#             return f"{response.message} (Saved as: {response.file_path})"
#         else:
#             return f"Failure: {response.message}"

#     except grpc.RpcError as e:
#         return f"RPC failed: {e.details()} (Code: {e.code()})"
#     except Exception as e:
#         return f"Unexpected error: {str(e)}"

# # Prettier UI using Blocks
# with gr.Blocks(theme=gr.themes.Base(primary_hue="blue", secondary_hue="gray")) as iface:
#     gr.Markdown(
#         """
#         <div style="text-align: center; padding: 10px;">
#             <h1 style="color: #1f2937;">🎙️ <u>Story2Audio</u></h1>
#             <p style="font-size: 16px; color: #4b5563;">
#                 Enter your story text and optionally a filename.<br>
#                 Minimum input: <b>15–20 characters</b>.
#             </p>
#         </div>
#         """
#     )

#     with gr.Column():
#         text_input = gr.Textbox(
#             label="Enter Text", lines=5, placeholder="Type your story here..."
#         )
#         filename_input = gr.Textbox(
#             label="Filename (optional)", placeholder="e.g., my_story.wav"
#         )
#         generate_button = gr.Button("🔊 Generate Audio", variant="primary")
#         output_text = gr.Textbox(label="Status", interactive=False)

#     generate_button.click(
#         fn=generate_audio,
#         inputs=[text_input, filename_input],
#         outputs=output_text
#     )

# iface.launch()




#frontend with audio displayed
import gradio as gr
import grpc
import os
from datetime import datetime
from app.grpc_generated import story2audio_pb2, story2audio_pb2_grpc

OUTPUT_DIR = "output"

def generate_audio(text, filename):
    if not filename:
        filename = f"story_audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.wav"
    else:
        filename = filename if filename.endswith(".wav") else filename + ".wav"

    try:
        channel = grpc.insecure_channel("localhost:50051")
        stub = story2audio_pb2_grpc.StoryToAudioStub(channel)

        response = stub.GenerateAudio(
            story2audio_pb2.AudioRequest(text=text, filename=filename)
        )

        if response.status == "SUCCESS":
            audio_path = os.path.join(OUTPUT_DIR, filename)
            if os.path.exists(audio_path):
                return f"{response.message} (Saved as: {response.file_path})", audio_path
            else:
                return f"Audio not found at expected location: {audio_path}", None
        else:
            return f"Failure: {response.message}", None

    except grpc.RpcError as e:
        return f"RPC failed: {e.details()} (Code: {e.code()})", None
    except Exception as e:
        return f"Unexpected error: {str(e)}", None


# Gradio UI with audio playback
with gr.Blocks(theme=gr.themes.Base(primary_hue="blue", secondary_hue="gray")) as iface:
    gr.Markdown("""
        <div style="text-align: center; padding: 10px;">
            <h1 style="color: #1f2937;">🎙️ <u>Story2Audio</u></h1>
            <p style="font-size: 16px; color: #4b5563;">
                Enter your story text and optionally a filename.<br>
                Minimum input: <b>15–20 characters</b>.
            </p>
        </div>
    """)

    with gr.Column():
        text_input = gr.Textbox(label="Enter Text", lines=5, placeholder="Type your story here...")
        filename_input = gr.Textbox(label="Filename (optional)", placeholder="e.g., my_story.wav")
        generate_button = gr.Button("🔊 Generate Audio", variant="primary")
        status_output = gr.Textbox(label="Status", interactive=False)
        audio_output = gr.Audio(label="Generated Audio", type="filepath")

    generate_button.click(
        fn=generate_audio,
        inputs=[text_input, filename_input],
        outputs=[status_output, audio_output]
    )

iface.launch()
