import math
from src.phys_constants import *


def total_coherent_neutrino_nucleus(Z, N, nu_energy):

    """

    neutrino + nucleus --> neutrino + nucleus

    :param Z: number of protons in nucleus
    :param N: number of neutron in nucleus
    :param nu_energy: initial neutrino energy in MeV

    :return: total cross section of the process. See "Sterile neutrinos, coherent scattering, and oscillometry measurements
    with low-temperature bolometers" by Joseph A. Formaggio and etc (PHYSICAL REVIEW D 85, 013009 (2012))

    """

    weak_charge = N - Z * (1 - 4 * MIXING_ANGLE)
    cross_section = (G_FERMI * weak_charge * nu_energy)**2 / (4 * math.pi)

    return cross_section
