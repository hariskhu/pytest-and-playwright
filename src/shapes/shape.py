from abc import ABC, abstractmethod

class Shape(ABC):
    name: str
    color: str

    @property
    @abstractmethod
    def sides(self) -> list[int | float]:
        """A list containing the side lengths of classes in inches."""
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