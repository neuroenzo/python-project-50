import pytest

from fixtures.correct_flat import correct_flat_structure
from gendiff import generate_diff


@pytest.mark.parametrize(
    'flat1, flat2',
    [('flat1.json',
      'flat2.json'),
     ('flat1.yml',
      'flat2.yml')]
)
def test_generate_diff(flat1, flat2):
    diff = generate_diff(flat1, flat2)
    assert diff == correct_flat_structure
