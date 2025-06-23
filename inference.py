import torch
from parler_tts import ParlerTTSForConditionalGeneration
from transformers import AutoTokenizer
import soundfile as sf

device = torch.device("cpu")

model = ParlerTTSForConditionalGeneration.from_pretrained(
    r"C:\Users\Maligi Yashika\Desktop\INDIC TTS\models\indic-parler-tts",
    local_files_only=True
)
tokenizer = AutoTokenizer.from_pretrained(
    r"C:\Users\Maligi Yashika\Desktop\INDIC TTS\models\indic-parler-tts",
    local_files_only=True
)

desc_tokenizer = AutoTokenizer.from_pretrained(model.config.text_encoder._name_or_path)

def synthesize(text, description="A neutral Indian-accented female voice"):
    desc = desc_tokenizer(description, return_tensors="pt").to(device)
    prompt = tokenizer(text, return_tensors="pt").to(device)
    with torch.no_grad():
        gen = model.generate(
            input_ids=desc.input_ids,
            attention_mask=desc.attention_mask,
            prompt_input_ids=prompt.input_ids,
            prompt_attention_mask=prompt.attention_mask
        )
    audio = gen.cpu().numpy().squeeze()
    return audio, model.config.sampling_rate
