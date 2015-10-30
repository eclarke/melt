from setuptools import setup

VERSION = open('VERSION').read().strip()

setup(
    name="melt",
    py_modules=['melting'],
    version=VERSION,
    author='Erik Clarke',
    author_email='ecl@mail.med.upenn.edu',
    url='https://github.com/eclarke/melt',
    description='A nucleotide melt temp calculator',
    long_description=open('README.rst').read(),
    classifiers=[
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License (GPL)'
    ],
    license='GPL 3',
    entry_points={'console_scripts': ['Tm = melting:main']}
)
