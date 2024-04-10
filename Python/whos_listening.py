import pyaudio

def print_audio_devices():
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        print(f"Index: {i}, Name: {info['name']}")

print_audio_devices()
