import pytest

from fixtures.correct_flat import correct_flat_structure
from gendiff import generate_diff
from gendiff.formatters.stylish import stylish_formatter


@pytest.mark.parametrize(
    'flat1, flat2',
    [('.tests/fixtures/flat1.json',
      '.tests/fixtures/flat2.json')]
)
def test_generate_diff(flat1, flat2):
    diff = generate_diff(flat1, flat2)
    assert stylish_formatter(diff) == correct_flat_structure

# @pytest.mark.parametrize(
#     'flat1, flat2',
#     [('/Users/virtualpoint/PycharmProjects/python-project-50/tests/fixtures/flat1.json',
#       '/Users/virtualpoint/PycharmProjects/python-project-50/tests/fixtures/flat2.json'),
#      ('/Users/virtualpoint/PycharmProjects/python-project-50/tests/fixtures/flat1.yml',
#       '/Users/virtualpoint/PycharmProjects/python-project-50/tests/fixtures/flat2.yaml')]
# )
# def test_generate_diff(flat1, flat2):
#     diff = generate_diff(flat1, flat2)
#     assert diff == correct_flat_structure
