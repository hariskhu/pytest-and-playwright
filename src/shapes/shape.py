from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal

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
        return f"({self.red}, {self.green}.{self.blue})"
    
    def __repr__(self) -> str:
        return f"Color(red={self.red}, green={self.green}, blue={self.blue})"

class Shape(ABC):
    """Abstract base class for all shapes."""
    @property
    @abstractmethod
    def name(self) -> str:
        """The name of the shape (doesn't have to be related to geometry)."""
        ...
    
    @property
    @abstractmethod
    def color(self) -> Color:
        """The color of the shape."""

    @property
    @abstractmethod
    def units(self) -> str:
        """Units used for each measurement of the shape."""

    @property
    @abstractmethod
    def sides(self) -> list[int | float]:
        """A list containing the side lengths of a shape."""
        ...
    
    @sides.setter
    @abstractmethod
    def sides(self, value: list[int | float]) -> None:
        """Set a shape's sides."""
        ...
    
    @property
    @abstractmethod
    def angles(self) -> list[int | float]:
        """A list containing the angles of a shape in degrees."""
        ...
    
    @angles.setter
    @abstractmethod
    def angles(self, value: list[int | float]) -> None:
        """Set a shape's angles."""
        ...

    @property
    @abstractmethod
    def area(self) -> float:
        """A shape's area in square inches."""
        ...

    @abstractmethod
    def __init__(self) -> None:
        """Instantiate a shape by giving its side lengths"""
        ...

    @abstractmethod
    def scale(self, scaling_factor: float | int, how: Literal["area", "sides"]) -> None:
        """Scales an object by either its sides or area."""
        ...