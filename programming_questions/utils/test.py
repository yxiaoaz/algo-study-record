import pytest

class Test:

    @pytest.mark.parametrize(
        "a,b,c",
        [
            (1, 2, 3),
        ],
    )
    def test(a, b, c):
        assert a + b == c
