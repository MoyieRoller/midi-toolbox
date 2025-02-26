"""Input-Handler für verschiedene Eingaben"""

import midinotes
import asyncio
import sys

valid_durations = (0.0625, 0.125, 0.25, 0.5, 1.0)
duration_needed = False

if __name__ == '__main__':
    pitches = []
    durations = []
    duration_needed = True
    stop_looping = False

class LoopBreak(Exception):
    pass

async def input_pitch(message: str) -> int:
    stop_looping = False
    try:
        while True:
            userInput = input(message)

            if userInput.lower() == 'stop':
                print('stop')
                stop_looping = True
                raise LoopBreak()
            
            if userInput == 'exit':
                sys.exit(0)

            try:
                userInput = int(userInput)
                userInput in range(128) == True
            except ValueError:
                print('Not a valid midi note!')
            else:
                return userInput
    except LoopBreak:
        pass

async def input_duration(message: str) -> float:
    while True:
        userInput = input(message)
        try:
            userInput = float(userInput) and userInput in valid_durations == True
            print(userInput)
        except (ValueError, Input):
            print('Please enter a valid duration!')
        else:
            return userInput

async def main() -> None:
    pitch = await input_pitch('Please enter a valid midi note: ')
    pitches.append(pitch)
    if duration_needed and stop_looping == False:
        duration = await input_duration('Please enter a valid duration: ')
        durations.append(duration)

if __name__ == '__main__':
    while True:
        asyncio.run(main())
        if stop_looping == True:
            break
    print(pitches, durations)