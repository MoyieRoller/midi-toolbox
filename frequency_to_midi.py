"""Umrechnung von Hertz in MIDI-Noten"""

import math
import sys
import input_handler
from typing import Union

frequencies = []
break_loop = False
max_freq_length = 0.0

def input_frequency(message: str) -> Union[int, list]:
    while True:
        userInput = input(message)

        # Eingabe beenden
        if userInput.lower() == '':
            global break_loop
            break_loop = True
            break
        
        # Programm beenden
        if userInput == 'exit':
            print('Exiting midi-toolbox...')
            sys.exit(0)

        if userInput.startswith('[') and userInput.endswith(']'): # Akkord
            chord = chord_validation(userInput)
            if chord != None:
                return chord
        elif userInput.startswith('[') and not userInput.endswith(']'): # unvollständiger Akkord
            print('ERROR: Not a chord in the correct format [frequency1, frequency2,...]!')
            continue
        else:
            try:
                userInput = float(userInput)
                if userInput < 8.0 or userInput > 12544.0:
                    raise ValueError()
            except ValueError:
                print('ERROR: Not a valid frequency, only numbers between 8 Hz and 12544 Hz accepted!')
            else:
                return userInput

def chord_validation(userInput: str) -> list:
    chord = []
    try:
        stripped_input = userInput.strip('[]')
        chord_list = stripped_input.split(',')

        for single_frequency_string in chord_list:
            single_frequency = float(single_frequency_string)
            if single_frequency < 8.0 or single_frequency > 12544.0:
                raise ValueError
            else:
                chord.append(single_frequency)
    except ValueError:
        print('ERROR: Not a valid frequency within the chord, only numbers between 8 Hz and 12544 Hz seperated by commas accepted!')
    else:
        return chord

def get_valid_inputs() -> list:
    while True:
        frequency = input_frequency("Please enter a valid frequency or chord.\nPress [enter] to start the calculation. Type 'exit' to stop the program: ")
        global max_freq_length
        if len(str(frequency)) > max_freq_length and frequency != None:
            max_freq_length = len(str(frequency))
        if not break_loop:
            frequencies.append(frequency)
        else:
            break
    return frequencies

def frequency_to_midi(freq: float) -> int:
    pitch = 12 * math.log2(freq / 440) + 69
    return round(pitch)

def format_frequencies(frequencies: list) -> list:
    new_frequencies = []
    for frequency in frequencies:
        frequency_with_unit = str(frequency) + ' Hz'
        new_frequencies.append(frequency_with_unit)
    new_frequencies_stringified = str(new_frequencies).replace("'", "")
    return(new_frequencies_stringified)
        
frequencies = get_valid_inputs()

# maximale Wortlänge vor dem "=" anpassen, für output-Formatierung
for freq in frequencies:
    if type(freq) == list:
        frequencies_string = format_frequencies(freq)
        if len(frequencies_string) > max_freq_length:
            max_freq_length = len(frequencies_string)

for freq in frequencies:
    if type(freq) == list: # Akkord
        chord = []
        for note in freq:
            pitch = frequency_to_midi(note)
            chord.append(str(pitch))
            stringified_chord = str(chord).replace("'", "")
        print(f'{format_frequencies(freq):>{max_freq_length}} = {stringified_chord}')
    else: # einzelne Note
        pitch = frequency_to_midi(freq)
        print(f'{freq:>{max_freq_length - 3}} Hz = {pitch}')