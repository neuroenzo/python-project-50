import pytest

from gendiff.scripts.gendiff import generate_diff

control_file = """{
- follow: false
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: true
}"""


@pytest.mark.parametrize(
    'flat1, flat2',
    [('flat1.json',
      'flat2.json'),
     ('flat1.yml',
      'flat2.yml')]
)
def test_generate_diff(flat1, flat2):
    diff = generate_diff(flat1, flat2)
    assert diff == control_file
