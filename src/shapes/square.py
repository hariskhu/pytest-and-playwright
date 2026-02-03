from .shape import Shape, Color, isnumeric
from typing import Literal, Any
import math

class Square(Shape):
    """Class defining the Square Shape."""
    def __init__(self, side_length: int | float) -> None:
        """Instantiates a Square."""
        super().__init__()
        
        self.sides = tuple(side_length for x in range(4))
        self.angles = tuple(90 for x in range(4))

    # ATTRIBUTES
    def _validate_sides(self, sides: tuple[int | float] | int | float) -> None:
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
        
    def _validate_angles(self, angles):
        """Method used when angles are attempted to be updated."""
        if not isinstance(angles, tuple):
            raise TypeError(f"Angles must be contained in a tuple, received {angles!r}")
        if len(angles) != 4:
            raise ValueError(f"Got {len(angles)}, expected 4")
        if angles != (90, 90, 90, 90):
            raise ValueError(f"Square angles must all be 90 degrees")
        
    # METHODS