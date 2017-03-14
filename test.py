from SpectrumInterpolator import SpectrumInterpolator

mockSpectrum = SpectrumInterpolator('./data/mock_reactor_neutrino_spectrum.csv', 'E', 'dN_dE')

y = mockSpectrum.interpolate(4.2)
print(y)
