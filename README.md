# Z80_interpreter (GameBoy subset)
A Z80 ASM interpreter (emulator) written in Python<br>
![GameBoy](https://user-images.githubusercontent.com/31623036/81413989-a0383d80-9146-11ea-8be7-99123ede8f0e.png)


## Features

- Parser for loading in assembly (.asm) files (I/O)
- Lexer to tokenize the input file
- Parser to check the validity of the tokens
- Runner to execute the parsed tokens
- 16x16 pixel display that reads pixel color values from CPU memory (I/O)
- Error handling: Invalid assembly lines are printed to the console including the line number.

## Limitations

Not all instructions are implemented, most of those unimplemented functions have to do with interrupts. Trying to call an unimplemented function will result in an NotImplementedError.
<br>Note: The unimplemented instructions can be found inside `helpers/opcodes.py`.

## How to use
- Install the required python packages using `pip install -r requirements.txt`

There are two files which can be executed (`main.py` and `run.py`)
1. `main.py` will load the `display_test.asm` file and print the result of every 'stage'.
2. `run.py` which asks for command line parameters <br>example: `python3 run.py --input src/display_test.asm --display True`

### Displaying pixels
The display memory range is `0x0000` - `0x00FF` write a value between 0-255 to display a color. The full color range can be seen inside the screenshot.


### Examples

There are pre-made test assembly files, which can be found inside the `src/` folder and are fully documented.


## Screenshot
<img width="1440" alt="Schermafbeelding 2020-05-08 om 13 41 19" src="https://user-images.githubusercontent.com/31623036/81402483-ca333500-9131-11ea-9920-e4fc0aebaa34.png">