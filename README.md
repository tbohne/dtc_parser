# DTC Parser

![unstable](https://img.shields.io/badge/stability-unstable-orange)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Parser for [diagnostic trouble codes](https://en.wikipedia.org/wiki/OBD-II_PIDs) (DTCs) used by vehicle [on-board diagnostics](https://en.wikipedia.org/wiki/On-board_diagnostics) (OBD). Resolves all digits of the code and outputs the resulting error information (e.g. vehicle part and descriptions). The parser currently supports *5090* DTCs from all categories, i.e., powertrain, body, chassis and user network, both generic and manufacturer-specific ones. If you miss DTCs, please don't hesitate to file an issue or directly add them in a PR.

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

## Code Scheme

`<VEHICLE_PART>_<CODE_TYPE>_<VEHICLE_SUBSYSTEM>_<FAULT_DESCRIPTION>`

## Related Publications

```bibtex
@inproceedings{10.1145/3587259.3627546,
    author = {Bohne, Tim and Windler, Anne-Kathrin Patricia and Atzmueller, Martin},
    title = {A Neuro-Symbolic Approach for Anomaly Detection and Complex Fault Diagnosis Exemplified in the Automotive Domain},
    year = {2023},
    isbn = {9798400701412},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    url = {https://doi.org/10.1145/3587259.3627546},
    doi = {10.1145/3587259.3627546},
    booktitle = {Proceedings of the 12th Knowledge Capture Conference 2023},
    pages = {35–43},
    numpages = {9},
    location = {Pensacola, FL, USA},
    series = {K-CAP '23}
}
```
