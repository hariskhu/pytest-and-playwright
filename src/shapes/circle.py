from .shape import Shape, Color, isnumeric
from typing import Literal, Any
import math

class Circle(Shape):
    """Class defining implementation of the Circle Shape."""
    def __init__(self, *, radius: int | float = None, circumference: int | float = None) -> None:
        """Instatiate a Circle"""
        super.__init__()

        if radius and circumference:
            raise TypeError("Circle() expects one of 'radius' or 'circumference', but received both")
        if radius:
            self.radius = radius
        elif circumference:
            self.circumference = circumference
        else:
            raise TypeError("Circle() expects one of 'radius' or 'circumference', but received neither")

    def __str__(self) -> str:
        """String representation of a Circle for a user."""
        return (
            f"{self._name} the Circle: r = {self._radius} {self._unit}, d = {self._radius * 2} {self._unit}"
            f"C = {self._circumference} {self.unit}, color {self._color!s}"
        )

    def __repr__(self) -> str:
        """String representation of a Circle for a developer."""
        return (
            f"Circle(name={self.name!r}, unit={self._unit!r}, color={self._color!r}, "
            f"radius={self._radius!r}, circumference={self._circumference!r}, area={self.area()!r}"
        )
    
    # PROPERTIES
    @property
    def circumference(self) -> int | float:
        """Circumference of a Circle."""
        return self._circumference
    
    @circumference.setter
    def circumference(self, circumference: int | float) -> None:
        """Updates circumference of a Circle."""
        if not isnumeric(circumference):
            raise TypeError(f"Radius must be numeric, received {circumference!r}")
        if circumference <= 0:
            raise ValueError(f"Circumference must be greater than 0, received {circumference!r}")
        self._circumference = circumference
        self._radius = circumference / (2 * math.pi)
            
    @property
    def radius(self) -> int | float:
        """Radius of a Circle."""
        return self._radius
    
    @radius.setter
    def radius(self, radius: int | float) -> None:
        """Updates radius of a Circle."""
        if not isnumeric(radius):
            raise TypeError(f"Radius must be numeric, received {radius!r}")
        if radius <= 0:
            raise ValueError(f"Radius must be greater than 0, received {radius!r}")
        self._radius = radius
        self._circumference = 2 * radius * math.pi

    # VALIDATION METHODS
    # __class__.__name__ for an oval class
    def _validate_sides(self, sides: Any) -> None:
        """Method used when sides are attempted to be updated."""
        raise TypeError(f"{self.__class__.__name__} does not have sides")
    
    def _validate_angles(self, angles: Any) -> None:
        """Method used when angles are attempted to be updated."""
        raise TypeError(f"{self.__class__.__name__} does not have angles")
    
    # CALCULATION METHODS
    def scale(self, scaling_factor: float | int, *, how: Literal["area", "radius", "circumference"] = "radius") -> None:
        """Scales a Circle based on area, radius, or circumference."""
        if not isnumeric(scaling_factor):
            raise TypeError("scale expects 'scaling_factor' to be of type int or float")
        if scaling_factor <= 0:
            raise ValueError(f"scale() expects 'scaling_factor' to be greater than 0, but received {scaling_factor!r}")
        if not isinstance(how, str):
            raise TypeError("scale() expects 'how' to be of type str")
            
        match how.lower():
            case "area":
                area = self.area() * scaling_factor
                self._radius = math.sqrt(area / math.pi)
                self._circumference = 2 * self._radius * math.pi
            case "radius":
                self._radius *= scaling_factor
                self._circumference = 2 * self.radius * math.pi
            case "circumference":
                self._circumference *= scaling_factor
                self._radius = self._circumference / (2 * math.pi)
            case _:
                raise ValueError(f"scale() expects 'how' to be one of: 'area', 'radius', 'circumference', but received {how!r}")

    
    def area(self) -> float:
        """Calculates and returns the area of a Circle."""
        return self._radius ** 2 * math.pi

    def perimeter(self) -> int | float:
        """Overridden superclass method, effectively an alias to circumference."""
        return self._circumference