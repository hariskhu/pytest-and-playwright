from .shape import Shape, isnumeric
from typing import Literal
import math

class Square(Shape):
    """Class defining the Square Shape."""
    def __init__(self, side_length: int | float) -> None:
        """Instantiates a Square."""
        super().__init__()
        
        self.sides = tuple(side_length for x in range(4))
        self.angles = tuple(90 for x in range(4))

    def __str__(self) -> str:
        """String representation of a Square for a user."""
        return (
            f"{self._name} the Sqaure: l = {self._sides[0]} {self._unit}, "
            f"A = {self.area()} {self._unit}^2, color = {self._color!s}"
        )

    def __repr__(self) -> str:
        """String representation of a Square for a developer."""
        return (
            f"Square(name={self.name!r}, unit={self._unit!r}, "
            f"color={self._color!r}, side_length={self._sides[0]!r})"
        )

    # VALIDATION METHODS
    def _validate_sides(self, sides: tuple[int | float]) -> None:
        """Method used when sides are attempted to be updated."""
        if not isinstance(sides, tuple):
            raise TypeError("Sides must be contained in a tuple")
        if len(sides) != 4:
            raise ValueError(f"Got {len(sides)} sides, expected 4")
        for side in sides:
            if not isnumeric(side):
                raise TypeError(f"Sides must be integers or floats, received {sides!r}")
            if side != sides[0]:
                raise ValueError(f"All sides of a Square must be identical, received {sides!r}")
        
    def _validate_angles(self, angles) -> None:
        """Method used when angles are attempted to be updated."""
        if not isinstance(angles, tuple):
            raise TypeError(f"Angles must be contained in a tuple, received {angles!r}")
        if len(angles) != 4:
            raise ValueError(f"Got {len(angles)}, expected 4")
        if angles != (90, 90, 90, 90):
            raise ValueError(f"Square angles must all be 90 degrees")
        
    # CALCULATION METHODS
    def scale(self, scaling_factor: float | int, *, how: Literal["area", "side_length",] = "side_length") -> None:
        """Scales a Sqaure based on area or side length."""
        if not isnumeric(scaling_factor):
            raise TypeError("scale() expects 'scaling_factor' to be of type int or float")
        if scaling_factor <= 0:
            raise ValueError(f"scale() expects 'scaling_factor' to be greater than 0, but received {scaling_factor!r}")
        if not isinstance(how, str):
            raise TypeError("scale() expects 'how' to be of type str")
            
        match how.lower():
            case "area":
                self._sides = (math.sqrt(self.area() * scaling_factor) for x in range(4))
            case "side_length":
                self._sides = (self._sides[0] * scaling_factor for x in range(4))
            case _:
                raise ValueError(f"scale() expects 'how' to be one of: 'area', 'side_length', but received {how!r}")
            
    def area(self) -> int | float:
        """Returns area of a Square."""
        return self._sides[0] ** 2