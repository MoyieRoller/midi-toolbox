"""Intervall zwischen zwei Noten herausfinden"""

import input_handler
import sys
from typing import Union

pitches = []
counter = 0
enough_input_to_calculate = False
only_midi_notes = False
break_loop = False
pitch_classes = ('r1', 'k2', 'g2', 'k3', 'g3', 'r4', 'ü4', 'r5', 'k6', 'g6', 'k7', 'g7', 'r8')

def get_interval(pitch1: int, pitch2: int) -> str:
    interval_as_number = abs(pitch2 - pitch1)
    try:
        interval = pitch_classes[interval_as_number]
        if interval_as_number > len(pitch_classes):
            raise IndexError()
    except IndexError:
        print('ERROR: Intervals only defined within one ocatve.')
    else:
        return interval

def input_pitch(message: str) -> Union[int, list]:
    """ User-Eingabe für die Tonhöhe in Form einer Midi-Note zwischen 0 und 127.

    Parameters:
    message (str): Im Terminal angezeigte Nachricht, die zur Eingabe einer Midi-Note oder eines Akkords auffordert.

    Returns:
    int: Validierte Midi-Note als Ganzzahl im Bereich 0 bis 127.
    list: Validierter Akkord mit folgender Syntax: [note1, note2,...] als Liste von Tonhöhen.
    """
    while True:
        global counter
        global break_loop
        global only_midi_notes
        global enough_input_to_calculate
        userInput = input(message)

        # Eingabe beenden, nur wenn min. ein Akkord oder zwei Midi-Noten vorhanden sind
        if userInput.lower() == '':
            if enough_input_to_calculate == False:
                print('ERROR: Please enter another midi note, not enough to calculate.')
                continue
            else:
                break_loop = True
                break
        
        # Programm beenden
        if userInput == 'exit':
            print('Exiting midi-toolbox...')
            sys.exit(0)

        if only_midi_notes == False: # extra Unterscheidung, damit nicht ein Akkord nach einem einzelnen Ton eingegeben werden kann
            if userInput.startswith('[') and userInput.endswith(']'): # Akkord
                chord = input_handler.chord_validation(userInput)
                if chord != None:
                    enough_input_to_calculate = True
                    return chord
            elif userInput.startswith('[') and not userInput.endswith(']'): # unvollständiger Akkord
                print('ERROR: Not a chord in the correct format [note1, note2,...]!')
                continue
            else:
                try:
                    userInput = int(userInput)
                    if userInput not in range(0, 128):
                        raise ValueError()
                except ValueError:
                    print('ERROR: Not a valid midi note, only numbers between 0 and 127 accepted!')
                else:
                    counter += 1
                    if counter >= 2:
                        enough_input_to_calculate = True
                    only_midi_notes = True
                    return userInput
        else:
            try:
                userInput = int(userInput)
                if userInput not in range(0, 128):
                    raise ValueError()
            except ValueError:
                print('ERROR: Not a valid midi note, only numbers between 0 and 127 accepted!')
            else:
                counter += 1
                if counter >= 2:
                    enough_input_to_calculate = True
                return userInput

def get_valid_inputs() -> list:
    while True:
        pitch = input_pitch("Please enter valid midi notes.\nPress [enter] to start the calculation. Type 'exit' to stop the program: ")
        if not break_loop:
            pitches.append(pitch)
        else:
            break
    return pitches

pitches = get_valid_inputs()

for i in range(len(pitches)):
    if type(pitches[i]) == list: # Akkord
        chord = []
        pitch = pitches[i]
        for j in range(len(pitch) - 1):
            interval = get_interval(pitch[j], pitch[j + 1])
            chord.append(interval)
            stringified_chord = str(chord).replace("'", "")
        print(f'The intervals for {str(pitch)} are {stringified_chord}.')
    else: # einzelne Note
        try:
            interval = get_interval(pitches[i], pitches[i + 1])
            if i + 1 > len(pitches):
                raise IndexError
        except IndexError:
            continue
        else:
            if interval != None:
                print(f'The interval between {pitches[i]} and {pitches[i + 1]} is {interval}.')