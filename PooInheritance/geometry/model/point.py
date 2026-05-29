from dataclasses import dataclass
import math
from typing import override

from geometry.model.form import Form


@dataclass(kw_only=True)
class Point(Form):
    x: float = 0.0
    y: float = 0.0

    @override
    def translate(self, delta_x: float, delta_y: float) -> None:
        self.x += delta_x
        self.y += delta_y

    def distance(self, other: 'Point') -> float:
        return math.hypot(self.x - other.x, self.y - other.y)
    
    # @staticmethod
    # def from_xy(x: float, y: float):
    #     return Point(x=x, y=y)

    @classmethod
    def from_xy(cls, x: float, y: float, **kwargs):
        """Build a Point from its coordinates. 
        The object is built according to the specific class cls 
        (Point or a subclass).

        Arguments:
        - x, y: coordinates
        - kwargs: extra arguments passed to the adequate constructor
        """
        return cls(x=x, y=y, **kwargs)
 
    

@dataclass(kw_only=True)
class WeightedPoint(Point):
    weight: float = 1.0

    # @override
    # def distance(self, other: Point) -> float:
    #     return super().distance(other) / self.weight


@dataclass(kw_only=True)
class ColoredPoint(Point):
    color: str = 'red'


@dataclass(kw_only=True)
class WeightedColoredPoint(WeightedPoint, ColoredPoint):
    pass
