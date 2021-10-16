import datetime
import os
from pydub import AudioSegment

_DI_SOUND = AudioSegment.from_file("static/sounds/di_sound.wav", format="wav")
_DAH_SOUND = AudioSegment.from_file("static/sounds/dah_sound.wav", format="wav")

_PAUSE_SOUND = AudioSegment.silent(len(_DI_SOUND))


def make_audio(text):
    filename = datetime.datetime.now().strftime("%y%m%d%H%M%S%f")
    output_sound = AudioSegment.silent(duration=0)

    for sign in text:
        if sign == '.':
            output_sound += _DI_SOUND + _PAUSE_SOUND
        elif sign == '-':
            output_sound += _DAH_SOUND + _PAUSE_SOUND
        elif sign == ' ' or sign == '/':
            output_sound += _PAUSE_SOUND + _PAUSE_SOUND

    output_sound.export(os.path.join(f"static/tmp/{filename}.mp3"), format="mp3")

    return f"tmp/{filename}.mp3"
