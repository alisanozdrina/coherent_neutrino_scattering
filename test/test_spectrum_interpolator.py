import pytest

from src.SpectrumInterpolator import SpectrumInterpolator


mock_spectrum = SpectrumInterpolator('./data/mock_reactor_neutrino_spectrum.csv', 'E', 'dN_dE')


class TestSpectrumInterpolator:

    def test_left_boundary_value(self):
        y = mock_spectrum.interpolate(1)
        assert y == 1.

    def test_right_boundary_value(self):
        y = mock_spectrum.interpolate(6)
        assert y == 36.

    def test_random_value(self):
        y = mock_spectrum.interpolate(3.5)
        assert y == 12.5

    def test_value_outer_range(self):
        y = mock_spectrum.interpolate(12)
        assert y is None

    def test_inizialization_fail(self):
        with pytest.raises(SystemExit):
            SpectrumInterpolator('./data/mock_reactor_neutrino_spectrum.csv', 'WrongX', 'dN_dE')
