import pytest

from gendiff import generate_diff
import os


def form_path_to_test_file(file):
    return os.path.abspath(
        f'fixtures/{file}'
    )


@pytest.mark.parametrize(
    'nested1,'
    'nested2,'
    'stylish_format,'
    'correct_nested_stylish',
    [('nested1.json',
      'nested2.json',
      'stylish',
      'correct_nested_stylish'),
     ('nested1.json',
      'nested2.yml',
      'stylish',
      'correct_nested_stylish'),
     ('nested1.yaml',
      'nested2.yml',
      'stylish',
      'correct_nested_stylish')]
)
def test_generating_nested_stylish_diff(nested1,
                                        nested2,
                                        stylish_format,
                                        correct_nested_stylish):
    diff = generate_diff(
        form_path_to_test_file(nested1),
        form_path_to_test_file(nested2),
        stylish_format
    )

    with open(form_path_to_test_file(correct_nested_stylish), 'r') as file:
        correct_structure = file.read()

        assert diff == correct_structure


@pytest.mark.parametrize(
    'nested1,'
    'nested2,'
    'plain_format,'
    'correct_nested_plain',
    [('nested1.json',
      'nested2.json',
      'plain',
      'correct_nested_plain'),
     ('nested1.json',
      'nested2.yml',
      'plain',
      'correct_nested_plain'),
     ('nested1.yaml',
      'nested2.yml',
      'plain',
      'correct_nested_plain')]
)
def test_generating_nested_plain_diff(nested1,
                                      nested2,
                                      plain_format,
                                      correct_nested_plain):
    diff = generate_diff(
        form_path_to_test_file(nested1),
        form_path_to_test_file(nested2),
        plain_format
    )

    with open(form_path_to_test_file(correct_nested_plain), 'r') as file:
        correct_structure = file.read()

        assert diff == correct_structure


@pytest.mark.parametrize(
    'nested1,'
    'nested2,'
    'raw_json_format,'
    'correct_nested_raw_json',
    [('nested1.json',
      'nested2.json',
      'json',
      'correct_nested_raw_json'),
     ('nested1.json',
      'nested2.yml',
      'json',
      'correct_nested_raw_json'),
     ('nested1.yaml',
      'nested2.yml',
      'json',
      'correct_nested_raw_json')]
)
def test_generating_nested_json_diff(nested1,
                                     nested2,
                                     raw_json_format,
                                     correct_nested_raw_json):
    diff = generate_diff(
        form_path_to_test_file(nested1),
        form_path_to_test_file(nested2),
        raw_json_format
    )

    with open(form_path_to_test_file(correct_nested_raw_json), 'r') as file:
        correct_structure = file.read()

        assert diff == correct_structure
