import torch
import torchaudio
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import speech_recognition as sr

model_name = "facebook/wav2vec2-large-960h"
processor = Wav2Vec2Processor.from_pretrained(model_name)
model = Wav2Vec2ForCTC.from_pretrained(model_name)

def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something:")
        audio = recognizer.listen(source)
        
        audio_path = "recorded_audio.wav"
        with open(audio_path, "wb") as f:
            f.write(audio.get_wav_data())
    
    return audio_path

def load_audio(file_path):
    speech_array, sampling_rate = torchaudio.load(file_path)
    return speech_array.squeeze().numpy(), sampling_rate

def transcribe(audio_path):
    speech, sampling_rate = load_audio(audio_path)
    
    if sampling_rate != 16000:
        resampler = torchaudio.transforms.Resample(orig_freq=sampling_rate, new_freq=16000)
        speech = resampler(torch.tensor(speech)).numpy()
    
    input_values = processor(speech, return_tensors="pt", sampling_rate=16000).input_values
    
    with torch.no_grad():
        logits = model(input_values).logits
    
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0])
    
    return transcription
