#!/usr/bin/python

import math
import os

import inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy_Draw as inkDraw
from drawRIComponents import component
from drawRICompressors import compressor
from drawRIPumps import pump

# some symbol definition

OhmChar = u'\u2126'.encode('utf-8')


# package needed:  steinmetz

def latexUnitMultiple(valueString):
    if valueString[-1] == 'M':
        return valueString.replace('M', r'\si\mega')

    if valueString[-1] == 'k':
        return valueString.replace('k', r'\si\kilo')

    if valueString[-1] == 'm':
        return valueString.replace('m', r'\si\milli')

    if valueString[-1] == 'u':
        return valueString.replace('u', r'\micro')

    if valueString[-1] == 'n':
        return valueString.replace('n', r'\si\nano')

    if valueString[-1] == 'p':
        return valueString.replace('p', r'\si\pico')

    return valueString


# ---------------------------------------------
class RISymbols(pump, compressor):
    def __init__(self):
        inkBase.inkscapeMadeEasy.__init__(self)

        self.OptionParser.add_option("--tab", action="store", type="string", dest="tab", default="object")

        self.OptionParser.add_option("--pump", action="store", type="string", dest="pump", default='Default')
        self.OptionParser.add_option("--pumpLabel", action="store", type="string", dest="pumpLabel", default='Pump')
        self.OptionParser.add_option("--pumpRot", action="store", type="string", dest="pumpRot", default='0')
        self.OptionParser.add_option("--pumpDirection", action="store", type="string", dest="pumpDirection", default='right')

        self.OptionParser.add_option("--compressor", action="store", type="string", dest="compressor", default='Default')
        self.OptionParser.add_option("--compressorLabel", action="store", type="string", dest="compressorLabel", default='Compressor')
        self.OptionParser.add_option("--compressorRot", action="store", type="string", dest="compressorRot", default='0')
        self.OptionParser.add_option("--compressorDirection", action="store", type="string", dest="compressorDirection", default='right')

        self.OptionParser.add_option("--currColor", action="store", type="string", dest="currColor", default='#FF0000')
        self.OptionParser.add_option("--colorPickerCurrent", action="store", type="string", dest="colorPickerCurrent", default='0')

    def effect(self):

        so = self.options
        so.tab = so.tab.replace('"', '')  # removes de exceeding double quotes from the string

        # latex related preamble
        self.preambleFile = os.getcwd() + '/textextLib/RISymbolsLatexPreamble.tex'

        # root_layer = self.current_layer
        root_layer = self.document.getroot()
        # root_layer = self.getcurrentLayer()

        # text size and font style
        self.fontSize = 5
        self.fontSizeSmall = 4

        # offset between symbol and text
        self.textOffset = self.fontSize
        # offset between symbol and text
        self.textOffsetSmall = self.fontSizeSmall / 2
        self.textStyle = inkDraw.textStyle.set(
            fontSize=self.fontSize, justification='center',
            fontFamily='Carlito'
        )
        self.textStyleSmall = inkDraw.textStyle.set(
            fontSize=self.fontSizeSmall, justification='center',
            fontFamily='Carlito'
        )

        # sets the position to the viewport center, round to next 10.
        position = [self.view_center[0], self.view_center[1]]
        position[0] = int(math.ceil(position[0] / 10.0)) * 10
        position[1] = int(math.ceil(position[1] / 10.0)) * 10

        [self.currentColor, alpha] = inkDraw.color.parseColorPicker(
            so.currColor, so.colorPickerCurrent
        )

        so.pumpRot = float(so.pumpRot)
        so.compressorRot = float(so.compressorRot)

        self.setDimensions()

        if so.tab == 'pump':
            self.drawPump(
                root_layer, position, label=so.pumpLabel,
                direction=so.pumpDirection, angleDeg=so.pumpRot,
                pumpType=so.pump
            )

        elif so.tab == 'compressor':
            self.drawCompressor(
                root_layer, position, label=so.compressorLabel,
                direction=so.compressorDirection, angleDeg=so.compressorRot,
                compressorType=so.compressor
            )


if __name__ == '__main__':
    ri = RISymbols()
    ri.affect()
