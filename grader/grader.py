"""Problem grader."""

import copy
from base import BaseGrader # pylint: disable=E0611

class Grader(BaseGrader):
    """Problem grader."""

    evaluation_function_name = 'duplicate_zeros'
    test_cases_file = 'grader/test_cases.txt'
#
    def eval_solution(self, test_case) -> bool:
        """Evaluates solution against the given test case."""
        transit_arr, want = test_case
        input_data = copy.copy(transit_arr)
        self.f(transit_arr)
        results_differ = transit_arr != want
        if results_differ:
            self.log_execution_results(transit_arr, (input_data, want), failed=True)
        return results_differ

    def get_test_cases(self):
        """Load and return the test cases."""
        base = [
            ([1], [1]),
            ([0], [0]),
            ([0, 1], [0, 0]),
            ([1, 0], [1, 0]),
            ([0, 1, 0], [0, 0, 1]),
            ([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]),
            ([1, 2, 3], [1, 2, 3]),
            ([1, 0, 0, 0, 0], [1, 0, 0, 0, 0]),
            ([0, 0, 0, 0, 1], [0, 0, 0, 0, 0]),
            ([1, 2, 0, 0, 3, 4, 5, 6, 7, 8], [1, 2, 0, 0, 0, 0, 3, 4, 5, 6]),
        ]
        with open(self.test_cases_file, 'r') as test_cases_file:
            test_cases = test_cases_file.readlines()
            for test in test_cases:
                input_data, output = test.split("|")
                input_data = [int(x) for x in input_data.split(",")]
                output = [int(x) for x in output.split(",")]
                base.append((input_data, output))
        return base
        