import shlex
import pytest
import melting

def within_margin(given, expected, margin=0.4):
    """
    Returns True if the given value is within +/- the margin of the 
    expected value.
    """
    return expected - margin <= given <= expected + margin

def test_melting():
    # Temps taken from https://www.idtdna.com/calc/analyzer
    # on 2015-10-29 using qPCR parameters:
    # - Oligo Conc: 0.2 uM
    # - Na+ Conc: 50mM
    # - Mg++ Conc: 3mM
    # - dNTPs Conc: 0.8mM
    idt_temps = {
        "ATGCATGC": 26.2,
        "CCCCTTTT": 21.7,
        "GCGCGCGCGCGCGCGC": 76.6,
    }

    for seq, expected_tm in idt_temps.items():
        given_tm = melting.temp(seq, DNA_c=200, Na_c=50, Mg_c=3, dNTPs_c=0.8)
        assert within_margin(given_tm, expected_tm)

def test_uncorrected_tm():
    corrected = melting.temp("ATGCATGC")
    uncorrected = melting.temp("ATGCATGC", uncorrected=True)
    assert corrected != uncorrected

def test_low_cation_ratio():
    expected_tm = 82.2
    given_tm = melting.temp("GCGCGCGCGCGCGCGC", DNA_c=200, Na_c=500, Mg_c=3, dNTPs_c=0.8)
    assert within_margin(given_tm, expected_tm, margin=1)

def test_invalid_nucleotide_seq():
    assert melting.nucleotide_sequence("ATGCATGC")
    with pytest.raises(ValueError):
        melting.nucleotide_sequence("ABCDEFG")

def test_cli(capsys):
    argv = shlex.split("--dna=200 --na=50 --mg=3 --dntp=0.8 ATGCATGC")
    melting.main(argv)
    out, _ = capsys.readouterr()
    out_float = float(out.strip())
    assert within_margin(out_float, 26.2)

