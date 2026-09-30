import os

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
