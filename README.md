# Story2Audio Microservice

A microservice that converts input story text into audio using gRPC and Text-to-Speech (TTS) technology. It includes a backend service that processes the text and generates audio, and a simple Gradio frontend interface for users to interact with the system.

---

## 📌 Project Overview

This project aims to demonstrate a complete microservice system built with gRPC. The backend service accepts text and filename via gRPC, converts the text into speech using a TTS model, and saves the audio output. A Gradio frontend allows easy interaction, and Docker support ensures smooth deployment.

---

## ⚙️ Technologies Used

- Python 3.8+
- gRPC
- [Coqui TTS](https://github.com/coqui-ai/TTS)
- Gradio
- Docker & Docker Compose
- Postman (for gRPC testing)

---

## 📦 Installation Instructions

### Prerequisites

- Python 3.8+
- `pip`
- `virtualenv` (recommended)
- Docker (optional, for container deployment)

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/story2audio.git
   cd story2audio

2. **Set Up a Virtual Environment** (optional but recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies for backend** 
    pip install -r requirements.txt
     (FOllowing if in virtual env)
    python grpc_server.py         # run this  command 
    gRPC starts running on localhost:50051

    #run frontend
    python grpc_frontend.py

4. **Runnning using Docker containers**


    Running the Application:
    Start running your Docker Desktop

    Backend (gRPC Server):
    Start the gRPC Server by running the grpc_server.py file in the terminal.

    gRPC Endpoint: The backend exposes the /generate endpoint via the GenerateAudio method. It receives a text input and an optional filename. The response includes a status, a message, and the file path of the generated audio file.
  
    Run following command for backend-through docker
    docker run -it --rm -v C:\Projects\story2audio:/app -p 50051:50051 story2audio-grpc

    Frontend (Gradio Interface):
    Navigate to: http://localhost:7860

    Enter Story Text: Type a story (minimum 15–20 characters).

    Generate Audio: Optionally enter a filename or leave it blank to auto-generate one.

    Audio Output: The audio will be generated, saved as a .wav file, and the status message will be shown in the Gradio interface.

    run Frontend through Venv (python .m app.grpc_frontend)

5. **Error Handling**
    Empty Input: If the input text is empty, the system will return an error: "Text input is empty".

    Server Error: If the backend encounters an error during processing, it will return a "Server error" message with the error details.


6. **Test Cases**
    1. Enter text(>15 char) and filename with .wav extension
    2. Enter text but no filename
    3. Enter text, filename but no .wav extension
    4. Enter no text
    5. Enter small texts eg (Hello)

7.  OR **The Text-to-Speech engine uses the model tts_models/en/ljspeech/speedy-speech from the Coqui TTS library.**

8. **For Docker**
     Dockerfiles for frontend and backend already attached