import survey
import runpy

miditools = [
    'arpeggiate',
    'count_intervals',
    'count_midi_notes',
    'frequency_to_midi',
    'generate_scale',
    'get_octave',
    'get_subsequent_intervals',
    'invert',
    'midi_to_frequency',
    'midi_to_pitch_class',
    'scale_timing',
    'transpose'
]

index = survey.routines.select('Choose miditool from toolbox: ', options = miditools, focus_mark = '> ',  evade_color = survey.colors.basic('yellow'))
miditool = miditools[index]
runpy.run_path(path_name=f'{miditool}.py')