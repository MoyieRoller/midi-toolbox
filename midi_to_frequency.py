import input_handler

pitches = []
frequencies = []

def midi_to_frequency(pitch: int) -> float:
    """Rechnet eine Midi-Note in die jeweilige Frequenz um.

    Parameters:
    pitch (int): Die MIDI-Tonhöhe der Noten.
    
    Returns:
    float: Die zugehörige Frequenz in Hz.
    """
    freq = 440 * (2**((pitch - 69) / 12))
    return freq

def get_valid_inputs() -> list:
    """Schleife um die Eingabe von Midi-Noten oder Akkorden zu ermöglichen.

    Returns:
    list: Eine Liste mit Midi-Noten oder Akkorden (Liste mit Tönen innerhalb der Liste).
    """
    while True:
        pitch = input_handler.input_pitch('Please enter a valid midi note or chord, press [enter] to stop the input: ')
        if not input_handler.break_loop:
            pitches.append(pitch)
        else:
            break
    return pitches

pitches = get_valid_inputs()

def round_frequency(freq: float) -> str:
    """Rundet die berechneten Frequenzen auf unterschiedliche Nachkommastellen, sodass für jede Frequenz
    genau fünf Ziffern verwendet werden. Es wurde explizit nicht round() verwendet, da bei bspw. 3.145 noch
    nicht aufgerundet wird.

    Parameters:
    frequency (float): Frequenz der jeweiligen Midi-Note in Hz.

    Returns:
    str: Gerundete Frequenz als string, damit in der Ausgabe auch alle gewünschten Nachkommstellen erscheinen,
            denn bei floats werden nachfolgende Nullen nicht dargestellt.
    """
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
    if type(pitch) == list: # Akkord
        chord = []
        for note in pitch:
            frequency = midi_to_frequency(note)
            frequency = round_frequency(frequency)
            chord.append(f'{frequency} Hz')
            stringified_chord = str(chord).replace("'", "")
        print(f'{pitch} = {stringified_chord}')
    else: # einzelne Note
        frequency = midi_to_frequency(pitch)
        frequency = round_frequency(frequency)
        print(f'{pitch} = {frequency} Hz')