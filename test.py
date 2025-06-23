import requests

text = "Hi, my name is Leela. I love to read books and play with my friends."
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
    print("❌ Request failed:", response.status_code, response.text)
