import pytest

from fixtures.correct_flat import correct_flat_structure
from fixtures.correct_nested import correct_nested_structure
from gendiff import generate_diff
from gendiff.formatters.stylish import stylish_formatter


@pytest.mark.parametrize(
    'flat1, flat2',
    [('python-project-50/tests/fixtures/flat1.json',
      'python-project-50/tests/fixtures/flat2.json')]
)
def test_generate_flat_diff(flat1, flat2):
    diff = generate_diff(flat1, flat2)
    assert stylish_formatter(diff) == correct_flat_structure


@pytest.mark.parametrize(
    'nested1, nested2',
    [('python-project-50/tests/fixtures/nested1.json',
      'python-project-50/tests/fixtures/nested2.json'),
     ('python-project-50/tests/fixtures/nested1.json',
      'python-project-50/tests/fixtures/nested2.yml'),
     ('python-project-50/tests/fixtures/nested1.yaml',
      'python-project-50/tests/fixtures/nested2.yml')]
)
def test_generate_nested_diff(nested1, nested2):
    diff = generate_diff(nested1, nested2)
    assert stylish_formatter(diff) == correct_nested_structure
