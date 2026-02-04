from abc import ABC, abstractmethod
from dataclasses import dataclass, fields
from typing import Literal, Any
import numbers

@dataclass
class Color:
    """Defines RBG color for a shape."""
    red: int
    green: int
    blue: int

    def __post_init__(self) -> None:
        for color, value in vars(self).items():
            if not isinstance(value, int):
                raise TypeError(f"{color.capitalize()} value must be an integer.")
            if not 0 <= value <= 255:
                raise ValueError(f"{color.capitalize()} value must be between 0 and 255 inclusive.")
            
    def __str__(self) -> str:
        return f"({self.red}, {self.green}, {self.blue})"
    
    def __repr__(self) -> str:
        return f"Color(red={self.red}, green={self.green}, blue={self.blue})"

class Shape(ABC):
    """Abstract base class for all shapes."""
    # MAGIC METHODS
    def __init__(self) -> None:
        """Instantiate a shape."""
        self._name = self.__class__.__name__
        self._color = Color(255, 255, 255) # White
        self._sides = ()
        self._angles = ()
        self._unit = "in"

    def __eq__(self, other: Any) -> bool:
        """Defines == operator with Shapes."""
        return True and bool(other)
    
    def __ne__(self, other: Any) -> bool:
        """Defines != operator with Shapes."""
        return not (True and bool(other))
    
    def __lt__(self, other: Any) -> bool:
        """Defines < operator with Shapes."""
        return self.area() < other
    
    def __gt__(self, other: Any) -> bool:
        """Defines > operator with Shapes."""
        return self.area() > other
    
    def __lt__(self, other: Any) -> bool:
        """Defines <= operator with Shapes."""
        return self.area() <= other
    
    def __gt__(self, other: Any) -> bool:
        """Defines >= operator with Shapes."""
        return self.area() >= other

    @abstractmethod
    def __str__(self) -> str:
        """String representation of a Shape for a user."""
        ...

    @abstractmethod
    def __repr__(self) -> str:
        """String representation of a Shape for a developer."""
        ...

    # ATTRIBUTES
    @property
    def name(self) -> str:
        """The name of the shape (doesn't have to be related to geometry)."""
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """Set a shape's name."""
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self._name = name
    
    @property
    def color(self) -> Color:
        """The color of the shape."""
        return self._color

    @color.setter
    def color(self, color: Color) -> None:
        """Sets a shapes's color."""
        for field in color.fields():
            value = getattr(color, field)
            if not (isinstance(value, int) and not (isinstance(value, bool))):
                raise TypeError(f"Value of {field} must be an integer")
            if not 0 <= value <= 255:
                raise ValueError(f"Value of {field} must be between 0 and 255 inclusive")
            self._color = Color(color.red, color.green, color.blue)

    @property
    def unit(self) -> str:
        """Unit used for each measurement of the shape."""
        return self._unit

    @unit.setter
    def unit(self, unit: str) -> None:
        """Set unit of a shape's side measurements."""
        if not isinstance(unit, str):
            raise TypeError("Unit must be a string")
        self._unit = unit

    @property
    def sides(self) -> tuple[int | float]:
        """A tuple containing the side lengths of a shape."""
        return self._sides
    
    @sides.setter
    def sides(self, sides: tuple[int | float]) -> None:
        """Set a shape's sides."""
        self._validate_sides(sides)
        self._sides = sides

    @abstractmethod
    def _validate_sides(self, sides: tuple[int | float]) -> None:
        """Validates a new sides tuple."""
        ...
    
    @property
    def angles(self) -> tuple[int | float]:
        """A tuple containing the angles of a shape in degrees."""
        return self._angles
    
    @angles.setter
    def angles(self, angles: tuple[int | float]):
        """Set the angles of a shape."""
        self._validate_angles(angles)
        self._angles = angles

    @abstractmethod
    def _validate_angles(self, angles: tuple[int | float]) -> None:
        """Validates a new angles tuple."""
        ...

    # METHODS
    @abstractmethod
    def scale(self, scaling_factor: float | int, *, how: Literal["area", "sides"]) -> None:
        """Scales an object by either its sides or area."""
        ...
    
    @abstractmethod
    def area(self) -> int | float:
        """A shape's area in square inches."""
        ...

    def perimeter(self) -> int | float:
        """The perimeter of a shape (sum of the sides)."""
        return sum(self._sides)

def isnumeric(val: Any) -> bool:
    """Returns true if a value is a float or integer (numeric)."""
    return isinstance(val, numbers.Number) and not isinstance(val, bool)