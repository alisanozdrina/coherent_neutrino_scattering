import numpy

import lib.phys_constants as phys

E_NU_AVERAGE = 12  # MeV
E_NU_TOTAL = 5 * 10**52 * phys.MeV_IN_ERG  # MeV
SUPERNOVA_DISTANCE = 10 * 10**3 * phys.METERS_IN_PARSEC  # kpc


def single_neutrino_flux(nu_energy, average_nu_energy=E_NU_AVERAGE, total_nu_energy=E_NU_TOTAL, distance=SUPERNOVA_DISTANCE):
    """
    The time-integrated flux for single neutrino flavor
    See "Gadolinium in Water Cherenkov Detectors Improves Detection of Supernova νe" by Ranjan Laha and John F. Beacom

    :param nu_energy: neutrino energy in MeV
    :param average_nu_energy: neutrino average energy in the explosion
    :param total_nu_energy: total neutrino energy in that ν flavor in the explosion
    :param distance: distance to the supernova

    :return: the time-integrated flux for a single neutrino flavor
    """
    return 1. / (4 * numpy.pi * distance**2) * total_nu_energy / average_nu_energy \
           * _maxwell_boltzmann_supernova_spectrum(nu_energy, average_nu_energy)


def _maxwell_boltzmann_supernova_spectrum(nu_energy, average_nu_energy):
    """
    Modified Maxwell-Boltzmann spectrum
    See "Gadolinium in Water Cherenkov Detectors Improves Detection of Supernova νe" by Ranjan Laha and John F. Beacom

    :param nu_energy: neutrino energy in MeV
    :param average_nu_energy: neutrino average energy in the explosion

    :return: Maxwell-Boltzmann spectrum
    """
    return 128. / 3. * nu_energy**3 / average_nu_energy**4 * numpy.exp(-4 * nu_energy / average_nu_energy)
