

# ##works good almost finalized pyttsx3
# import pyttsx3
# from datetime import datetime

# class TextToSpeechEngine:
#     def __init__(self):
#         self.engine = pyttsx3.init()
#         self.engine.setProperty('rate', 150)  # Speed
#         self.engine.setProperty('volume', 1.0)  # Volume

#         # Try to set female voice
#         voices = self.engine.getProperty('voices')
#         for voice in voices:
#             if "female" in voice.name.lower() or "zira" in voice.name.lower():
#                 self.engine.setProperty('voice', voice.id)
#                 break

#     def text_to_audio(self, text, output_file=None):
#         if not output_file:
#             # Generate a random unique name if not provided
#             output_file = f"story_audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp3"
#         else:
#             if not output_file.endswith('.mp3'):
#                 output_file += '.mp3'

#         self.engine.save_to_file(text, output_file)
#         self.engine.runAndWait()
#         return output_file



# ##perfect finalized with grpc  finalizeddd
# # with coqui TTS
# from TTS.api import TTS
# from datetime import datetime

# class TextToSpeechEngine:
#     def __init__(self):
#         # Load a lightweight and faster model
#         self.tts = TTS(
#             model_name="tts_models/en/ljspeech/speedy-speech",  # Faster model
#             gpu=False,  # CPU only
#             progress_bar=False
#         )

#     def text_to_audio(self, text, output_file=None):
#         if not output_file:
#             output_file = f"story_audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.wav"
#         else:
#             if not output_file.endswith('.wav'):
#                 output_file += '.wav'

#         self.tts.tts_to_file(text=text, file_path=output_file)
#         return output_file


##for  dockerr - to save audio to machine
import os
from TTS.api import TTS
from datetime import datetime

class TextToSpeechEngine:
    def __init__(self):
        self.tts = TTS(
            model_name="tts_models/en/ljspeech/speedy-speech",
            #model_name="tts_models/en/ljspeech/fast_pitch",
            gpu=False,
            progress_bar=False
        )
        self.output_dir = "/app/output"  # This matches your Docker container's /app volume
        os.makedirs(self.output_dir, exist_ok=True)

    def text_to_audio(self, text, output_file=None):
        if not output_file:
            output_file = f"story_audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.wav"
        else:
            if not output_file.endswith('.wav'):
                output_file += '.wav'

        full_path = os.path.join(self.output_dir, output_file)
        self.tts.tts_to_file(text=text, file_path=full_path)
        return full_path
