
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
    def __add__(self, other) -> Polygon:
        # TODO : add coord, tuple(coord)
        if not isinstance(other, int):
            return NotImplemented
        return Polygon(
            [(x + other, y + other) for (x,y) in self.vertices]
        )
    
    def __radd__(self, other) -> Polygon:
        return self.__add__(other)
    
    def __iadd__(self, other) -> Polygon:
        if not isinstance(other, int):
            return NotImplemented
        for i, (x, y) in enumerate(self.vertices):
            self.vertices[i] = (x + other, y + other) 
        return self


    # 2nd iteration => .edges()
    def edges(self) -> Generator[segment, None, None]:
        prec_vertix = self.vertices[-1] # polygon is wel-formed
        for next_vertix in self.vertices:
            yield (prec_vertix, next_vertix)
            prec_vertix = next_vertix

