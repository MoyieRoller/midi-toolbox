"""Input-Handler für verschiedene Eingaben"""

import midinotes
import asyncio
import sys

valid_durations = (0.0625, 0.125, 0.25, 0.5, 1.0)
duration_needed = False
break_loop = False

if __name__ == '__main__':
    pitches = []
    durations = []
    duration_needed = True

async def input_pitch(message: str) -> int:

    while True:
        userInput = input(message)

        if userInput.lower() == 'stop':
            global break_loop
            break_loop = True
            break
        
        if userInput == 'exit':
            print('Exiting midi-toolbox...')
            sys.exit(0)

        try:
            userInput = int(userInput)
            userInput in range(128) == True
        except ValueError:
            print('Not a valid midi note!')
        else:
            return userInput


async def input_duration(message: str) -> float:
    while True:
        userInput = input(message)

        if userInput == 'exit':
            print('Exiting midi-toolbox...')
            sys.exit(0)

        try:
            userInput = float(userInput) and userInput in valid_durations == True
            print(userInput)
        except (ValueError):
            print('Please enter a valid duration!')
        else:
            return userInput

async def main() -> None:
    pitch = await input_pitch('Please enter a valid midi note: ')

    if not break_loop:
        pitches.append(pitch)
        if duration_needed:
            duration = await input_duration('Please enter a valid duration: ')
            durations.append(duration)

if __name__ == '__main__':
    while True:
        asyncio.run(main())
        if break_loop == True:
            break
    print(pitches, durations)