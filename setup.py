from setuptools import setup

with open("VERSION") as version_file:
    VERSION = version_file.read().strip()

setup(
    name="melt",
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
