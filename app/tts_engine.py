# # # import pyttsx3
# # # ## handles text to speech
# # # class TextToSpeechEngine:
# # #     def __init__(self):
# # #         self.engine = pyttsx3.init()
# # #         self.engine.setProperty('rate', 150)  # Speed of speech
# # #         self.engine.setProperty('volume', 1.0)  # Volume 0.0 to 1.0

# # #     def text_to_audio(self, text, output_file="output_audio.mp3"):
# # #         self.engine.save_to_file(text, output_file)
# # #         self.engine.runAndWait()
# # #         return output_file



# # import pyttsx3

# # class TextToSpeechEngine:
# #     def __init__(self):
# #         self.engine = pyttsx3.init()
# #         self.engine.setProperty('rate', 150)  # Speed of speech
# #         self.engine.setProperty('volume', 1.0)  # Volume 0.0 to 1.0

# #         # Set female voice if available
# #         voices = self.engine.getProperty('voices')
# #         for voice in voices:
# #             if "female" in voice.name.lower() or "zira" in voice.name.lower():
# #                 self.engine.setProperty('voice', voice.id)
# #                 break
# #         # If no female voice found, it will use default

# #     def text_to_audio(self, text, output_file="output_audio.mp3"):
# #         self.engine.save_to_file(text, output_file)
# #         self.engine.runAndWait()
# #         return output_file


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




# with coqui TTS
from TTS.api import TTS
from datetime import datetime

class TextToSpeechEngine:
    def __init__(self):
        # Load a lightweight and faster model
        self.tts = TTS(
            model_name="tts_models/en/ljspeech/speedy-speech",  # Faster model
            gpu=False,  # CPU only
            progress_bar=False
        )

    def text_to_audio(self, text, output_file=None):
        if not output_file:
            output_file = f"story_audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.wav"
        else:
            if not output_file.endswith('.wav'):
                output_file += '.wav'

        self.tts.tts_to_file(text=text, file_path=output_file)
        return output_file
