import grpc
from app.grpc_generated import story2audio_pb2, story2audio_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = story2audio_pb2_grpc.StoryToAudioStub(channel)

    request = story2audio_pb2.StoryRequest(
        text="Once upon a time in a quiet forest, there lived a wise old owl.",
        filename="test_audio.wav"
    )

    response = stub.GenerateAudio(request)

    print(f"Status: {response.status}")
    print(f"Message: {response.message}")
    print(f"File path: {response.file_path}")

if __name__ == "__main__":
    run()
