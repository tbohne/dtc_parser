#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Tim Bohne

import argparse


def parse_vehicle_part(char):
    """
    OBD-II codes start with a letter that denotes the part of the vehicle that has a fault.

    :param char: first char of the DTC
    :return: parsed vehicle part
    """
    if char == "P":
        return "powertrain (engine, transmission, and associated accessories)"
    elif char == "C":
        return "chassis (covers mechanical systems and functions: steering, suspension, and braking)"
    elif char == "B":
        return "body (parts that are mainly found in the passenger compartment area)"
    elif char == "U":
        return "network & vehicle integration (functions that are managed by the onboard computer system)"
    else:
        print("unknown first char")
        return "---"


def parse_code_type(char):
    """
    The second char is a number (0 or 1) that determines the type of the code.
        0 -> generic
        1 -> manufacturer-specific

    :param char: second char of the DTC
    :return: parsed code type
    """
    if char == "0":
        return "standardized (SAE) code, aka generic code"
    elif char == "1":
        return "manufacturer-specific code"
    else:
        print("unknown second char")
        return "---"


def parse_vehicle_subsystem(char):
    """
    The third char tells which vehicle subsystem has a fault.

    :param char: third char of the DTC
    :return: parsed vehicle subsystem
    """
    if char == "0":
        return "fuel and air metering and auxiliary emission controls"
    elif char == "1":
        return "fuel and air metering"
    elif char == "2":
        return "fuel and air metering – injector circuit"
    elif char == "3":
        return "ignition systems or misfires"
    elif char == "4":
        return "auxiliary emission controls"
    elif char == "5":
        return "vehicle speed control, idle control systems, and auxiliary inputs"
    elif char == "6":
        return "computer and output circuit"
    elif char == "7":
        return "transmission"
    elif char in ["A", "B", "C"]:
        return "hybrid propulsion systems"
    else:
        print("unknown third char")
        return "---"


def parse_fault_description(code):
    assert len(code) == 2
    error_code = int(code)
    print("err:", error_code)


def parse_code(code):
    """
    Parses the provided DTC.

    :param code: DTC to be parsed
    """
    print("parsing", code)
    assert len(code) == 5

    parse_vehicle_part(code[0])
    parse_code_type(code[1])
    parse_vehicle_subsystem(code[2])
    parse_fault_description(code[3] + code[4])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parser for diagnostic trouble codes (DTCs)')
    parser.add_argument('--code', action='store', type=str, help='DTC to be parsed', required=True)
    args = parser.parse_args()
    parse_code(args.code)