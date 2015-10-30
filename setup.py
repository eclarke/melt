from setuptools import setup

VERSION = open('VERSION').read().strip()

setup(
    name="melting",
    py_modules=['melting'],
    version=VERSION,
    author='Erik Clarke',
    author_email='ecl@mail.med.upenn.edu',
    url='https://github.com/eclarke/melt',
    description='A nucleotide melt temp calculator',
    long_description=(
        "A nucleotide sequence melt temp calculator for Python, with "
        "adjustments for monovalent and divalent ion concentrations."),
    classifiers=[
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ],
    entry_points={'console_scripts': ['Tm = melting:main']}
)
