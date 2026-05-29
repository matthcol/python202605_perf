

from dataclasses import dataclass

from geometry.model.form import Form


@dataclass
class Circle(Form):

    def translate(self, delta_x: float, delta_y: float) -> None:
        # TODO
        pass