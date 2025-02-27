import input_handler

pitches = []
frequencies = []

def midi_to_frequency(pitch: int):
    freq = 440 * (2**((pitch - 69) / 12))
    return freq

def get_valid_inputs():
    while True:
        pitch = input_handler.input_pitch('Please enter a valid midi note or chord, press enter to stop the input: ')
        if not input_handler.break_loop:
            pitches.append(pitch)
        else:
            break
    return pitches

pitches = get_valid_inputs()

def round_frequency(freq: float) -> str:
    if str(freq).find('.') == 3:
        return '%.2f'%(freq)
    elif str(freq).find('.') == 2:
        return '%.3f'%(freq)
    elif str(freq).find('.') == 4:
        return '%.1f'%(freq)
    elif str(freq).find('.') == 5:
        return '%.0f'%(freq)
    else:
        return '%.4f'%(freq)

for pitch in pitches:
    if type(pitch) == list:
        chord = []
        for note in pitch:
            frequency = midi_to_frequency(note)
            frequency = round_frequency(frequency)
            chord.append(f'{frequency} Hz')
            stringified_chord = str(chord).replace("'", "")
        print(f'{pitch} = {stringified_chord}')
    else:
        frequency = midi_to_frequency(pitch)
        frequency = round_frequency(frequency)
        print(f'{pitch} = {frequency} Hz')