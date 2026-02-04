import pytest
import numpy as np
from shapes.circle import Circle
from shapes.shape import Color

@pytest.fixture
def new_circle():
    return Circle(radius=1)

@pytest.fixture
def white():
    return Color(255, 255, 255)

class TestCircleCreation:
    """Tests for creating Circles."""
    def test_circle_default_name(self, new_circle: Circle) -> None:
        assert new_circle.name == "Circle"

    def test_circle_default_color(self, new_circle: Circle, white: Color) -> None:
        assert new_circle.color == white

    def test_circle_default_unit(self, new_circle: Circle) -> None:
        assert new_circle.unit == "in"

    def test_circle_default_sides(self, new_circle: Circle) -> None:
        assert new_circle.sides == ()

    def test_circle_default_angles(self, new_circle: Circle) -> None:
        assert new_circle.angles == ()

    @pytest.mark.parametrize(
        "n,expected",
        [(x * 0.1, x * 0.1) for x in range(1, 11)]
    )
    def test_circle_create_radius(self, n: int, expected: int) -> None:
        circle: Circle = Circle(radius=n)

        assert circle.radius == expected

    @pytest.mark.parametrize(
        "n,expected",
        [(x * 0.1, x * 0.1) for x in range(1, 11)]
    )
    def test_circle_create_circumference(self, n: int, expected: int) -> None:
        circle: Circle = Circle(circumference=n)

        assert circle.circumference == expected

class TestCircleOperators:
    """Tests for boolean Opeartors on Circles."""
    @pytest.mark.parametrize("left,right,expected", [
        (2, 0.5, False),
        (2, 1, False),
        (2, 1.5, False),
        (2, 2, False),
        (2, 2.5, True),
        (2, 3, True),
    ])
    def test_circle_lt(self, left: int | float, right: int | float, expected: bool) -> None:
        left_circle: Circle = Circle(radius=left)
        right_circle: Circle = Circle(radius=right)
        
        assert left_circle < right_circle == expected