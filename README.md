# PULSE-CHARGER

## Description

Pulse charging setup designed for research and development on improving lithium-ion battery cell reliability, longevity, as well as reduction of gassing. 

## Hardware Devices

- Diligent Digital Discovery (Pattern generator)
- KIPRIM DC310S Programmable Power Supply (Source)
- NI USB-6008 (DAQ unit, SSR control)

## Circuit

`#TODO`

## Get Started

1. Connect all necessary components to each respective terminal block.
2. Supply the BDMS modules with sufficient power. For a LiPo with 4.2V max, 9V VCC to each BDMS (SSR) was used.
3. Run the .exe
4. Input each parameter as prompted into the terminal window. For efficiency, you may copy a list of them (delimit by newline chars) and hit `Ctrl+V` to enter them all at once.
5. The program should begin to run indicating the system state in green text, and each data readout in blue text.
6. The program will run until the battery has cycled below the cutoff percent of initial capacity, or the user presses `Ctrl+C`. 

## Resources Used

https://github.com/maximweb/kiprim-dc310s

https://github.com/Digilent/WaveForms-SDK-Getting-Started-PY

https://github.com/ni/nidaqmx-python/tree/master