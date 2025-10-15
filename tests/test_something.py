# pyright: reportUnusedCallResult=false

import pytest

from optional import Optional, Something


def test_can_not_instantiate_with_a_none_value():
    with pytest.raises(ValueError, match="\\AInvalid value for Something: None\\Z"):
        Something(None)


def test_can_instantiate_with_any_other_value():
    assert Something(23) == Optional[int].of(23)
