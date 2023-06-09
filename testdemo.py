from demo import exponential_this
import numpy as np
import pytest

@pytest.mark.parametrize(
        "input, expected", 
        [
            (10, np.exp(10)), 
            (5, np.exp(5)), 
            (10, np.exp(10)), 
            (77, np.exp(77))
    ]
)
def test_exponential(input, expected):

    assert exponential_this(input) == expected, "Function is not working"