# DTC Parser

Parser for [diagnostic trouble codes](https://en.wikipedia.org/wiki/OBD-II_PIDs) (DTCs) used by vehicle [on-board diagnostics](https://en.wikipedia.org/wiki/On-board_diagnostics) (OBD). Resolves all digits of the code and outputs the resulting error information (e.g. vehicle part and descriptions).

## Installation
```
$ git clone https://github.com/tbohne/dtc_parser.git
$ cd dtc_parser/
$ pip install .
```

## Usage
```
$ python dtc_parser/parser.py --code CODE
```

## Example
```
$ python dtc_parser/parser.py --code P0112

... parsing P0112 ...
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
VEHICLE PART:		 powertrain (engine, transmission, and associated accessories)
CODE TYPE:		 standardized (SAE) code, aka generic code
VEHICLE SUBSYSTEM:	 fuel and air metering
FAULT DESCRIPTION:	 intake air temperature sensor 1 circuit low
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
```
