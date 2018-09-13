from unittest import TestCase

from optional import Optional
from optional.something import Something


class TestSomething(TestCase):

    def test_can_not_instantiate_with_a_none_value(self):
        with self.assertRaises(ValueError) as cm:
            Something(value=None, optional=Optional)

        self.assertEqual(
            'Invalid value for Something: None',
            str(cm.exception)
        )

    def test_can_instantiate_with_any_other_value(self):
        self.assertEqual(
            Optional.of(23),
            Something(value=23, optional=Optional)
        )
