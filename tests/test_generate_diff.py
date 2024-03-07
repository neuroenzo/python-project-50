

import pytest

from fixtures.correct_flat import correct_flat_structure
from fixtures.correct_nested import correct_nested_structure
from gendiff import generate_diff
from gendiff.formatters.stylish import stylish_formatter



@pytest.mark.parametrize(
    'flat1, flat2',
    [('flat1.json',
      'flat2.json')]
)
def test_generate_flat_diff(flat1, flat2):
    diff = generate_diff(file_name_1, file_name_2)
    assert stylish_formatter(diff) == correct_flat_structure


@pytest.mark.parametrize(
    'nested1, nested2',
    [('fixtures/nested1.json',
      'fixtures/nested2.json'),
     ('fixtures/nested1.json',
      'fixtures/nested2.yml'),
     ('fixtures/nested1.yaml',
      'fixtures/nested2.yml')]
)
def test_generate_nested_diff(nested1, nested2):
    diff = generate_diff(nested1, nested2)
    assert stylish_formatter(diff) == correct_nested_structure
