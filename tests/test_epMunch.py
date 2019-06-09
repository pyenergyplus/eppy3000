# Copyright (c) 2019 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""py.test for epMunch"""

from eppy3000 import epMunch


def test_printkey():
    """py.test for printkey"""
    data = (
        ("Gumby", None, None,
            ["", "", "Gumby"]),  # key, indent, formatstr, expected
        ("Gumby", 1, None,
            ["", "    Gumby"]),  # key, indent, formatstr, expected
        ("Gumby", None, "{}{}",
            ["", "", "Gumby"]),  # key, indent, formatstr, expected
        ("Gumby", None, "{}{},",
            ["", "", "Gumby,"]),  # key, indent, formatstr, expected
    )
    for key, indent, formatstr, expected in data:
        lines = []
        epMunch.printkey(key, indent, formatstr, func=lines.append)
        assert lines == expected


def test_printkey_withprint(capsys):
    """py.est for printkey when func=None"""
    key, indent, formatstr, expected = ("Gumby", None, None,
            '\n\nGumby\n')
    epMunch.printkey(key, indent, formatstr)
    captured = capsys.readouterr()
    assert captured.out == expected
