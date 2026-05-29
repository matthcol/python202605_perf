from decimal import Decimal

import pytest

from geometry import Polygon

@pytest.fixture
def triangle345():
    return Polygon([(12.5, 7.25), (12.5, 10.25), (16.5, 7.25)])

@pytest.mark.parametrize(
        'right_operand, expected_result_polygon',
        [
            (2, Polygon([(14.5, 9.25), (14.5, 12.25), (18.5, 9.25)])),
            (2.5, Polygon([(15.0, 9.75), (15.0, 12.75), (19.0, 9.75)])),
            ((2, -1.0), Polygon([(14.5, 6.25), (14.5, 9.25), (18.5, 6.25)])),
        ],
        ids=[
            'right operand int',
            'right operand float',
            'right operand tuple of 2',
        ]
)
def test_polygon_add_implemented(triangle345, right_operand, expected_result_polygon):
    actual_result_polygon = triangle345.__add__(right_operand)
    assert actual_result_polygon == expected_result_polygon # uses Polygon.__eq__ (@dataclass) then list.__eq__ 

@pytest.mark.parametrize(
        'right_operand',
        [
            ('a text is not a coordinate',),
            (True, ),
            ((1,)),
            ((1, 2, 3)),
        ],
        ids=[
            'right operand text',
            'right operand boolean',
            'right operand tuple of 1',
            'right operand tuple of 3',
        ]
)
def test_polygon_add_not_implemented(triangle345, right_operand):
    actual_result_polygon = triangle345.__add__(right_operand)
    assert actual_result_polygon is NotImplemented


def test_float_equals():
    y = 3 * 0.1         # 0.1 (base 10) = 0.0001100110011001100... (base 2)
    # assert y == 0.3     #  0.30000000000000004 == 0.3
    assert y == pytest.approx(0.3, rel=1e-15)

def test_decimal_equals():
    y = 3 * Decimal('0.1')
    assert y == Decimal('0.3')