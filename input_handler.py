"""Input-Handler für verschiedene Eingaben"""

import asyncio
import sys

valid_durations = (0.0625, 0.125, 0.25, 0.5, 1.0)
break_loop = False

if __name__ == '__main__':
    pitch = 0
    duration = 0.0
    pitches = []
    durations = []
    duration_needed = True

def input_pitch(message: str) -> int | list:
    """ User-Eingabe für die Tonhöhe in Form einer Midi-Note zwischen 0 und 127.

    Parameters:
    message (str): Im Terminal angezeigte Nachricht, die zur Eingabe einer Midi-Note oder eines Akkords auffordert.

    Returns:
    int: Validierte Midi-Note als Ganzzahl im Bereich 0 bis 127.
    list: Validierter Akkord mit folgender Syntax: [note1, note2,...] als Liste von Tonhöhen.
    """
    while True:
        userInput = input(message)

        if userInput.lower() == '':
            global break_loop
            break_loop = True
            break
        
        if userInput == 'exit':
            print('Exiting midi-toolbox...')
            sys.exit(0)

        if userInput.startswith('[') and userInput.endswith(']'):
            chord = chord_validation(userInput)
            if chord != None:
                return chord
        elif userInput.startswith('[') and not userInput.endswith(']'):
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
                return userInput

def input_duration(message: str) -> float:
    """ User-Eingabe für die zur Midi-Tonhöhe zugehörige Dauer des Tons. Zur Vereinfachung, werden nur Ganze
    bis Sechzehntel-Noten akzeptiert.

    Parameters:
    message (str): Im Terminal angezeigte Nachrichte, die zur Eingabe einer Dauer auffordert.

    Returns:
    float: Dauer des Tons/Akkords als einer von folgenden floats: 0.625, 0.125, 0.25, 0.5 und 1.0.
    """
    while True:
        userInput = input(message)

        if userInput.lower() == '':
            print('WARNING: You need to enter a duration for the last midi note or chord!')
            continue

        if userInput == 'exit':
            print('Exiting midi-toolbox...')
            sys.exit(0)

        try:
            userInput = float(userInput)
            if userInput not in valid_durations:
                raise ValueError()
        except (ValueError):
            print('ERROR: Not a valid duration, only sixteenth to whole notes accepted!')
        else:
            return userInput

def chord_validation(userInput: str) -> list:
    """Validiert den Inhalt eines eingegebenen Akkords auf korrekte Midi-Tonhöhen.

    Parameters:
    userInput (str): User-Eingabe, solange diese mit '[' beginnt und mit ']' endet.

    Returns:
    list: Gibt den Akkord 
    """
    chord = []
    try:
        stripped_input = userInput.strip('[]')
        chord_list = stripped_input.split(',')

        for single_note_string in chord_list:
            single_note = int(single_note_string)
            if single_note not in range(0, 128):
                raise ValueError
            else:
                chord.append(single_note)
    except ValueError:
        print('ERROR: Not a valid midi note within the chord, only numbers between 0 and 127 seperated by commas accepted!')
    else:
        return chord

if __name__ == '__main__':
    while True:
        pitch = input_pitch('Please enter a valid midi note or chord, press enter to stop the input: ')
        if not break_loop:
            pitches.append(pitch)
            if duration_needed:
                duration = input_duration('Please enter a valid duration, only sixteenth to whole notes accepted: ')
                durations.append(duration)
        else:
            break
    print(pitches, durations)