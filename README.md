# esta version 2.6:
==================

Copyright 2017-2021 Sonu Kumar


"EStA" software package for analyzing, pre-processing, and post-processing 
data from different software packages such as vasp, quantum-espresso, gaussian, 
GRRM, xTB, and so on. It can automatically generate input files for vasp, 
quantum-esspresso, and other codes as well can do some model calculations. 
It is written in python3, Fotran90, and some part in C. In future, it will be 
able to perform electronic structure calculations.


A few additional topics are also covered:

- an overview of theoretical results,
- some other notable extensions,
- bibliography.


Some abilities of the software:
===============================

- automatic input generations for different electronic structure softwares

- output analysis of different file formats such xml, yaml, json, and so on

- vibrational and thermodynamical analysis of atomic and molecular systems

- transition state finding using CI-NEB approach (interfaced with quantum-espresso for the time being!!)

#. zone centre phonon calculations based on gradient input (to be expanded to whole zone) 

#. model calculations of lattice thermal conductivity (first principles calculation is experimental)

#. tight binding calculation of bulk materials

#. point group detection (space group detection and other stuff carried out using spglib)

#. lattice transformation analysis

#. machine learning prediction of important physical property (more to add soon!!)

#. easy to use unit conversion routine; axsf, bxsf, cube files .. for visualizations etc

#. more routines (interfacing of xTB with GRRM, minimization procedures, fortran code for calculating static dielectric constant, mode oscillator  strength etc..) are there, but to be added to esta package!!!




