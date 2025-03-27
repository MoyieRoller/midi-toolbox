"""Bestimmung der Oktave einer MIDI-Note"""

import input_handler

pitches = []
octaves = ('not defined', '0', '1', '2', '3', '4', '5', '6', '7', '8', 'not defined')
max_pitch_length = 0

def get_octave(pitch: int) -> str:
    octave = octaves[int(pitch / 12)]
    return octave

def get_valid_inputs() -> list:
    while True:
        pitch = input_handler.input_pitch("Please enter a valid midi note or chord.\nPress [enter] to start the calculation. Type 'exit' to stop the program: ")
        if not input_handler.break_loop:
            pitches.append(pitch)
        else:
            break
    return pitches

pitches = get_valid_inputs()

for pitch in pitches:
    if type(pitch) == list: # Akkord
        chord = []
        for note in pitch:
            octave = get_octave(note)
            chord.append(octave)
            stringified_chord = str(chord).replace("'", "")
        print(f'The octaves for {str(pitch)} are {stringified_chord}.')
    else: # einzelne Note
        octave = get_octave(pitch)
        print(f'The octave for {pitch} is {octave}.')