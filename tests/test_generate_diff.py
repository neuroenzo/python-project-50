import pytest

from fixtures.correct_flat_stylish import correct_flat_stylish_structure
from fixtures.correct_nested_stylish import correct_nested_stylish_structure
from fixtures.correct_nested_plain import correct_nested_plain_structure
from fixtures.correct_nested_raw_json import correct_nested_raw_json
from fixtures.correct_flat_raw_json import correct_flat_raw_json
from gendiff import generate_diff


@pytest.mark.parametrize(
    'flat1, flat2, stylish_format',
    [('./tests/fixtures/flat1.json',
      './tests/fixtures/flat2.json',
      'stylish')]
)
def test_generate_flat_stylish_diff(flat1, flat2, stylish_format):
    diff = generate_diff(flat1, flat2, stylish_format)

    assert diff == correct_flat_stylish_structure


@pytest.mark.parametrize(
    'nested1, nested2, stylish_format',
    [('./tests/fixtures/nested1.json',
      './tests/fixtures/nested2.json',
      'stylish'),
     ('./tests/fixtures/nested1.json',
      './tests/fixtures/nested2.yml',
      'stylish'),
     ('./tests/fixtures/nested1.yaml',
      './tests/fixtures/nested2.yml',
      'stylish')]
)
def test_generate_nested_stylish_diff(nested1, nested2, stylish_format):
    diff = generate_diff(nested1, nested2, stylish_format)

    assert diff == correct_nested_stylish_structure


@pytest.mark.parametrize(
    'nested1, nested2, plain_format',
    [('./tests/fixtures/nested1.json',
      './tests/fixtures/nested2.json',
      'plain'),
     ('./tests/fixtures/nested1.json',
      './tests/fixtures/nested2.yml',
      'plain'),
     ('./tests/fixtures/nested1.yaml',
      './tests/fixtures/nested2.yml',
      'plain')]
)
def test_generate_nested_plain_diff(nested1, nested2, plain_format):
    diff = generate_diff(nested1, nested2, plain_format)

    assert diff == correct_nested_plain_structure


@pytest.mark.parametrize(
    'flat1, flat2, raw_json_format',
    [('./tests/fixtures/flat1.json',
      './tests/fixtures/flat2.json',
      'json')]
)
def test_generate_nested_json_diff(flat1, flat2, raw_json_format):
    diff = generate_diff(flat1, flat2, raw_json_format)

    assert diff == correct_flat_raw_json


@pytest.mark.parametrize(
    'nested1, nested2, raw_json_format',
    [('./tests/fixtures/nested1.json',
      './tests/fixtures/nested2.json',
      'json'),
     ('./tests/fixtures/nested1.json',
      './tests/fixtures/nested2.yml',
      'json'),
     ('./tests/fixtures/nested1.yaml',
      './tests/fixtures/nested2.yml',
      'json')]
)
def test_generate_nested_json_diff(nested1, nested2, raw_json_format):
    diff = generate_diff(nested1, nested2, raw_json_format)

    assert diff == correct_nested_raw_json
