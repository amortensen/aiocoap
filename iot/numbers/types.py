"""List of known values for the CoAP "Type" field.

As this field is only 2 bits, its valid values are comprehensively enumerated
in the `Type` object.
"""

from enum import IntEnum

class Type(IntEnum):
    CON = 0 # Confirmable
    NON = 1 # Non-confirmable
    ACK = 2 # Acknowledgement
    RST = 3 # Reset

CON, NON, ACK, RST = Type.CON, Type.NON, Type.ACK, Type.RST

__all__ = ['Type', 'CON', 'NON', 'ACK', 'RST']