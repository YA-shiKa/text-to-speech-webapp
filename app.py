from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import io, soundfile as sf
from inference import synthesize

app = FastAPI()

@app.post("/speak")
async def speak(req: Request):
    data = await req.json()
    text = data.get("text", "")
    desc = data.get("description", "A neutral Indian-accented female voice")
    audio, sr = synthesize(text, desc)
    buf = io.BytesIO()
    sf.write(buf, audio, sr, format="WAV")
    buf.seek(0)
    return StreamingResponse(buf, media_type="audio/wav")

@app.get("/")
async def home():
    return StreamingResponse(open("templates/index.html", "rb"), media_type="text/html")

if __name__ == "__main__":
    import uvicorn; uvicorn.run(app, host="0.0.0.0", port=8000)
