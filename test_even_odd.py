from even_odd import evenodd
import pytest

class TestEvenOdd:

  @pytest.mark.parametrize("n,expected", [(2, 'even'), (5, 'odd'), (0, 'even'), (11, 'odd')])
  def test_evenodd(self, n, expected):
    assert evenodd(n=n) == expected