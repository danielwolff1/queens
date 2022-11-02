import os
import pickle
from pathlib import Path

import pytest

from pqueens import run


def test_branin_monte_carlo(inputdir, tmpdir):
    """Test case for monte carlo iterator."""
    run(Path(Path(inputdir, 'monte_carlo_branin.json')), Path(tmpdir))

    result_file = str(tmpdir) + '/' + 'xxx.pickle'
    with open(result_file, 'rb') as handle:
        results = pickle.load(handle)
    assert results["mean"] == pytest.approx(55.81419875080866)
    assert results["var"] == pytest.approx(2754.1188056842070)
