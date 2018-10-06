import pytest

from optional import Optional
from optional.something import Something


class TestSomething(object):
    def test_can_not_instantiate_with_a_none_value(self):
        with pytest.raises(ValueError, match='\\AInvalid value for Something: None\\Z'):
            Something(value=None, optional=Optional)

    def test_can_instantiate_with_any_other_value(self):
        assert Something(value=23, optional=Optional) == Optional.of(23)
