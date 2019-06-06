"""py.test for idfjsonconverter"""

from eppy3000 import idfjsonconverter

def test_keymapping():
    """py.test for keymapping"""
    data = (
    (
    ('Gumby', 'Softy'),
    ('gumby', 'so', 'softy', 'Kamby'),
    {'Gumby': 'gumby', 'Softy': 'softy'}), # somekeys, allkeys, expected
    )
    for somekeys, allkeys, expected in data:
        result = idfjsonconverter.keymapping(somekeys, allkeys)
        assert result == expected