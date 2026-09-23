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
