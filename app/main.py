



##coqui TTS
from fastapi import FastAPI
from app.tts_engine import TextToSpeechEngine
from app.schemas import StoryRequest

app = FastAPI()

#Load the model ONCE here when app starts
tts_engine = TextToSpeechEngine()

@app.get("/")
def read_root():
    return {"message": "API is running!"}

@app.post("/generate-audio/")
async def generate_audio(story_request: StoryRequest):
    try:
        output_file = tts_engine.text_to_audio(
            story_request.text,
            story_request.filename
        )
        return {"message": "Audio generated successfully!", "file_path": output_file}
    except Exception as e:
        return {"error": f"Failed to generate audio: {str(e)}"}

