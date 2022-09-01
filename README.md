# DTC Parser

Parser for diagnostic trouble codes (DTCs) used by vehicle onboard diagnosis (OBD). Resolves all digits of the code and outputs the resulting error information (e.g. vehicle part and descriptions).

## Usage

```
$ python parser.py --code CODE
```

## Example

```
$ python parser.py --code P0112

... parsing P0112 ...
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
VEHICLE PART:		 powertrain (engine, transmission, and associated accessories)
CODE TYPE:		 standardized (SAE) code, aka generic code
VEHICLE SUBSYSTEM:	 fuel and air metering
FAULT DESCRIPTION:	 intake air temperature sensor 1 circuit low
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
```
