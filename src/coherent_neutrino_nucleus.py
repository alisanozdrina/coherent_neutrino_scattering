import math
from src.phys_constants import *


def total_cross_section(Z, N, nu_energy):

    """

    neutrino + nucleus --> neutrino + nucleus

    :param Z: number of protons in nucleus
    :param N: number of neutron in nucleus
    :param nu_energy: initial neutrino energy in MeV

    :return: total cross section of the process. See "Sterile neutrinos, coherent scattering, and oscillometry measurements
    with low-temperature bolometers" by Joseph A. Formaggio and etc (PHYSICAL REVIEW D 85, 013009 (2012))

    """

    Q_weak = weak_charge(Z, N)
    cross_section = (G_FERMI * Q_weak * nu_energy)**2 / (4 * math.pi)

    return cross_section


def differential_cross_section_for_nucleus_kinetic(Z, N, nucleus_m, nu_energy, nucleus_kin):

    """

    neutrino + nucleus --> neutrino + nucleus

    :param Z: number of protons in nucleus
    :param N: number of neutron in nucleus
    :param nucleus_m: nucleus mass
    :param nu_energy: initial neutrino energy in MeV
    :param nucleus_kin: kinetic energy of the recoiling nucleus
    :return: differential cross section for kinetic energy of the recoil nucleus (PHYSICAL REVIEW D 85, 013009 (2012)
    """

    Q_weak = weak_charge(Z, N)
    differential_cs = G_FERMI**2 / (4 * math.pi) * Q_weak**2 * nucleus_m * (1 - (nucleus_m * nucleus_kin) / (2 * nu_energy**2))

    return differential_cs


def max_kinetic_recoil_nucleus(nucleus_m, nu_energy):

    """
    :param nucleus_m: nucleus mass
    :param nu_energy: initial neutrino energy in MeV
    :return: The maximum kinetic energy of the recoil nucleus
    """
    max_kinetic = nu_energy / (1 + (nucleus_m / (2 * nu_energy)))
    return max_kinetic


def min_energy_neutrino_produce_recoil_nucleus(nucleus_m, kinetic_nucleus):
    """
    Inverse function to `max_kinetic_recoil_nucleus`
    :param nucleus_m: nucleus mass
    :param kinetic_nucleus: kinetic energy of the recoil nucleus
    :return: minimal neutrino energy needed to produce recoil nucleus with kinetic equals to `kinetic_nucleus`
    """
    nu_energy = 0.5 * (kinetic_nucleus + math.sqrt(kinetic_nucleus**2 + 2 * kinetic_nucleus * nucleus_m))
    return nu_energy


def weak_charge(Z, N):

    """
    :param Z: number of protons in nucleus
    :param N: number of neutron in nucleus
    :return: weak charge
    """

    return N - Z * (1 - 4 * MIXING_ANGLE)
