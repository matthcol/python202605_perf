
from collections.abc import Generator, Iterable, Iterator, Sized
from dataclasses import dataclass
from typing import override

type coord = float | int
type vertex = tuple[coord, coord]
type segment = tuple[vertex, vertex]


@dataclass
class Polygon(Sized, Iterable):
    vertices: list[vertex]

    def __post_init__(self):
        assert len(self.vertices) >= 3, "a polygon must have at least 3 vertices"

    @override
    def __len__(self) -> int:
        return len(self.vertices)
    
    # default iteration => vertices
    @override
    def __iter__(self) -> Iterator[vertex]:
        return iter(self.vertices)

    # Tutorial Pattern matching
    # https://peps.python.org/pep-0636/
    def __add__(self, other) -> 'Polygon': # with python 3.14+, quotes around current class for typing are not mandatory anymore
        match other:
            case int() | float():
                return Polygon([(x + other, y + other) for (x,y) in self.vertices])
            # case (int(dx) | float(dx), int(dy) | float(dy)):
            case (int() | float() as dx, int() | float() as dy):
                return Polygon([(x + dx, y + dy) for (x, y) in self.vertices])
            case _: 
                return NotImplemented
        
    
    def __radd__(self, other) -> 'Polygon':
        return self.__add__(other)
    
    # Note: if absent calls __add__ and replace reference
    def __iadd__(self, other) -> 'Polygon':
        match other:
            case int() | float():
                for i, (x, y) in enumerate(self.vertices):
                    self.vertices[i] = (x + other, y + other) 
            case (int() | float() as dx, int() | float() as dy):
                for i, (x, y) in enumerate(self.vertices):
                    self.vertices[i] = (x + dx, y + dy) 
            case _: 
                return NotImplemented
        return self

    # 2nd iteration => .edges()
    def edges(self) -> Generator[segment, None, None]:
        prec_vertix = self.vertices[-1] # polygon is wel-formed
        for next_vertix in self.vertices:
            yield (prec_vertix, next_vertix)
            prec_vertix = next_vertix

