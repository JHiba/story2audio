import grpc
from concurrent import futures
from app.tts_engine import TextToSpeechEngine
from app.grpc_generated import story2audio_pb2, story2audio_pb2_grpc

class StoryToAudioServicer(story2audio_pb2_grpc.StoryToAudioServicer):
    def __init__(self):
        self.tts_engine = TextToSpeechEngine()
    #/generate endpoint is represented by the GenerateAudio method
    def GenerateAudio(self, request, context):
        try:
            # Validate input
            if not request.text.strip():
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)##error handling
                context.set_details("Text input is empty.")
                return story2audio_pb2.AudioResponse(
                    status="FAILURE",
                    message="Text input was empty.",
                    file_path=""
                )

            output_file = self.tts_engine.text_to_audio(request.text, request.filename)
            #JSON-like responses
            return story2audio_pb2.AudioResponse(
                status="SUCCESS",
                message="Audio generated successfully.",
                file_path=output_file
            )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return story2audio_pb2.AudioResponse(
                status="FAILURE",
                message=f"Server error: {str(e)}",
                file_path=""
            )

def serve():                              ##asynchronus handling to handle concurrent requests
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) 
    story2audio_pb2_grpc.add_StoryToAudioServicer_to_server(StoryToAudioServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC Server started on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()


