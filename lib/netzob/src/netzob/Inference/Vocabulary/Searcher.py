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

#+----------------------------------------------
#| Global Imports
#+----------------------------------------------
from gettext import gettext as _
import logging
import re

#+----------------------------------------------
#| Local Imports
#+----------------------------------------------
from netzob.Common.Type.TypeConvertor import TypeConvertor
from netzob.Common.Type.TypeIdentifier import TypeIdentifier
from netzob.Common.Type.Format import Format
from netzob.Inference.Vocabulary.SearchResult import SearchResult
from netzob.Inference.Vocabulary.SearchTask import SearchTask


#+----------------------------------------------
#| Searcher:
#|     Provides multiple algorithms for a searching after a pattern in a
#|     set of computed messages
#+----------------------------------------------
class Searcher(object):

    #+----------------------------------------------
    #| Constructor:
    #| @param project : the project where the search will be executed
    #+----------------------------------------------
    def __init__(self, project, status_cb=None):
        # create logger with the given configuration
        self.log = logging.getLogger('netzob.Inference.Vocabulary.Searcher.py')
        self.project = project
        self.status_cb = status_cb

    #+----------------------------------------------
    #| getSearchedDataForBinary:
    #|   Generates data which can represent the specified Binary
    #| @param value the value to search for
    #+----------------------------------------------
    def getSearchedDataForBinary(self, value):
        return []

    #+----------------------------------------------
    #| getSearchedDataForOctal:
    #|   Generates data which can represent the specified Octal
    #| @param value the value to search for
    #+----------------------------------------------
    def getSearchedDataForOctal(self, value):
        return []

    #+----------------------------------------------
    #| getSearchedDataForDecimal:
    #|   Generates data which can represent the specified Decimal
    #| @param value the value to search for
    #+----------------------------------------------
    def getSearchedDataForDecimal(self, value):
        if not value.isdigit():
            return []
        # Creation of a SearchTask
        task = SearchTask(value, value, Format.DECIMAL)
        task.registerVariation(TypeConvertor.decimalToNetzobRaw(value), "Decimal representation of '{0}'".format(TypeConvertor.decimalToNetzobRaw(value)))
        task.registerVariation(TypeConvertor.decimalToNetzobRaw(value[::-1]), "Inverted decimal representation of '{0}'".format(TypeConvertor.decimalToNetzobRaw(value[::-1])))
        return [task]

    #+----------------------------------------------
    #| getSearchedDataForHexadecimal:
    #|   Generates data which can represent the specified Hexa
    #| @param value the value to search for
    #+----------------------------------------------
    def getSearchedDataForHexadecimal(self, value, extraInfo=None):
        typeIdentifier = TypeIdentifier()
        if not typeIdentifier.isHexString(value):
            return []
        # Creation of a SearchTask
        task = SearchTask(value, value, Format.HEX)
        task.registerVariation(value, "Hex repr of '{0}'({1}))".format(value, extraInfo))
#        task.registerVariation(value[::-1], "Inverted representation of '{0}'".format(value[::-1]))
        return [task]

    #+----------------------------------------------
    #| getSearchedDataForString:
    #|   Generates data which can represent the specified string
    #| @param value the value to search for
    #+----------------------------------------------
    def getSearchedDataForString(self, value):
        # Creation of a SearchTask
        task = SearchTask(value, value, Format.STRING)
        task.registerVariation(TypeConvertor.stringToNetzobRaw(value), "String representation of '%s'" % value)
        task.registerVariation(TypeConvertor.stringToNetzobRaw(value[::-1]), "Inverted string representation of '%s'" % value[::-1])
        return [task]

    #+----------------------------------------------
    #| getSearchedDataForIP:
    #|   Generates data which can represent the specified IP
    #| @param value the value to search for
    #+----------------------------------------------
    def getSearchedDataForIP(self, value):
        tasks = []

        ipPattern = "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
        # first verify its a ip format
        if not re.match(ipPattern, value):
            return tasks

        # parse the value to get a, b, c and d
        ipTab = value.split('.')
        a = ipTab[0]
        b = ipTab[1]
        c = ipTab[2]
        d = ipTab[3]

        a2 = a
        if a2 < 100:
            a2 = "0" + a2
        if a2 < 10:
            a2 = "0" + a2
        b2 = b
        if b2 < 100:
            b2 = "0" + b2
        if b2 < 10:
            b2 = "0" + b2
        c2 = c
        if c2 < 100:
            c2 = "0" + c2
        if c2 < 10:
            c2 = "0" + c2
        d2 = d
        if d2 < 100:
            d2 = "0" + d2
        if d2 < 10:
            d2 = "0" + d2

#        # in String :
#        # - 192.168.0.10
#        val = "%s.%s.%s.%s" % (a, b, c, d)
#        tasks.extend(self.getSearchedDataForString(val))
#
#        # - 192.168.000.010
#        val = "%s.%s.%s.%s" % (a2, b2, c2, d2)
#        tasks.extend(self.getSearchedDataForString(val))
#
#        # - 192168000010
#        val = "%s%s%s%s" % (a2, b2, c2, d2)
#        tasks.extend(self.getSearchedDataForString(val))
#
#        # - 10.0.168.192
#        val = "%s.%s.%s.%s" % (d, c, b, a)
#        tasks.extend(self.getSearchedDataForString(val))
#
#        # - 000.010.192.168
#        val = "%s.%s.%s.%s" % (d2, c2, b2, a2)
#        tasks.extend(self.getSearchedDataForString(val))
#
#        # - 0.10.192.168
#        val = "%s.%s.%s.%s" % (c, d, a, b)
#        tasks.extend(self.getSearchedDataForString(val))
#
#        # - 000.010.192.168
#        val = "%s.%s.%s.%s" % (c2, d2, a2, b2)
#        tasks.extend(self.getSearchedDataForString(val))
#
#        # - 000010192168
#        val = "%s%s%s%s" % (c2, d2, a2, b2)
#        tasks.extend(self.getSearchedDataForString(val))

        #in hexadecimal
        ah = hex(int(a))[2:]
        ah = ((2 - len(ah)) * '0') + ah

        bh = hex(int(b))[2:]
        bh = ((2 - len(bh)) * '0') + bh

        ch = hex(int(c))[2:]
        ch = ((2 - len(ch)) * '0') + ch

        dh = hex(int(d))[2:]
        dh = ((2 - len(dh)) * '0') + dh

        val = "{0}{1}{2}{3}".format(ah, bh, ch, dh)
        tasks.extend(self.getSearchedDataForHexadecimal(val, value))

        return tasks

    #+----------------------------------------------
    #| search:
    #|   Search a set of specified data in all the project
    #| @param tasks the set of "search" task
    #+----------------------------------------------
    def search(self, tasks):

        symbols = self.project.getVocabulary().getSymbols()

        # compute the step for status notification
        try:
            step = 100.0 / (len(symbols) * len(tasks))
        except ZeroDivisionError:
            step = 100
        status = 0.0

        for task in tasks:
            if self.status_cb is not None and int(status % 2) == 0:
                    self.status_cb(float(status / 100.0), None)
            for symbol in symbols:
                for message in symbol.getMessages():
                    variations = task.getVariations()
                    for variation_value in variations.keys():
                        task.registerResults(self.extendedSearch(variation_value, message), variations[variation_value])
                status += step

        return tasks

    #+----------------------------------------------
    #| searchInSymbol:
    #|   Search a set of specified data in a the specified symbol
    #| @param tasks the set of "search" task
    #| @param symbol the symbol to search in
    #+----------------------------------------------
    def searchInSymbol(self, tasks, symbol):
        for task in tasks:
            for message in symbol.getMessages():
                variations = task.getVariations()
                for variation_value in variations.keys():
                    task.registerResults(self.extendedSearch(variation_value, message), variations[variation_value])
        return tasks

    #+----------------------------------------------
    #| searchInMessage:
    #|   Search a set of specified data in a the specified message
    #| @param tasks the set of "search" task
    #| @param message the message to search in
    #+----------------------------------------------
    def searchInMessage(self, tasks, message):
        for task in tasks:
            variations = task.getVariations()
            for variation_value in variations.keys():
                task.registerResults(self.extendedSearch(variation_value, message), variations[variation_value])
        return tasks

    #+----------------------------------------------
    #| extendedSearch:
    #|   Search for a data in a specified message
    #+----------------------------------------------
    def extendedSearch(self, data, message):
        results = []
        results.extend(self.naturalSearch(data, message))
#        results.extend(self.inversedSearch(data, message))
#        results.extend(self.semiInvertedOnNaturalSearch(data, message))
#        results.extend(self.semiInvertedOnInvertedSearch(data, message))
        return results

    def naturalSearch(self, data, message):
        results = []
        self.log.debug("Natural search of {0} in {1}".format(data, message.getStringData()))
        # Search naturally all the possible places of data in message
        indice = 0
        messageData = message.getStringData()
        indice = messageData.find(data, 0)
        while indice >= 0:
            searchResult = SearchResult(message, "Natural search")
            searchResult.addSegment(indice, len(data))
            results.append(searchResult)
            indice = messageData.find(data, indice + 1)

        return results

    def inversedSearch(self, data, message):
        results = []
        invData = data[::-1]

        # Search naturally all the possible places of data in message
        indice = 0
        while indice + len(invData) <= len(message.getStringData()):
            if message.getStringData()[indice:len(invData) + indice] == invData:
                # We have a match
                searchResult = SearchResult(message, "Inverted search")
                searchResult.addSegment(indice, len(invData))
                results.append(searchResult)
            indice = indice + 1

        return results

    def semiInvertedOnNaturalSearch(self, data, message):
        results = []
        invData = ""
        for i in range(0, len(data), 2):
            if len(data) > i + 1:
                invData = invData + data[i + 1]
            invData = invData + data[i]

        if len(data) % 2 == 1:
            invData = invData + data[-1]

        # Search naturally all the possible places of data in message
        indice = 0
        while indice + len(invData) <= len(message.getStringData()):
            if message.getStringData()[indice:len(invData) + indice] == invData:
                # We have a match
                searchResult = SearchResult(message, "4bytes inverted on natural search")
                searchResult.addSegment(indice, len(invData))
                results.append(searchResult)
            indice = indice + 1

        return results

    def semiInvertedOnInvertedSearch(self, data, message):

        results = []
        tmpData = data[::-1]
        invData = ""
        for i in range(0, len(tmpData), 2):
            if len(data) > i + 1:
                invData = invData + tmpData[i + 1]
            invData = invData + tmpData[i]

        if len(tmpData) % 2 == 1:
            invData = invData + tmpData[-1]

        # Search naturally all the possible places of data in message
        indice = 0
        while indice + len(invData) <= len(message.getStringData()):
            if message.getStringData()[indice:len(invData) + indice] == invData:
                # We have a match
                searchResult = SearchResult(message, "4bytes inverted on inverted search")
                searchResult.addSegment(indice, len(invData))
                results.append(searchResult)
            indice = indice + 1

        return results
