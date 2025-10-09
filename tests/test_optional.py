# pyright: reportUnnecessaryComparison=false
# pyright: reportUnreachable=false
# pyright: reportUnusedCallResult = false

import pytest

from optional import Nothing, Optional, Something


def test_can_instantiate():
    Optional.of()


def test_can_instantiate_empty():
    Optional.empty()


def test_can_instantiate_with_content():
    Optional.of("something")


def test_can_instantiate_with_none():
    Optional.of(None)


def test_can_structurally_match_against_nothing():
    match Optional.empty():
        case Something():
            pytest.fail("An empty Optional should not match against Something")
        case Nothing():
            pass
        case _:
            pytest.fail("An Optional should either be Something or Nothing")


def test_can_structurally_match_against_something():
    match Optional.of("thing"):
        case Something():
            pass
        case Nothing():
            pytest.fail("A populated Optional should not match against Nothing")
        case _:
            pytest.fail("An Optional should either be Something or Nothing")


def test_can_structurally_match_against_something_and_extract():
    match Optional.of(23):
        case Something(x):
            assert 23 == x
        case Nothing():
            pytest.fail("A populated Optional should not match against Nothing")
        case _:
            pytest.fail("An Optional should either be Something or Nothing")


def test_optional_not_equal_with_non_optional():
    assert "PANTS" != Optional.of("PANTS")
    assert Optional.of("PANTS") != "PANTS"


def test_empty_optionals_are_equal():
    assert Optional.empty() == Optional.empty()


def test_empty_optional_not_equal_non_empty_optional():
    assert Optional.empty() != Optional.of("thing")


def test_non_empty_optionals_with_non_equal_content_are_not_equal():
    assert Optional.of("PANTS") != Optional.of("thing")


def test_non_empty_optionals_with_equal_content_are_equal():
    assert Optional.of("PANTS") == Optional.of("PANTS")


def test_can_eval_the_representation_of_an_empty_optional():
    optional = Optional.empty()
    assert eval(repr(optional)) == optional


def test_can_eval_the_representation_of_a_populated_optional():
    optional = Optional.of("23")
    assert eval(repr(optional)) == optional


def test_can_instantiate_an_empty_optional_via_the_zero_arity_of():
    assert Optional.of() == Optional.empty()


def test_can_instantiate_an_empty_optional_via_none():
    assert Optional.of(None) == Optional.empty()


def test_populated_optionals_are_truthy():
    assert Optional.of("foo")


def test_populated_optionals_are_truthy_even_if_their_value_is_falsy():
    assert Optional.of(False)


def test_empty_optionals_are_falsy():
    assert not Optional.empty()
