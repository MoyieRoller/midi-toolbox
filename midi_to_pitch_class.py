"""Umwandlung von Midi-Noten in Tonhöhenklassen"""

import input_handler

pitches = []
pitch_classes = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
max_pitch_length = 0

def midi_to_pitch_class(pitch: int) -> str:
    pitch_class = pitch_classes[pitch % 12]
    return pitch_class

def get_valid_inputs() -> list:
    while True:
        pitch = input_handler.input_pitch("Please enter a valid midi note or chord.\nPress [enter] to start the calculation. Type 'exit' to stop the program: ")
        global max_pitch_length
        if len(str(pitch)) > max_pitch_length and pitch != None:
            max_pitch_length = len(str(pitch))
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
            pitch_class = midi_to_pitch_class(note)
            chord.append(pitch_class)
            stringified_chord = str(chord).replace("'", "")
        print(f'{str(pitch):>{max_pitch_length}} = {stringified_chord}')
    else: # einzelne Note
        pitch_class = midi_to_pitch_class(pitch)
        print(f'{pitch:>{max_pitch_length}} = {pitch_class}')