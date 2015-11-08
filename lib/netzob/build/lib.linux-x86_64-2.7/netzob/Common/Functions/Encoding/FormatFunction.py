# -*- coding: utf-8 -*-

#+---------------------------------------------------------------------------+
#|          01001110 01100101 01110100 01111010 01101111 01100010            |
#|                                                                           |
#|               Netzob : Inferring communication protocols                  |
#+---------------------------------------------------------------------------+
#| Copyright (C) 2011 Georges Bossert and Frédéric Guihéry                   |
#| This program is free software: you can redistribute it and/or modify      |
#| it under the terms of the GNU General Public License as published by      |
#| the Free Software Foundation, either version 3 of the License, or         |
#| (at your option) any later version.                                       |
#|                                                                           |
#| This program is distributed in the hope that it will be useful,           |
#| but WITHOUT ANY WARRANTY; without even the implied warranty of            |
#| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the              |
#| GNU General Public License for more details.                              |
#|                                                                           |
#| You should have received a copy of the GNU General Public License         |
#| along with this program. If not, see <http://www.gnu.org/licenses/>.      |
#+---------------------------------------------------------------------------+
#| @url      : http://www.netzob.org                                         |
#| @contact  : contact@netzob.org                                            |
#| @sponsors : Amossys, http://www.amossys.fr                                |
#|             Supélec, http://www.rennes.supelec.fr/ren/rd/cidre/           |
#+---------------------------------------------------------------------------+

#+---------------------------------------------------------------------------+
#| Standard library imports
#+---------------------------------------------------------------------------+
import logging
import struct
from netzob.Common.Type.Format import Format
from netzob.Common.Functions.EncodingFunction import EncodingFunction
from netzob.Common.Type.TypeConvertor import TypeConvertor
from netzob.Common.Type.UnitSize import UnitSize
from netzob.Common.Type.Endianess import Endianess
from netzob.Common.Type.Sign import Sign

#+---------------------------------------------------------------------------+
#| Related third party imports
#+---------------------------------------------------------------------------+

#+---------------------------------------------------------------------------+
#| Local application imports
#+---------------------------------------------------------------------------+


#+---------------------------------------------------------------------------+
#| FormatFunction:
#|     Definition of an encoding function which apply a format on a message
#+---------------------------------------------------------------------------+
class FormatFunction(EncodingFunction):

    TYPE = "FormatFunction"

    def __init__(self, name, formatType, unitSize, endianness, sign):
        EncodingFunction.__init__(self, FormatFunction.TYPE, name)
        self.formatType = formatType
        self.unitsize = unitSize
        self.endianness = endianness
        self.sign = sign

    def apply(self, message):

        if self.unitsize != UnitSize.NONE:
            # First we apply the unit size
            # Default modulo = 2 => 8BITS
            if self.unitsize == UnitSize.BIT:
                modulo = 1
            else:
                modulo = UnitSize.getSizeInBits(self.unitsize) / 4

            splittedData = []
            tmpResult = ""
            for i in range(0, len(message)):
                if i > 0 and i % modulo == 0:
                    splittedData.append(tmpResult)
                    tmpResult = ""
                tmpResult = tmpResult + message[i]
            splittedData.append(tmpResult)
        else:
            splittedData = [message]

        encodedSplittedData = []
        # Now we have the message splitted per unit size
        # we apply endianess on it
        # we consider the normal mode is big-endian
        for i in range(0, len(splittedData)):
            origNetzobRaw = splittedData[i]

            # SPECIAL CASE : ASCII we do not compute endianess neither signed/unsigned
            if not self.formatType == Format.STRING and UnitSize.getSizeInBits(self.unitsize) >= 8 and not self.formatType == Format.BINARY:
                tmpVal = UnitSize.getSizeInBits(self.unitsize) / 4 - len(origNetzobRaw)
                if self.endianness == Endianess.BIG:
                    netzobRaw = (tmpVal * "0") + origNetzobRaw
                else:
                    netzobRaw = origNetzobRaw + (tmpVal * "0")

                # Convert in Python raw
                pythonraw = TypeConvertor.netzobRawToPythonRaw(netzobRaw)

                # Create transformer
                # - ENDIANESS
                transformer = ">"
                if self.endianness == Endianess.LITTLE:
                    transformer = "<"
                # - SIGNED/UNISGNED
                if self.sign == Sign.SIGNED:
                    transformer = transformer + (UnitSize.getPackDefiniton(self.unitsize)).lower()
                else:
                    transformer = transformer + (UnitSize.getPackDefiniton(self.unitsize)).upper()

                # Apply the transformation
                (unpackRaw,) = struct.unpack(transformer, pythonraw)

                localResult = ""
                fmt = "%" + str(UnitSize.getMaxDigitForTypeAndUnitSize(self.formatType, self.unitsize))
                if self.formatType == Format.OCTAL:
                    localResult = (fmt + "o") % unpackRaw
                elif self.formatType == Format.DECIMAL:
                    localResult = (fmt + "d") % unpackRaw
                elif self.formatType == Format.HEX:
                    localResult = (fmt + "s") % origNetzobRaw
                encodedSplittedData.append(localResult)
            elif self.formatType == Format.STRING:
                encodedSplittedData.append(TypeConvertor.netzobRawToString(origNetzobRaw))
            elif self.formatType == Format.BINARY:
                encodedSplittedData.append(TypeConvertor.netzobRawToBinary(origNetzobRaw))
            elif self.formatType == Format.IPv4:
                encodedSplittedData.append(TypeConvertor.netzobRawToIPv4(origNetzobRaw))
            elif UnitSize.getSizeInBits(self.unitsize) < UnitSize.getSizeInBits(UnitSize.BITS8):
                encodedSplittedData.append(TypeConvertor.encodeNetzobRawToGivenType(origNetzobRaw, self.formatType))

        # Before sending back (;D) we join everything
        return " ".join(encodedSplittedData)

    def getConversionAddressingTable(self, message):
        return None
