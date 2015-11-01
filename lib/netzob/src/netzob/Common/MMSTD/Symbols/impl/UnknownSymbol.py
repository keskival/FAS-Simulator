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
from bitarray import bitarray

#+---------------------------------------------------------------------------+
#| Local application imports
#+---------------------------------------------------------------------------+
from netzob.Common.MMSTD.Symbols.AbstractSymbol import AbstractSymbol


#+---------------------------------------------------------------------------+
#| UnknownSymbol:
#|     Definition of an unknwon symbol
#+---------------------------------------------------------------------------+
class UnknownSymbol(AbstractSymbol):

    # Name of the "type" of the symbol
    TYPE = "UnknownSymbol"

    def __init__(self):
        AbstractSymbol.__init__(self, UnknownSymbol.TYPE)
        # create logger with the given configuration
        self.log = logging.getLogger('netzob.Common.MMSTD.Symbols.impl.UnknownSymbol.py')

    def isEquivalent(self, symbol):

        if symbol.__class__.__name__ == UnknownSymbol.__name__:
            self.log.debug("The symbols are equivalents")
            return True
        else:
            self.log.debug("The symbols are not equivalents")
            return False

    def write(self, writingToken):
        """write:
                Returns bitarray('').

                @type writingToken: netzob.Common.MMSTD.Dictionary.VariableProcessingToken.VariableWritingToken.VariableWritingToken
                @param writingToken: a token which contains all critical information on this writing access.
                @rtype: bitarray
                @return: bitarray('').
        """
        return (bitarray(endian='big'), "")

    #+-----------------------------------------------------------------------+
    #| GETTERS AND SETTERS
    #+-----------------------------------------------------------------------+
    def getID(self):
        return "UnknownSymbol"

    def getEntry(self):
        return None

    def getName(self):
        return "UnknownSymbol"

    def __str__(self):
        return "UnknownSymbol"

#    def setID(self, id):
#        self.id = id
#    def setEntry(self, entry):
#        self.entry = entry
