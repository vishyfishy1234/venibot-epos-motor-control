# WEEK 1 — EPOS2 / MOTOR RESEARCH AND SETUP

## Goal

Understand the hardware/software chain before attempting motor movement.

Setup EPOS Studio & Motor Parameters

## Hardware chain

Laptop -> USB -> EPOS2 24/2 (#390438) -> Maxon adapter (#327086) -> motor (#337880)

## Research checklist

- [ ] Confirm EPOS2 model and part number.
- [ ] Understand USB connection and Node ID.
- [ ] Understand enable/disable and fault states.
- [ ] Understand profile velocity mode.
- [ ] Confirm motor part #337880.
- [ ] Find the exact motor documentation/datasheet.
- [ ] Record rated voltage, speed, current, encoder type/resolution.
- [ ] Confirm adapter #327086 and its signal/pin functions.
- [ ] Install Python on Mac.
- [ ] Create this project and virtual environment.
- [ ] Read about VCS_OpenDevice / VCS_CloseDevice.
- [ ] Read about VCS_ClearFault / VCS_SetEnableState / VCS_SetDisableState.
- [ ] Read about reading position, velocity, and faults.

## EPOS Studio Setup

1. Opened EPOS Studio and created an EPOS2 project.
2. Connected the EPOS2 over USB and confirmed that the controller was detected.
3. Connected the required external 12 V power supply.
4. Used the Startup Wizard to configure the EPOS2 using the motor and encoder documentation.
5. Configured the motor as a DC motor.
6. Configured the incremental encoder and verified the encoder resolution.
7. Configured the encoder as being mounted on the motor with the gear system enabled.
8. Configured the communication settings:
   - Interface: USB
   - Port: USB0
   - Node ID: 1
9. Configured the motor/system parameters in EPOS Studio.
10. Completed Regulation Tuning / Auto Tuning.
11. Used the Position Mode tools to verify that the encoder position changed when manually rotating the motor shaft.

## Motor Control Test

1. Used Device Control in EPOS Studio to enable and disable the EPOS2.
2. Verified that the controller could successfully communicate with the motor.
3. Used Profile Position Mode to test motor movement.
4. Changed parameters such as target position and target velocity.
5. Successfully commanded the motor to move.
6. Verified that the motor responded to the changed parameters.
7. Verified that the actual position followed the commanded position.
8. Confirmed that the motor could be controlled successfully through EPOS Studio.

## Lab Visit

1. Open EPOS Studio.
2. Connect to EPOS2 over USB.
3. Confirm the controller is detected.
4. Record Node ID.
5. Record configured motor and encoder settings.
6. Check for faults.
7. Do not command motion until configuration and mechanical setup are verified.

## Week 1 Deliverable

Successfully configured and tested the EPOS2 and motor through EPOS Studio. The motor parameters and encoder were configured using the provided documentation, Regulation Tuning was completed, the encoder was verified, and the motor was successfully moved and controlled by changing position and velocity parameters.

The hardware setup is now ready for the next stage: communicating with and controlling the EPOS2 through Python using Maxon's EPOS Command Library.

# WEEK 2 NOTES — PYTHON + EPOS2 HARDWARE

## Goal

Begin controlling and communicating with the Maxon EPOS2 through Python on the Linux workstation using the Maxon EPOS Command Library.

## Completed

### 1. EPOS Command Library

- Located the existing Maxon EPOS Linux Command Library on the lab workstation.
- Confirmed the library is compatible with the Linux system.
- Resolved the `libftd2xx.so` dependency using `LD_LIBRARY_PATH`.
- Successfully loaded `libEposCmd.so` through Python `ctypes`.

### 2. EPOS2 USB Connection

- Connected the physical EPOS2 controller to the Linux workstation.
- Confirmed the controller appears through USB:
  - USB ID: `0403:a8b0`
  - Device: maxon motor EPOS2
- Successfully opened and closed the EPOS2 connection using Python.
- Configuration used:
  - Device: `EPOS2`
  - Protocol: `MAXON SERIAL V2`
  - Interface: `USB`
  - Port: `USB0`
  - Node ID: `1`

### 3. Read EPOS2 Status

Python successfully reads:

- Enabled state
- Fault state
- Position
- Velocity

Initial hardware status:

```text
enabled: False
fault: False
position: 0
velocity: 0