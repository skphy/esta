.. EStA documentation master file, created by
   sphinx-quickstart on Fri Jun  4 13:18:44 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: esta_logo_general1_1.png
   :height: 450 px
   :width: 903 px
   :scale: 30 %
   :alt: esta
   :align: center

EStA documentation!
================================

**Electronic Structure Analyzer** (**EStA**) aka pytware for analyzing and calculating to some extent the electronic structure of materials and molecules.

**EStA** software package is capable of analyzing, pre-processing, and post-processing data from different software packages such as vasp, quantum-espresso, gaussian, GRRM, xTB, and so on. It can automatically generate input files for vasp, quantum-esspresso, and other codes as well can do some model calculations. It is written in python3, Fotran90, and some part in C. In future, it will be able to perform calculations for predicting electronic and transport properties.


Some abilities of the code
--------------------------

    #.    automatic input generations for different electronic structure softwares

    #.    output analysis of different file formats such xml, yaml, json, and so on

    #.    vibrational and thermodynamical analysis of atomic and molecular systems

    #.    transition state finding using CI-NEB approach (interfaced with quantum-espresso for the time being!!)

    #.    zone centre phonon calculations based on gradient input (to be expanded to whole zone)

    #.    model calculations of lattice thermal conductivity (first principles calculation is experimental)

    #.    tight binding calculation of bulk materials

    #.    point group detection (space group detection and other stuff carried out using spglib)

    #.    lattice transformation analysis   

    #.    machine learning prediction of *important* physical property (more to add soon!!)

    #.    easy to use unit conversion  routine; axsf, bxsf, cube files .. for visualizations etc

    #.    more routines (interfacing of xTB with GRRM, minimization procedures, fortran code for calculating static dielectric constant, mode oscillator strength etc..)  are there, but to be added to esta package!!!


Link to my website at google site: `google site home page`_ 

.. _`google site home page`:  https://sites.google.com/view/1009ukumars

Keyword related to author's research areas
------------------------------------------

**thermoelectrics, heterogeneous catalysis, homogeneous catalysis, defects, phonons, and  machine learning**

.. toctree::
   :maxdepth: 4
   :caption: EStA1:

   file1
   file2
   file3

.. toctree::
   :maxdepth: 4
   :caption: EStA2:

   file4 

.. toctree::
   :maxdepth: 4
   :caption: Additional:

   file3a
 
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
