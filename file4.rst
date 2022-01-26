.. note:: **General package**:
    This package does general work related to files processing, manipulation, and many other
    things to speed up the workflow.

.. include:: esta.general.rst

.. note:: **QE package**:
    This package does processes the Quantum-Espresso files from different calculations, such as scf, relax, 
    vc-relax, or other preprocessing outputs.

    - The note contains all indented body elements.

.. include:: esta.qeBag.rst

.. note:: **VASP package**:
    This package does processing of the VASP sofware output files

.. include:: esta.vaspBag.inout.rst

.. note:: **GRRM package**:
    This package does processing of the GRRM sofware output files

.. include:: esta.grrmBag.rst

.. note:: **POINT GROUP package**:
    This package does point group detection of molecules using C program

.. include:: esta.pointGroup.rst

.. note:: **PHONON package**:
    This package calculates the vibrational frequencies of atomic surfaces, interfaces, or molecules using 
    finite displacement methodology. All the input files are automatically generated from the QE input files. 

.. include:: esta.phonon.rst

.. note:: **TransitionState package**:
    Transition state finding using NEB and CI-NEB method for chemical reactions and diffusion processes.

.. include:: esta.transitionState.rst

.. note:: **surfReact package**:
    Surface reaction tool for finding various atomic structures created using different operations ... more 
    documentation will be added later.

.. include:: esta.surfReact.rst

.. note:: **mlBag package**:
   ML related algorithms are implemented such gaussian kernals, etc. Atomic and other descriptors creation is also 
   possible provided DFT or low level calculation results are available.  Also, various other algorithms are 
   called from the well known package sklearn package. 

.. include:: esta.mlBag.rst
