from .shape import Shape, Color, isnumeric
import math

class Circle(Shape):
    """Class defining implementation of the Circle Shape."""
    def __init__(
            self, 
            *, 
            radius: int | float = None,
            circumference: int | float = None,
    ) -> None:
        """Instatiate a Circle"""
        if radius and circumference:
            raise TypeError("Circle() expects one of 'radius' or 'circumference', but received both")
        if radius:
            if isnumeric(radius):
                if radius <= 0: raise ValueError("Radius must be greater than 0")
                self._radius = radius
                self._circumference = 2 * radius * math.pi
            else:
                raise TypeError(f"Radius must be numeric, received {radius!r}")
        elif circumference:
            if isnumeric(circumference):
                if circumference <= 0: raise ValueError("Circumference must be greater than 0")
                self._circumference = circumference
                self._radius = circumference / (2 * math.pi)
            else:
                raise TypeError(f"Radius must be numeric, received {circumference!r}")
        else:
            raise TypeError("Circle() expects one of 'radius' or 'circumference', but received neither")
        
        self._name = "Circle"
        self._color = Color(255, 255, 255) # White
        self._units = "in"
        self._sides = ()
        self._area = math.pi * self._radius ** 2

    def __str__(self) -> str:
        """String representation of a Shape for a user."""
        return f"{self._name} the Circle: radius {self._radius} {self._units}, color {self._color!s}"

    def __repr__(self) -> str:
        """String representation of a Shape for a developer."""
        return (
            f"Circle(name={self.name}, units={self._units}, color={self._color!r}, "
            f"radius={self._radius}, circumference={self._circumference}, area={self._area}"
        )

