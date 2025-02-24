import math

def frequency_to_midi(freq: float):
    pitch = 12 * math.log2(freq / 440) + 69
    return int(pitch)

input = int(input('Please enter a valid frequency: '))
print(frequency_to_midi(input))