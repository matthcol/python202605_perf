from collections.abc import Sized
from dataclasses import dataclass
from typing import override


@dataclass
class Polygon(Sized):
    vertices: list[tuple[float, float]]

    @override
    def __len__(self) -> int:
        return len(self.vertices)