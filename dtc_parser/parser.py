#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Tim Bohne

import argparse

from dtc_parser import error_codes


class DTCParser:
    """
    Parser for diagnostic trouble codes (DTCs) used by vehicle onboard diagnosis (OBD).
    """

    def __init__(self):
        self.vehicle_part = ""
        self.code_type = ""
        self.vehicle_subsystem = ""
        self.fault_description = ""

    @staticmethod
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

    @staticmethod
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
        elif char in ["1", "2", "3"]:
            return "manufacturer-specific code"
        else:
            print("unknown second char")
            return "---"

    @staticmethod
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

    @staticmethod
    def parse_generic_powertrain_fault(prefix, code):
        """
        Parses the generic powertrain fault.

        :param prefix: first two characters (category)
        :param code: last three chars (specific fault)
        :return: generic powertrain fault
        """
        if code[0] == "0":
            return error_codes.P00_ERRORS[prefix + code]
        elif code[0] == "1":
            return error_codes.P01_ERRORS[prefix + code]
        elif code[0] == "2":
            return error_codes.P02_ERRORS[prefix + code]
        elif code[0] == "3":
            return error_codes.P03_ERRORS[prefix + code]
        elif code[0] == "4":
            return error_codes.P04_ERRORS[prefix + code]
        elif code[0] == "5":
            return error_codes.P05_ERRORS[prefix + code]
        elif code[0] == "6":
            return error_codes.P06_ERRORS[prefix + code]
        elif code[0] == "7":
            return error_codes.P07_ERRORS[prefix + code]
        elif code[0] == "8":
            return error_codes.P08_ERRORS[prefix + code]
        elif code[0] == "9":
            return error_codes.P09_ERRORS[prefix + code]
        elif code[0] == "A":
            return error_codes.P0A_ERRORS[prefix + code]
        elif code[0] == "B":
            return error_codes.P0B_ERRORS[prefix + code]
        elif code[0] == "C":
            return error_codes.P0C_ERRORS[prefix + code]
        else:
            print("invalid generic powertrain code")
            return "---"

    @staticmethod
    def parse_manufacturer_specific_powertrain_fault(prefix, code):
        """
        Parses the manufacturer-specific powertrain fault.

        :param prefix: first two characters (category)
        :param code: last three chars (specific fault)
        :return: manufacturer-specific powertrain fault
        """
        if prefix[1] == "1":
            return error_codes.P1_ERRORS[prefix + code]
        elif prefix[1] == "2":
            return error_codes.P2_ERRORS[prefix + code]
        elif prefix[1] == "3":
            return error_codes.P3_ERRORS[prefix + code]
        else:
            print("invalid manufacturer-specific powertrain code")
            return "---"

    def parse_fault_description(self, prefix, error_code):
        """
        Parses the specific fault description (last three chars) based on the category (first two chars).

        :param prefix: first two characters (category)
        :param error_code: last three chars (specific fault)
        :return: parsed fault description
        """
        assert len(prefix) == 2 and len(error_code) == 3

        if prefix == "P0":
            return self.parse_generic_powertrain_fault(prefix, error_code)
        elif prefix in ["P1", "P2", "P3"]:
            return self.parse_manufacturer_specific_powertrain_fault(prefix, error_code)
        elif prefix == "C0":
            print("generic chassis fault descriptions not yet supported..")
            return "----"
        elif prefix == "C1":
            print("manufacturer-specific chassis fault descriptions not yet supported..")
            return "----"
        elif prefix == "B0":
            print("generic body fault descriptions not yet supported..")
            return "----"
        elif prefix == "B1":
            print("manufacturer-specific body fault descriptions not yet supported..")
            return "----"
        elif prefix == "U0":
            print("generic network fault descriptions not yet supported..")
            return "----"
        elif prefix == "U1":
            print("manufacturer-specific network fault descriptions not yet supported..")
            return "----"
        else:
            print("unknown category (first two chars of code)")
            return "---"

    def parse_code(self, code):
        """
        Parses the provided DTC.

        :param code: DTC to be parsed
        """
        print("... parsing", code, "...")
        assert len(code) == 5

        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("VEHICLE PART:\t\t", self.parse_vehicle_part(code[0]))
        print("CODE TYPE:\t\t", self.parse_code_type(code[1]))
        print("VEHICLE SUBSYSTEM:\t", self.parse_vehicle_subsystem(code[2]))
        print("FAULT DESCRIPTION:\t",
              self.parse_fault_description(code[0] + code[1], code[2] + code[3] + code[4]).lower())
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def parse_code_machine_readable(self, code):
        """
        Parses the provided DTC and returns the results in a machine-readable format.

        :param code: DTC to be parsed
        :return: parsed DTC results in machine-readable format
        """
        print("... parsing", code, "...")
        assert len(code) == 5
        return "{" + self.parse_vehicle_part(code[0]) + ", " + self.parse_code_type(code[1]) + ", " \
               + self.parse_vehicle_subsystem(code[2]) + ", " \
               + self.parse_fault_description(code[0] + code[1], code[2] + code[3] + code[4]).lower() + "}"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parser for diagnostic trouble codes (DTCs)')
    parser.add_argument('--code', action='store', type=str, help='DTC to be parsed', required=True)
    args = parser.parse_args()

    dtc_parser = DTCParser()
    dtc_parser.parse_code(args.code)
