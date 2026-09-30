import os

import numpy as np
import pandas as pd
from zen_garden import Results, run

from tests.end_to_end.utils.test_helpers import (
    compare_variables_results,
)


# All the tests
###############
def test_1a(fixtures_path, capsys):
    # add duals for this test

    # test also whether config and dataset can take just file name in cwd
    cwd = os.getcwd()
    os.chdir(fixtures_path)
    try:
        # run the test
        data_set_name = "test_1a"
        run(
            config="config_duals.yaml",
            dataset=data_set_name,
        )

        # read the results and check again
        res = Results(os.path.join("outputs", data_set_name))
        compare_variables_results(
            data_set_name, res, fixtures_path, "test_variables.yaml"
        )

        output = capsys.readouterr().out
        assert "[Plugin Template] Example setting: set_value" in output
        assert "[Plugin Template] Example number: 42" in output
        assert "[Plugin Template] Plugin loaded successfully!" in output
    finally:
        os.chdir(cwd)


def test_plugin_template_add_new_constraint(fixtures_path):
    """Test that the node-indexed variable equals the input parameter."""
    data_set_name = "test_1a"
    run(
        config=os.path.join(
            fixtures_path, "config_plugin_template_add_new_constraint.yaml"
        ),
        dataset=os.path.join(fixtures_path, data_set_name),
    )

    results = Results(os.path.join(fixtures_path, "outputs", data_set_name))
    new_variable = results.get_unprocessed_result("new_variable")
    parameter_input = pd.read_csv(
        os.path.join(
            fixtures_path, data_set_name, "energy_system", "new_parameter.csv"
        ),
        index_col="node",
    )["new_parameter"]

    assert new_variable.index.name == "node"
    assert set(new_variable.index) == set(parameter_input.index)
    assert np.allclose(new_variable.sort_index(), parameter_input.sort_index())
