import pytest
from .assesment import solution


@pytest.mark.parametrize(
    "input,output",
    [
        ("00000", "0"),
        ("12310", "131"),
        ("88892", "898"),
        ("99999", "99999"),
        ("56778449", "74947"),
    ],
)
def test_solution(input, output):
    res = solution(input)
    assert res == output
