import numpy


def total_antineutrino_flux(reactor_power, isotopes, nu_energy_range):
    """

    :param reactor_power: well... reactor power
    :param isotopes: array of the isotope's info as python dict:
    {
        'FISSION_FRACTION': ..(constant for reactor),
        'FISSION_ENERGY': ..(constant for isotope),
        'ENERGY_SPECTRUM': function_to_calculate_isotope_antinu_spectrum
     }
    :param nu_energy_range: set of antinu energy
    :return: total reactor antineutrino flux
    """
    released_energy = 0.
    for isotope in isotopes:
        released_energy += isotope['FISSION_FRACTION'] * isotope['FISSION_ENERGY']

    total_flux = []
    for nu_energy in nu_energy_range:

        probability = 0
        for isotope in isotopes:
            isotope_probability = isotope['ENERGY_SPECTRUM'](nu_energy) or 0.0
            probability += isotope['FISSION_FRACTION'] * isotope_probability

        probability *= (reactor_power / released_energy)
        total_flux.append(probability)

    return numpy.array(total_flux)
