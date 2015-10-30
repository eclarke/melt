Melt
------------
.. image:: https://travis-ci.org/eclarke/melt.svg?branch=master
    :target: https://travis-ci.org/eclarke/melt
.. image:: https://coveralls.io/repos/eclarke/melt/badge.svg?branch=master&service=github
	:target: https://coveralls.io/github/eclarke/melt?branch=master

A nucleotide sequence melt temp calculator for Python. 

Features:
==========

- Usually within a few tenths of a degree C match to IDT's `OligoAnalyzer <https://www.idtdna.com/calc/analyzer>`_
- Mono- and divalent cation corrections (from https://www.idtdna.com/Calc/Analyzer/Home/Definitions#MeltTemp)
- Accurate nucleotide pair coefficents from Allawi and SantaLucia (1997).

Installation
=============

.. code-block:: bash

	$ pip install melt


## Usage

From the command line:

.. code-block:: bash

	$ Tm ATGCATGC
	44.4
	$ Tm --dna 200 --na 50 --mg 3 --dntp 0.8 ATGCATGC
	26.4


As a library:

.. code-block:: Python

	>>> import melting
	>>> melting.temp("ATGCATGC")
	44.387081560668946
	>>> melting.temp("ATGCATGC", DNA_c=200, Na_c=50, Mg_c=3, dNTPs_c=0.8)
	26.438734864285152


## Acknowledgements

This code is largely built on existing code from:

- Sebastian Bassi (sbassi@genesdigitales.com)
- Greg Singer (singerg@tcd.ie)
- Nicolas Le Novere (lenov@ebi.ac.uk) 

Salt concentration equations adapted from IDT, with work from `Erik Clarke <https://github.com/eclarke>`_, `Sesh Sundararaman <https://github.com/sesh-sas>`_, and `Calvin Morrison <https://github.com/mutantturkey>`_.
