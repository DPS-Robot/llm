import torchaudio
from speechbrain.inference.TTS import Tacotron2
from speechbrain.inference.vocoders import HIFIGAN
import pygame

tacotron2 = Tacotron2.from_hparams(source="speechbrain/tts-tacotron2-ljspeech", savedir="tmpdir_tts")
hifi_gan = HIFIGAN.from_hparams(source="speechbrain/tts-hifigan-ljspeech", savedir="tmpdir_vocoder")


def gen(p):
    mel_output, mel_length, alignment = tacotron2.encode_text(p)

    waveforms = hifi_gan.decode_batch(mel_output)

    torchaudio.save('example_TTS.wav',waveforms.squeeze(1), 22050)
def playAudio():
    pygame.mixer.init()
    pygame.mixer.music.load("example_TTS.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
