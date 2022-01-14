import unittest

import numpy as np

from pqueens.interfaces.direct_python_interface import DirectPythonInterface
from pqueens.iterators.elementary_effects_iterator import ElementaryEffectsIterator
from pqueens.models.simulation_model import SimulationModel
from pqueens.variables.variables import Variables


class TestElementaryEffectsIshigami(unittest.TestCase):
    def setUp(self):

        uncertain_parameter = {
            "type": "FLOAT",
            "size": 1,
            "max": 3.14159265359,
            "min": -3.14159265359,
        }

        random_variables = {
            'x1': uncertain_parameter,
            'x2': uncertain_parameter,
            'x3': uncertain_parameter,
        }

        uncertain_parameters = {"random_variables": random_variables}
        some_settings = {"experiment_name": "test"}

        self.variables = Variables.from_uncertain_parameters_create(uncertain_parameters)
        self.interface = DirectPythonInterface('test_interface', 'ishigami.py', self.variables)

        # create mock model
        self.model = SimulationModel("my_model", self.interface, uncertain_parameters)

        self.my_iterator = ElementaryEffectsIterator(
            self.model,
            num_trajectories=20,
            local_optimization=True,
            num_optimal_trajectories=4,
            num_levels=4,
            seed=42,
            confidence_level=0.95,
            num_bootstrap_samples=1000,
            result_description={},
            global_settings=some_settings,
        )

    def test_correct_sampling(self):
        """Test if sampling works correctly."""
        self.my_iterator.pre_run()

        ref_vals = np.array(
            [
                [-1.04719755, 3.14159265, 3.14159265],
                [3.14159265, 3.14159265, 3.14159265],
                [3.14159265, 3.14159265, -1.04719755],
                [3.14159265, -1.04719755, -1.04719755],
                [-3.14159265, -1.04719755, -3.14159265],
                [-3.14159265, 3.14159265, -3.14159265],
                [-3.14159265, 3.14159265, 1.04719755],
                [1.04719755, 3.14159265, 1.04719755],
                [-3.14159265, -3.14159265, 1.04719755],
                [-3.14159265, -3.14159265, -3.14159265],
                [-3.14159265, 1.04719755, -3.14159265],
                [1.04719755, 1.04719755, -3.14159265],
                [3.14159265, 1.04719755, 3.14159265],
                [3.14159265, -3.14159265, 3.14159265],
                [-1.04719755, -3.14159265, 3.14159265],
                [-1.04719755, -3.14159265, -1.04719755],
            ]
        )

        np.testing.assert_allclose(self.my_iterator.samples, ref_vals, 1e-07, 1e-07)

    def test_correct_sensitivity_indices(self):
        """Test correct results."""
        self.my_iterator.pre_run()
        self.my_iterator.core_run()
        si = self.my_iterator.si

        ref_mu = np.array([10.82845216, 0.0, -3.12439805])
        ref_mu_star = np.array([10.82845216, 7.87500000, 3.12439805])
        ref_mu_star_conf = np.array([5.49677290, 0.0, 5.26474752])
        ref_sigma = np.array([6.24879610, 9.09326673, 6.24879610])

        np.testing.assert_allclose(si['mu'], ref_mu, 1e-07, 1e-07)
        np.testing.assert_allclose(si['mu_star'], ref_mu_star, 1e-07, 1e-07)
        np.testing.assert_allclose(si['mu_star_conf'], ref_mu_star_conf, 1e-07, 1e-07)
        np.testing.assert_allclose(si['sigma'], ref_sigma, 1e-07, 1e-07)
