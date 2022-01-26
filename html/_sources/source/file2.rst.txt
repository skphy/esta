EStA subfolders
===============

.. code-block:: rst

    EStA contains various software preprocessing and postprocessing routines to make 
    tasks easily and automated to some extents. 

    The main class is `aadhaar` class to handle atomic structure information i.e. atomic positions, atomic 
    symbols, cell parameters. It can handle both molecules and periodic systems. Molecules are handled 
    using xyz file format and periodic systems are handled using POSCAR file format. These formats can 
    be further suited to other file format,

    Various Bags are present in the EStA folder to handle software specific data such as `vaspBag`, `qeBag`, 
    `siestaBag`, `grrmBag`, `xtbBag`, and so on.

    Thermodynamics can be calculated based on the vibrational calculation implemented in the `qeBag`. Similarly
    transition state analysis is possible using routines in the `transitionState`.

    There are lots of routines some written in fortran to be interfaced with `EStA` package. Machine learning 
    algorithms are also implemented such as GPR based on gaussian processes in the `mlBag`.





