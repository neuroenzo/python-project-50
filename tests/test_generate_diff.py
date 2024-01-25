import pytest

from gendiff.scripts.gendiff import generate_diff

control = """{
- follow: false
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: true
}"""


@pytest.mark.parametrize(
    'flat1, flat2',
    [('./tests/fixtures/flat1.json',
      './tests/fixtures/flat2.json')]
)
def test_generate_diff(flat1, flat2):
    diff = generate_diff(flat1, flat2)
    assert diff == control
