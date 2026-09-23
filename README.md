# VeniBot EPOS Motor Control

Python tools for testing and controlling Maxon EPOS2 motor controllers for the VeniBot project.

## Hardware

- Maxon EPOS2 24/2 Positioning Controller
- Controller: Part #390438
- Maxon motor: Part #337880
- Maxon encoder adapter: Part #327086

## Project Structure

- `motor_test.py` — main motor test program
- `epos_interface.py` — EPOS2 communication interface
- `mock_epos.py` — mock interface for development without hardware
- `config.py` — EPOS configuration
- `week1_notes.md` — Week 1 research and notes

## Development

Development is being done on macOS, while hardware testing will be performed on the Linux lab computer.

The project uses Maxon's EPOS Command Library through Python `ctypes`.

## Safety

Motor parameters should be configured and verified in EPOS Studio before running motion commands.

<<<<<<< HEAD
# VeniBot EPOS2 Motor Control — Weeks 1 & 2

Develop the Python software on a Mac, then transfer it to the Linux lab laptop for real EPOS2 hardware testing.

Hardware from the lab photos:
- Maxon EPOS2 24/2 — #390438
- Maxon adapter — #327086
- Maxon motor — #337880

Important: do not guess motor/encoder parameters. Verify the exact configuration in EPOS Studio on the lab machine before commanding motion.

## Mac setup

1. Install Python 3.
2. Open Terminal and enter:
   `cd /path/to/venibot_epos_weeks_1_2`
3. Create a virtual environment:
   `python3 -m venv .venv`
4. Activate it:
   `source .venv/bin/activate`
5. No third-party packages are required.
6. Run the software in safe mock mode:
   `python3 motor_test.py --mock`

Mock mode does not connect to or move a motor. It lets you develop the program structure on your Mac.

## Linux lab setup

Copy the folder to the Linux laptop. After Maxon's Linux EPOS Command Library is installed, set its path, for example:

`export EPOS_LIB=/path/to/libEposCmd.so`

Then run:

`python3 motor_test.py`

Confirm the Node ID in EPOS Studio before using the real hardware.
=======
# venibot-epos-motor-control
Python Motor Control for Venibot EPOS2
>>>>>>> 09d7661ec1a917e0c745b922936ae480f0ff41bd
