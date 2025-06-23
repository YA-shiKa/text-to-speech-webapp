# 🎙️ Responsive Text-to-Speech (TTS) Web App

## 🌐 Overview

This web application takes user input text in **English, Hindi**, or **Hinglish** and generates natural-sounding speech using an open-source TTS model.  
It supports **Indian-accented English and Hindi**, and streams audio directly from the Python backend in real-time.

---

## 🖼️ UI Preview
A glimpse of the responsive TTS application interface.
![image](https://github.com/user-attachments/assets/6eafb3df-1b72-4d93-b337-00bd3dedf15c)

🎥 Demo Videos

🔊 Hindi TTS Demo

[🗣️ Hindi Demo](https://github.com/user-attachments/assets/4d98626c-8dd0-454e-a3d1-4391e29c86f9)

🔊 English TTS Demo

[🗣️ English Demo](https://github.com/user-attachments/assets/c90e73f6-a0ab-433d-8cb0-92f8a4af07d0)

🔊 Hinglish TTS Demo

[🗣️ Hinglish Demo](https://github.com/user-attachments/assets/144a3b6c-916c-4cdd-a6a2-ed21c3a1b6cd)

---

## ⚙️ Setup Instructions

### 🧱 Clone and Install
```bash
git clone https://github.com/YA-shiKa/text-to-speech-webapp.git
cd INDIC\ TTS
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 🚀 Run the App
```bash
uvicorn app:app --reload
```
Then open your browser and visit: http://127.0.0.1:8000

---

## 🎤 API Usage
➤ Endpoint:
```bash
POST /speak
```
➤ JSON Request Body:
```bash
{
  "text": "Namaste, how are you?",
  "description": "Leela speaks in a high-pitched, fast-paced, and cheerful tone, full of energy and happiness. The recording is very high quality with no background noise."
}
```
➤ Response:

audio/mpeg stream (playable or downloadable)

---

## ✨ Example Integration with OpenAI SDK
You can use the hosted /speak endpoint with openai.tts_to_file()-style code:

```bash
import requests

text = "Hello! This is a simple TTS test with Indian English."
voice_url = "http://127.0.0.1:8000/speak"

response = requests.post(
    voice_url,
    json={
        "text": text,
        "description": "Leela speaks in a high-pitched, fast-paced, and cheerful tone, full of energy and happiness. The recording is very high quality with no background noise."
    },
    stream=True
)

if response.status_code == 200:
    with open("output.wav", "wb") as f:
        for chunk in response.iter_content(chunk_size=4096):
            f.write(chunk)
    print("✅ Audio saved to output.wav")
else:
    print("❌ Request failed:", response.status_code)
```

---

## 🌟 Features
✅ Open-source TTS model: Meta's Indic Parler-TTS (7B)

✅ Supports Indian-accented English, Hindi, and Hinglish

✅ Streaming audio from backend (FastAPI StreamingResponse)

✅ Accepts speaker descriptions (e.g., pitch, speed, tone)

✅ Fully working frontend UI

✅ Compatible with OpenAI’s tts_to_file() style integration

---

## 📌 Note
The model.safetensors file is not included in this repo to reduce size.
Please download it manually and place it in:

```bash
Edit
models/indic-parler-tts/
```
