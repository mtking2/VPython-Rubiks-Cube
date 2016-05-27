import pyaudio
import wave


def play_turn(sound):
    # define stream chunk
    chunk = 1024

    # open a wav format music
    switcher = {1: wave.open(r"resources/RTurn1.wav","rb"),
                2: wave.open(r"resources/RTurn2.wav","rb"),
                3: wave.open(r"resources/RTurn3.wav","rb")}

    f = switcher.get(sound)
    # f = wave.open(r"resources/RTurn1.wav","rb")
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    # read data
    data = f.readframes(chunk)

    # paly stream
    while data != '':
        stream.write(data)
        data = f.readframes(chunk)

    # stop stream
    stream.stop_stream()
    stream.close()

    # close PyAudio
    p.terminate()