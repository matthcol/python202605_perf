from dataclasses import dataclass
from typing import override

from geometry.model.form import Form


@dataclass
class Point(Form):
    x: float
    y: float

    @override
    def translate(self, delta_x: float, delta_y: float) -> None:
        self.x += delta_x
        self.y += delta_y