from typing import override


class Movie: # inherits class object
    def __init__(self, title: str, year: int):
        self.title = title
        self.year = year

    # customize repr 
    @override
    def __repr__(self) -> str:
        # NB: format !r calls repr instead of str
        return f"Movie(title={self.title!r}, year={self.year})"
    
    # customize str (by default = repr)
    @override
    def __str__(self) -> str:
        return f"{self.title} ({self.year})"