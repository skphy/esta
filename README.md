# esta version 2.9.3

Copyright 2017-2022, 2022-2024 Sonu Kumar


"EStA" software package for analyzing, pre-processing, and post-processing 
data from different software packages such as vasp, quantum-espresso, gaussian, 
grrm, siesta, xtb, and so on. It can automatically generate input files for vasp, 
quantum-espresso, gaussian, xtb, orca, siesta, and other codes as well can do some model calculations. 
It is written in python3, Fortran, and a small part in C. In the future, it will be 
able to perform electronic structure calculations.


Some abilities of the software:
===============================

- automatic input generations for different electronic structure softwares

- output analysis of different file formats such xml, yaml, json, and so on

- vibrational and thermodynamical analysis of atomic and molecular systems

- transition state finding using CI-NEB approach (interfaced with quantum-espresso for the time being!!)

- zone centre phonon calculations based on gradient input (to be expanded to whole zone) 

- model calculations of lattice thermal conductivity (first principles calculation is experimental)

- tight binding calculation of bulk materials

- point group detection (space group detection and other stuff carried out using spglib)

- lattice transformation analysis

- machine learning prediction of important physical property (more to add soon!!)

- easy to use unit conversion routine; axsf, bxsf, cube files .. for visualizations etc

- more routines (interfacing of xTB with GRRM, minimization procedures, Fortran code for calculating static dielectric constant, mode oscillator  strength etc..) are there, but to be added to esta package!!!

# Additional topics:
  - an overview of theoretical results
  - some other notable extensions or dependencies
  - bibliography.





