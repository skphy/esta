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

**Electronic Structure Automater** (**EStA**) aka pytware for preprocessing, post-processing, and analyzing the electronic structure of materials and molecules. 

**EStA** software package is capable of analyzing, pre-processing, and post-processing data from different software packages such as vasp, quantum-espresso, gaussian, GRRM, xTB, siesta, and so on. It can automatically generate input files for vasp, quantum-esspresso, GRRM, gaussian and other codes as well can do some model calculations. It is written in python3, modern Fotran, and some part in C. In future, it will be able to perform calculations for predicting electronic and transport properties.


Features
--------

    *    automatic input generations for different electronic structure softwares

    *    output analysis of different file formats such xml, yaml, json, and so on

    *    vibrational and thermodynamical analysis of atomic and molecular systems

    *    transition state finding using CI-NEB approach (interfaced with quantum-espresso for the time being!!)

    *    zone centre phonon calculations based on gradient input as implemented in phonon directory (to be expanded to whole zone)

    *    model calculations of lattice thermal conductivity (first principles calculation is experimental)

    *    tight binding calculation of bulk materials

    *    point group detection (space group detection and other stuff carried out using spglib)

    *    lattice transformation analysis   

    *    machine learning prediction of *important* physical property (more to add soon!!)

    *    easy to use unit conversion  routine; axsf, bxsf, cube files .. for visualizations etc

    *    reading force constants from phonopy calculations at gamma or any other q-point and finding the force-constants ( :math:`\phi_{i,j})` between all pair of atoms or specific atom pairs along with respective distances; further exploration of stretching and bending force constants (:math:`\phi_{stretch}` and :math:`\phi_{bend}`)

    *    Infra-red and Raman-intensity calculations for periodic systems (automatically generates the needed files to compute the :math:`\epsilon_{\infty}`)

    *    Manipulation of atomic and crystal structures such as atomic substitution, deletion, extension, modulation, and inversion, etc.

    *    more routines (interfacing of xTB with GRRM, minimization procedures, fortran code for calculating static dielectric constant, mode oscillator strength etc..)  are there, but to be added to esta package!!!


Author's research areas
------------------------

**thermoelectrics, heterogeneous catalysis, homogeneous catalysis, defects, phonons, and  machine learning**

.. toctree::
   :maxdepth: 4
   :caption: EStA:
   
   file1
   file2
   file3

.. toctree::
   :maxdepth: 4
   :caption: PACKAGES:

   file4  
   file4.1
   file4.2
   file4.3
   file4.4
   file4.5
   file4.6


.. toctree::
   :maxdepth: 4
   :caption: examples:

   file_example


.. toctree::
   :maxdepth: 4
   :caption: Additional:

   file3a
 
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
