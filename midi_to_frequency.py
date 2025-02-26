import input_handler

def midi_to_frequency(pitch: int):
    freq = 440 * (2**((pitch - 69) / 12))
    return freq

input = int(input('Please enter a valid midi note: '))
print(midi_to_frequency(input))
