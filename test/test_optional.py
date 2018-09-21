from unittest import TestCase

from optional import Optional
from optional.exceptions import (
    OptionalAccessOfEmptyException,
    FlatMapFunctionDoesNotReturnOptionalException
)


class TestOptional(TestCase):

    def test_can_instantiate(self):
        Optional.of(None)

    def test_instantiate_empty(self):
        optional = Optional.empty()
        self.assertTrue(optional.is_empty())

    def test_instantiate_with_content(self):
        optional = Optional.of("something")
        self.assertFalse(optional.is_empty())

    def test_instantiate_with_none(self):
        optional = Optional.of(None)
        self.assertTrue(optional.is_empty())

    def test_is_present_with_content(self):
        optional = Optional.of("thing")
        self.assertTrue(optional.is_present())

    def test_is_not_present_with_empty(self):
        optional = Optional.of(None)
        self.assertFalse(optional.is_present())

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

    def test_will_not_run_or_else_from_if_present_when_not_empty(self):
        scope = {
            'if_seen': False,
            'else_seen': False
        }

        def some_thing_consumer(thing):
            scope['if_seen'] = True

        def or_else_procedure():
            scope['else_seen'] = True

        optional = Optional.of(23)
        optional.if_present(some_thing_consumer).or_else(or_else_procedure)
        self.assertTrue(scope['if_seen'])
        self.assertFalse(scope['else_seen'])

    def test_will_raise_on_or_else_raise_from_if_present_when_not_present(self):
        class TestException(Exception):
            pass

        optional = Optional.empty()
        with self.assertRaises(TestException):
            optional.if_present(lambda x: x).or_else_raise(TestException("Something"))

    def test_wont_raise_on_or_else_raise_from_if_present_when_present(self):
        class ShouldNotHappenException(Exception):
            pass

        optional = Optional.of("thing")
        scope = {'seen': False}

        def some_thing_consumer(thing):
            scope['seen'] = True

        optional.if_present(some_thing_consumer).or_else_raise(ShouldNotHappenException)

        self.assertTrue(scope['seen'])

    def test_map_returns_empty_if_function_returns_none(self):

        def does_nothing(thing):
            return None

        optional = Optional.of("thing")
        self.assertTrue(optional.map(does_nothing).is_empty())

    def test_map_returns_empty_if_value_is_empty(self):

        def does_stuff(thing):
            return "PANTS"

        optional = Optional.empty()
        self.assertTrue(optional.map(does_stuff).is_empty())

    def test_map_returns_optional_wrapped_value_with_map_result(self):

        def maps_stuff(thing):
            return thing + "PANTS"

        optional = Optional.of("thing")
        res = optional.map(maps_stuff)
        self.assertTrue(res.is_present())
        self.assertEqual("thingPANTS", res.get())

    def test_flat_map_returns_empty_if_function_returns_empty_optional(self):

        def does_nothing(thing):
            return Optional.empty()

        optional = Optional.of("thing")
        self.assertTrue(optional.flat_map(does_nothing).is_empty())

    def test_raises_if_flat_map_function_returns_non_optional(self):

        def does_not_return_optional(thing):
            return "PANTS"

        optional = Optional.of("thing")
        with self.assertRaises(FlatMapFunctionDoesNotReturnOptionalException):
            optional.flat_map(does_not_return_optional)

    def test_flat_map_returns_empty_if_value_is_empty(self):

        def does_stuff(thing):
            return Optional.of("PANTS")

        optional = Optional.empty()
        self.assertTrue(optional.flat_map(does_stuff).is_empty())

    def test_flat_map_returns_unwrapped_value_with_map_result(self):

        def maps_stuff(thing):
            return Optional.of(thing + "PANTS")

        optional = Optional.of("thing")
        res = optional.flat_map(maps_stuff)
        self.assertTrue(res.is_present())
        self.assertEqual("thingPANTS", res.get())

    def test_optional_not_equal_with_non_optional(self):
        self.assertNotEqual("PANTS", Optional.of("PANTS"))

    def test_empty_optionals_are_equal(self):
        self.assertEqual(Optional.empty(), Optional.empty())

    def test_empty_optional_not_equal_non_empty_optional(self):
        self.assertNotEqual(Optional.empty(), Optional.of("thing"))

    def test_non_empty_optionals_with_non_equal_content_are_not_equal(self):
        self.assertNotEqual(Optional.of("PANTS"), Optional.of("thing"))

    def test_non_empty_optionals_with_equal_content_are_equal(self):
        self.assertEqual(Optional.of("PANTS"), Optional.of("PANTS"))

    def test_can_eval_the_representation_of_an_empty_optional(self):
        optional = Optional.empty()
        self.assertEqual(optional, eval(repr(optional)))

    def test_can_eval_the_representation_of_a_populated_optional(self):
        optional = Optional.of(23)
        self.assertEqual(optional, eval(repr(optional)))

    def test_can_instantiate_an_empty_optional_via_the_zero_arity_of(self):
        optional = Optional.of()
        self.assertEqual(Optional.empty(), optional)
