import unittest

from optional import Optional, OptionalAccessWithoutCheckingPresenceException, OptionalAccessOfEmptyException


class TestOptional(unittest.TestCase):

    def test_can_instantiate(self):
        Optional(None)

    def test_instantiate_empty(self):
        optional = Optional.empty()
        self.assertTrue(optional.is_empty())

    def test_instantiate_with_content(self):
        optional = Optional.of("something")
        self.assertFalse(optional.is_empty())

    def test_is_present_with_content(self):
        optional = Optional.of("thing")
        self.assertTrue(optional.is_present())

    def test_is_not_present_with_empty(self):
        optional = Optional.of(None)
        self.assertFalse(optional.is_present())

    def test_cannot_get_without_checking_presence(self):
        optional = Optional.of("thing")
        with self.assertRaises(OptionalAccessWithoutCheckingPresenceException):
            optional.get()

    def test_cannot_get_from_empty_even_after_checking(self):
        optional = Optional.empty()
        self.assertTrue(optional.is_empty())
        with self.assertRaises(OptionalAccessOfEmptyException):
            optional.get()

    def test_can_get_when_present_and_have_checked(self):
        optional = Optional.of("thing")
        self.assertTrue(optional.is_present())
        self.assertEqual("thing", optional.get())

    def test_will_run_consumer_if_present(self):
        scope = {'seen': False}

        def some_thing_consumer(thing):
            scope['seen'] = True

        optional = Optional.of("thing")
        optional.if_present(some_thing_consumer)
        self.assertTrue(scope['seen'])

    def test_will_not_run_consumer_if_not_present(self):
        scope = {'seen': False}

        def some_thing_consumer(thing):
            scope['seen'] = True

        optional = Optional.empty()
        optional.if_present(some_thing_consumer)
        self.assertFalse(scope['seen'])

    def test_will_run_or_else_from_if_present_when_not_present(self):
        scope = {
            'if_seen': False,
            'else_seen': False
        }

        def some_thing_consumer(thing):
            scope['if_seen'] = True

        def or_else_procedure():
            scope['else_seen'] = True

        optional = Optional.empty()
        optional.if_present(some_thing_consumer).or_else(or_else_procedure)
        self.assertFalse(scope['if_seen'])
        self.assertTrue(scope['else_seen'])


if __name__ == '__main__':
    unittest.main()
