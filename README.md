# RISymbols
Inkscape extension to assist creating R+I symbols. This package has been created on basis of the <https://github.com/fsmMLK/inkscapeCircuitSymbols> extension.

# Installation and requirements

This extension was partially developed in Inkscape 0.48 and partially in 0.91 in Linux (Kubuntu 12.04 and 14.04). It should work on both versions of Inkscape. Also, they should work in different OSs too as long as all requirements are installed.

This extension requires another extension to run, inkscapeMadeEasy <https://github.com/fsmMLK/inkscapeMadeEasy>, which contains several backstage methods and classes.

In order to use circuitSymbols extension, you must also download inkscapeMadeEasy files and put them inside Inkscape's extension directory. Please refer to inkscapeMadeEasy installation instructions. In the end you must have the following files and directories in your Inkscape extension directory.

```
inkscape/extensions/
            |-- inkscapeMadeEasy_Base.py
            |-- inkscapeMadeEasy_Draw.py
            |-- inkscapeMadeEasy_Plot.py
            |-- textextLib
            |   |-- __init__.py
            |   |-- basicLatexPackages.tex
            |   |-- CircuitSymbolsLatexPreamble.tex      <-- add this file to  textextLib  subdirectoy
            |   |-- textext.inx
            |   |-- textext.py
            |
            |-- circuitSymbols.py
            |-- circuitSymbols.py
            |-- drawAmpOp.py
            |-- drawArrows.py
            |-- drawDiodes.py
            |-- drawRLC.py
            |-- drawSignals.py
            |-- drawSources.py
            |-- drawSwitches.py
            |-- drawTransistors.py
            |-- circuitSymbols_semiconductors.inx
            `-- circuitSymbols_general.inx
```

**LaTeX package requirement**

If LaTeX support is enables (see below), you will need in your system the following packages: amsmath, amsthm, amsbsy, amsfonts, amssymb, siunitx, steinmetz


**Disabling LaTeX support of inkscapeMadeEasy**

Many of the methods implemented in inkscapeMadeEasy project use LaTeX to generate text. To this end I decided to employ the excellent extension **textext** from Pauli Virtanen  <https://pav.iki.fi/software/textext/>. 

LaTeX support via textext extension requires LaTeX typesetting system in your computer (it's free and awesome! =] ).

Since many people don't use LaTeX and/or don't have it installed, inkscapeMadeEasy's LaTeX support is now optional. **By default, LaTeX support is ENABLED.**

Please refer to <https://fsmmlk.github.io/inkscapeMadeEasy/#installation-and-requirements> on how to easily disable LaTeX support.


# Usage

## GENERAL menu entry

### Some tab

### Color tab

# Observations

 - The objects will be created at the center of your screen.
    
# Examples

