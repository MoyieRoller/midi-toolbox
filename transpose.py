"""Transponierung von Noten oder Akkorden"""

import input_handler

pitches = []
max_pitch_length = 0 

def transpose(pitch: int) -> int:
    try:
        new_pitch = pitch + transpose_interval
        if new_pitch not in range(0, 128):
            raise ValueError()
    except ValueError:
        print('ERROR: Transposing this midi note falls out of the midi range.')
    else:
        return new_pitch
    
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

def get_transpose_interval() -> int:
    while True:
        userInput = input('Please enter a positive or negative amount, to transpose your entered notes: ')
        try:
            userInput = int(userInput)
            if userInput not in range(-127, 128):
                raise ValueError()
        except ValueError:
            print('ERROR: Not a correct number for transposing.')
        else:
            return userInput
            break

pitches = get_valid_inputs()
transpose_interval = get_transpose_interval()

for pitch in pitches:
    if type(pitch) == list: # Akkord
        chord = []
        for note in pitch:
            new_pitch = transpose(note)
            chord.append(new_pitch)
            stringified_chord = str(chord).replace("'", "")
        print(f'{str(pitch):>{max_pitch_length}} = {stringified_chord}')
    else: # einzelne Note
        new_pitch = transpose(pitch)
        print(f'{pitch:>{max_pitch_length}} = {new_pitch}')