# Week 1 — EPOS2 / Motor Research and Setup

## Goal
Understand the hardware/software chain before attempting motor movement.

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

## Lab visit
1. Open EPOS Studio.
2. Connect to EPOS2 over USB.
3. Confirm the controller is detected.
4. Record Node ID.
5. Record configured motor and encoder settings.
6. Check for faults.
7. Do not command motion until configuration and mechanical setup are verified.

## Week 1 deliverable
Be able to explain how the Mac-written Python program will communicate with the EPOS2 through Maxon's EPOS Command Library, while the Linux laptop is used for actual USB/hardware testing.
