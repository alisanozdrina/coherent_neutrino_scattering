import numpy as np
import sys
import lib.config as config
import logging

logger = logging.getLogger(__name__)


class SpectrumInterpolator:

    def __init__(self, filepath, xname, yname, delimiter=';'):
        self.x, self.y = self._read_plot_to_array(filepath, xname, yname, delimiter)
        self.x_min = self.x.min()
        self.x_max = self.x.max()

        logger.info('File data was read successfully!')

    def interpolate(self, x_value):
        if (x_value < self.x_min) or (x_value > self.x_max):
            logger.debug('Unexpected value for interpolation:')
            return None

        if x_value == self.x[self.x.size - 1]:
            return self.y[self.x.size - 1]

        left_index = self._find_index_of_left_border(x_value)
        y_interpolated = self._interpolate_linear(x_value, left_index)

        return y_interpolated

    def _find_index_of_left_border(self, x_value):
        left_index = 0

        for i in range(self.x.size - 1):
            if x_value < self.x[i+1]:
                left_index = i
                break

        return left_index

    def _interpolate_linear(self, x_value, left_index):
        y = self.y[left_index] + (x_value - self.x[left_index]) * (self.y[left_index + 1] - self.y[left_index]) \
                                 / (self.x[left_index + 1] - self.x[left_index])

        return y

    @staticmethod
    def _read_plot_to_array(filepath, xname, yname, delimiter):
        try:
            file_data = np.genfromtxt(filepath, delimiter=delimiter, names=True)
            return file_data[xname], file_data[yname]

        except Exception as ex:
            logger.error('Errors occurred during reading file: %s' % filepath)
            logger.error('Error: ' + str(ex))
            sys.exit()


