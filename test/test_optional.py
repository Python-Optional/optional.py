import pytest

from optional import Optional
from optional.exceptions import (
    OptionalAccessOfEmptyException,
    FlatMapFunctionDoesNotReturnOptionalException
)

class TestOptional(object):

    def test_can_instantiate(self):
        Optional.of(None)

    def test_instantiate_empty(self):
        optional = Optional.empty()
        assert optional.is_empty()

    def test_instantiate_with_content(self):
        optional = Optional.of("something")
        assert not optional.is_empty()

    def test_instantiate_with_none(self):
        optional = Optional.of(None)
        assert optional.is_empty()

    def test_is_present_with_content(self):
        optional = Optional.of("thing")
        assert optional.is_present()

    def test_is_not_present_with_empty(self):
        optional = Optional.of(None)
        assert not optional.is_present()

    def test_cannot_get_from_empty_even_after_checking(self):
        optional = Optional.empty()
        assert optional.is_empty()
        with pytest.raises(OptionalAccessOfEmptyException):
            optional.get()

    def test_can_get_when_present_and_have_checked(self):
        optional = Optional.of("thing")
        assert optional.is_present()
        assert optional.get() == "thing"

    def test_will_run_consumer_if_present(self):
        scope = {'seen': False}

        def some_thing_consumer(thing):
            scope['seen'] = True

        optional = Optional.of("thing")
        optional.if_present(some_thing_consumer)
        assert scope['seen']

    def test_will_not_run_consumer_if_not_present(self):
        scope = {'seen': False}

        def some_thing_consumer(thing):
            scope['seen'] = True

        optional = Optional.empty()
        optional.if_present(some_thing_consumer)
        assert not scope['seen']

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
        assert not scope['if_seen']
        assert scope['else_seen']

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
        assert scope['if_seen']
        assert not scope['else_seen']

    def test_will_raise_on_or_else_raise_from_if_present_when_not_present(self):
        class TestException(Exception):
            pass

        optional = Optional.empty()
        with pytest.raises(TestException):
            optional.if_present(lambda x: x).or_else_raise(TestException("Something"))

    def test_wont_raise_on_or_else_raise_from_if_present_when_present(self):
        class ShouldNotHappenException(Exception):
            pass

        optional = Optional.of("thing")
        scope = {'seen': False}

        def some_thing_consumer(thing):
            scope['seen'] = True

        optional.if_present(some_thing_consumer).or_else_raise(ShouldNotHappenException)
        assert scope['seen']

    def test_map_returns_empty_if_function_returns_none(self):

        def does_nothing(thing):
            return None

        optional = Optional.of("thing")
        assert optional.map(does_nothing).is_empty()

    def test_map_returns_empty_if_value_is_empty(self):

        def does_stuff(thing):
            return "PANTS"

        optional = Optional.empty()
        assert optional.map(does_stuff).is_empty()

    def test_map_returns_optional_wrapped_value_with_map_result(self):

        def maps_stuff(thing):
            return thing + "PANTS"

        optional = Optional.of("thing")
        res = optional.map(maps_stuff)
        assert res.is_present()
        assert res.get() == "thingPANTS"

    def test_flat_map_returns_empty_if_function_returns_empty_optional(self):

        def does_nothing(thing):
            return Optional.empty()

        optional = Optional.of("thing")
        assert optional.flat_map(does_nothing).is_empty()

    def test_raises_if_flat_map_function_returns_non_optional(self):

        def does_not_return_optional(thing):
            return "PANTS"

        optional = Optional.of("thing")
        with pytest.raises(FlatMapFunctionDoesNotReturnOptionalException):
            optional.flat_map(does_not_return_optional)

    def test_flat_map_returns_empty_if_value_is_empty(self):

        def does_stuff(thing):
            return Optional.of("PANTS")

        optional = Optional.empty()
        assert optional.flat_map(does_stuff).is_empty()

    def test_flat_map_returns_unwrapped_value_with_map_result(self):

        def maps_stuff(thing):
            return Optional.of(thing + "PANTS")

        optional = Optional.of("thing")
        res = optional.flat_map(maps_stuff)
        assert res.is_present()
        assert res.get() == "thingPANTS"

    def test_optional_not_equal_with_non_optional(self):
        assert "PANTS" != Optional.of("PANTS")

    def test_empty_optionals_are_equal(self):
        assert Optional.empty() == Optional.empty()

    def test_empty_optional_not_equal_non_empty_optional(self):
        assert Optional.empty() != Optional.of("thing")

    def test_non_empty_optionals_with_non_equal_content_are_not_equal(self):
        assert Optional.of("PANTS") != Optional.of("thing")

    def test_non_empty_optionals_with_equal_content_are_equal(self):
        assert Optional.of("PANTS") == Optional.of("PANTS")

    def test_can_eval_the_representation_of_an_empty_optional(self):
        optional = Optional.empty()
        assert eval(repr(optional)) == optional

    def test_can_eval_the_representation_of_a_populated_optional(self):
        optional = Optional.of(23)
        assert eval(repr(optional)) == optional

    def test_can_instantiate_an_empty_optional_via_the_zero_arity_of(self):
        assert Optional.of() == Optional.empty()

    def test_get_or_default_on_a_populated_optional_ignores_default_value(self):
        optional = Optional.of("thing")
        assert optional.get_or_default("pants") == optional.get()

    def test_get_or_default_on_an_empty_optional_returns_default_value(self):
        optional = Optional.empty()
        assert optional.get_or_default("pants") == "pants"

    def test_get_or_raise_on_a_populated_optional_returns_value(self):
        optional = Optional.of("thing")

        class RandomDomainException(Exception):
            pass

        assert optional.get_or_raise(RandomDomainException()) == optional.get()

    def test_get_or_raise_on_an_empty_optional_throws_wrapped_exception(self):
        optional = Optional.empty()

        class RandomDomainException(Exception):
            pass

        with pytest.raises(RandomDomainException):
            optional.get_or_raise(RandomDomainException())
