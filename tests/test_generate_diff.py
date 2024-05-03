import pytest

from gendiff import generate_diff
import os


def form_path_to_test_file(file_name):
    fixtures_path = os.path.join(
        os.path.dirname(__file__),
        'fixtures'
    )
    return os.path.join(
        fixtures_path,
        file_name
    )


@pytest.mark.parametrize(
    'nested1,'
    'nested2,'
    'actual_format,'
    'expected_format',
    [('nested1.json',
      'nested2.json',
      'stylish',
      'correct_nested_stylish'),
     ('nested1.json',
      'nested2.yml',
      'plain',
      'correct_nested_plain'),
     ('nested1.yaml',
      'nested2.yml',
      'json',
      'correct_nested_raw_json')]
)
def test_generating_correct_diff(nested1,
                                 nested2,
                                 actual_format,
                                 expected_format):
    diff = generate_diff(
        form_path_to_test_file(nested1),
        form_path_to_test_file(nested2),
        actual_format
    )

    with open(form_path_to_test_file(expected_format), 'r') as file:
        correct_structure = file.read()

        assert diff == correct_structure
