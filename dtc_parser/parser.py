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
    def parse_vehicle_part(char: str) -> str:
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
    def parse_code_type(char: str) -> str:
        """
        The second char is a number that determines the type of the code.
            0  -> generic
            >0 -> manufacturer-specific

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
    def parse_vehicle_subsystem(first_char, third_char: str) -> str:
        """
        The third char tells which vehicle subsystem has a fault (based on the category (first char)).
        This function returns the subsystems for powertrain codes.

        :param first_char: first char of the DTC
        :param third_char: third char of the DTC
        :return: parsed vehicle subsystem
        """
        # TODO: only supporting powertrain (P) subsystems atm, should be extended when
        #       a source for the other categories can be found
        if first_char != "P":
            print("we don't have information about subsystems for category", first_char)
            return "unknown"
        elif third_char == "0":
            return "fuel and air metering and auxiliary emission controls"
        elif third_char == "1":
            return "fuel and air metering"
        elif third_char == "2":
            return "fuel and air metering – injector circuit"
        elif third_char == "3":
            return "ignition systems or misfires"
        elif third_char == "4":
            return "auxiliary emission controls"
        elif third_char == "5":
            return "vehicle speed control, idle control systems, and auxiliary inputs"
        elif third_char == "6":
            return "computer and output circuit"
        elif third_char == "7":
            return "transmission"
        elif third_char in ["A", "B", "C"]:
            return "hybrid propulsion systems"
        else:
            print("unknown third char")
            return "unknown"

    @staticmethod
    def get_code_from_dict(code_dict: dict, code: str) -> str:
        """
        Parses the specified DTC using the specified dictionary (if supported).

        :param code_dict: dictionary to parse DTC info from
        :param code: DTC to be parsed
        :return: parsed DTC info
        """
        return code_dict[code] if code in code_dict.keys() else "unsupported DTC"

    def parse_generic_powertrain_fault(self, prefix: str, code: str) -> str:
        """
        Parses the generic powertrain fault.

        :param prefix: first two characters (category)
        :param code: last three chars (specific fault)
        :return: generic powertrain fault
        """
        if code[0] == "0":
            return self.get_code_from_dict(error_codes.P00_ERRORS, prefix + code)
        elif code[0] == "1":
            return self.get_code_from_dict(error_codes.P01_ERRORS, prefix + code)
        elif code[0] == "2":
            return self.get_code_from_dict(error_codes.P02_ERRORS, prefix + code)
        elif code[0] == "3":
            return self.get_code_from_dict(error_codes.P03_ERRORS, prefix + code)
        elif code[0] == "4":
            return self.get_code_from_dict(error_codes.P04_ERRORS, prefix + code)
        elif code[0] == "5":
            return self.get_code_from_dict(error_codes.P05_ERRORS, prefix + code)
        elif code[0] == "6":
            return self.get_code_from_dict(error_codes.P06_ERRORS, prefix + code)
        elif code[0] == "7":
            return self.get_code_from_dict(error_codes.P07_ERRORS, prefix + code)
        elif code[0] == "8":
            return self.get_code_from_dict(error_codes.P08_ERRORS, prefix + code)
        elif code[0] == "9":
            return self.get_code_from_dict(error_codes.P09_ERRORS, prefix + code)
        elif code[0] == "A":
            return self.get_code_from_dict(error_codes.P0A_ERRORS, prefix + code)
        elif code[0] == "B":
            return self.get_code_from_dict(error_codes.P0B_ERRORS, prefix + code)
        elif code[0] == "C":
            return self.get_code_from_dict(error_codes.P0C_ERRORS, prefix + code)
        else:
            print("invalid generic powertrain code")
            return "---"

    def parse_manufacturer_specific_powertrain_fault(self, prefix: str, code: str) -> str:
        """
        Parses the manufacturer-specific powertrain fault.

        :param prefix: first two characters (category)
        :param code: last three chars (specific fault)
        :return: manufacturer-specific powertrain fault
        """
        if prefix[1] == "1":
            return self.get_code_from_dict(error_codes.P1_ERRORS, prefix + code)
        elif prefix[1] == "2":
            return self.get_code_from_dict(error_codes.P2_ERRORS, prefix + code)
        elif prefix[1] == "3":
            return self.get_code_from_dict(error_codes.P3_ERRORS, prefix + code)
        else:
            print("invalid manufacturer-specific powertrain code")
            return "---"

    def parse_generic_chassis_fault(self, prefix: str, code: str) -> str:
        """
        Parses the generic chassis fault.

        :param prefix: first two characters (category)
        :param code: last three chars (specific fault)
        :return: generic chassis fault
        """
        return self.get_code_from_dict(error_codes.C0_ERRORS, prefix + code)

    def parse_manufacturer_specific_chassis_fault(self, prefix: str, code: str) -> str:
        """
        Parses the manufacturer-specific chassis fault.

        :param prefix: first two characters (category)
        :param code: last three chars (specific fault)
        :return: manufacturer-specific chassis fault
        """
        if prefix[1] == "1":
            return self.get_code_from_dict(error_codes.C1_ERRORS, prefix + code)
        elif prefix[1] == "2":
            return self.get_code_from_dict(error_codes.C2_ERRORS, prefix + code)
        else:
            print("invalid manufacturer-specific chassis code")
            return "---"

    def parse_generic_body_fault(self, prefix: str, code: str) -> str:
        """
        Parses the generic body fault.

        :param prefix: first two characters (category)
        :param code: last three chars (specific fault)
        :return: generic body fault
        """
        return self.get_code_from_dict(error_codes.B0_ERRORS, prefix + code)

    def parse_manufacturer_specific_body_fault(self, prefix: str, code: str) -> str:
        """
        Parses the manufacturer-specific body fault.

        :param prefix: first two characters (category)
        :param code: last three chars (specific fault)
        :return: manufacturer-specific body fault
        """
        if prefix[1] == "1":
            return self.get_code_from_dict(error_codes.B1_ERRORS, prefix + code)
        elif prefix[1] == "2":
            return self.get_code_from_dict(error_codes.B2_ERRORS, prefix + code)
        else:
            print("invalid manufacturer-specific body code")
            return "---"

    def parse_generic_network_fault(self, prefix: str, code: str) -> str:
        """
        Parses the generic network fault.

        :param prefix: first two characters (category)
        :param code: last three chars (specific fault)
        :return: generic network fault
        """
        return self.get_code_from_dict(error_codes.U0_ERRORS, prefix + code)

    def parse_manufacturer_specific_network_fault(self, prefix: str, code: str) -> str:
        """
        Parses the manufacturer-specific network fault.

        :param prefix: first two characters (category)
        :param code: last three chars (specific fault)
        :return: manufacturer-specific network fault
        """
        if prefix[1] == "1":
            return self.get_code_from_dict(error_codes.U1_ERRORS, prefix + code)
        elif prefix[1] == "2":
            return self.get_code_from_dict(error_codes.U2_ERRORS, prefix + code)
        else:
            print("invalid manufacturer-specific network code")
            return "---"

    def parse_fault_description(self, prefix: str, error_code: str) -> str:
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
            return self.parse_generic_chassis_fault(prefix, error_code)
        elif prefix in ["C1", "C2"]:
            return self.parse_manufacturer_specific_chassis_fault(prefix, error_code)
        elif prefix == "B0":
            return self.parse_generic_body_fault(prefix, error_code)
        elif prefix in ["B1", "B2"]:
            return self.parse_manufacturer_specific_body_fault(prefix, error_code)
        elif prefix == "U0":
            return self.parse_generic_network_fault(prefix, error_code)
        elif prefix in ["U1", "U2"]:
            return self.parse_manufacturer_specific_network_fault(prefix, error_code)
        else:
            print("unknown category (first two chars of code)")
            return "---"

    def parse_code(self, code: str) -> None:
        """
        Parses the provided DTC.

        :param code: DTC to be parsed
        """
        print("... parsing", code, "...")
        assert len(code) == 5
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("VEHICLE PART:\t\t", self.parse_vehicle_part(code[0]))
        print("CODE TYPE:\t\t", self.parse_code_type(code[1]))
        print("VEHICLE SUBSYSTEM:\t", self.parse_vehicle_subsystem(code[0], code[2]))
        print("FAULT DESCRIPTION:\t",
              self.parse_fault_description(code[0] + code[1], code[2] + code[3] + code[4]).lower())
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def parse_code_machine_readable(self, code: str) -> dict:
        """
        Parses the provided DTC and returns the results in a machine-readable format.

        :param code: DTC to be parsed
        :return: parsed DTC results in machine-readable format
        """
        print("... parsing", code, "...")
        assert len(code) == 5
        return {
            "vehicle_part": self.parse_vehicle_part(code[0]),
            "code_type": self.parse_code_type(code[1]),
            "vehicle_subsystem": self.parse_vehicle_subsystem(code[0], code[2]),
            "fault_description": self.parse_fault_description(code[0] + code[1], code[2] + code[3] + code[4]).lower()
        }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parser for diagnostic trouble codes (DTCs)')
    parser.add_argument('--code', action='store', type=str, help='DTC to be parsed', required=True)
    args = parser.parse_args()
    dtc_parser = DTCParser()
    dtc_parser.parse_code(args.code)
