# Copyright (c) 2022 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""py.test for epj_mmapping"""

import pytest

from eppy3000.epj_mmapping import EpjMapping
from eppy3000.epj_mmapping import EpjSequence

def eppyfields(epj):
    """put eppy fields into epj"""
    for key in epj:
        for kkey in epj[key]:
            epj[key][kkey]['eppykey'] = key
            epj[key][kkey]['eppyname'] = kkey
    return epj
    
def epjsequence2dict(epjs):
    """convert the epjsequence to a dict to compare to epj[key]"""
    return {item['eppyname']:{key:item[key] for key in item} for item in epjs}    

@pytest.fixture
def make_epj():
    epj = dict(
        Zone=dict(
                zone1=dict(area=15, type="conditioned"),
                 ), 
        Wall=dict(
                wall1=dict(area=23, ZoneName="zone1"),
                wall2=dict(area=24, ZoneName="zone1"),
                 ), 
             )
    return eppyfields(epj)
    

def test_epj_mapping_init(make_epj):
    """py.test for EpjMapping init"""
    epj = make_epj
    mm = EpjMapping(epj)
    expectedkeys =  ['Zone', 'Wall']
    result = list(mm.keys())
    assert result == expectedkeys
    result = mm['Zone']
    assert isinstance(result, EpjSequence)
    assert len(result) == 1
    result = mm['Wall']
    assert isinstance(result, EpjSequence)
    assert len(result) == 2
    
def test_epj_mapping_functions(make_epj):
    """apy.test for EpjMapping functions
        - __getitem__ -> a = d['a']
        - len()
        - __setitem__ -> d['a'] = 1
        - __delitem__ -> pop('a')
    ensure that the change is reflected in the epj
    """
    epj = make_epj
    mm = EpjMapping(epj)
    # - __getitem__ -> a = d['a']
    result = mm['Zone']
    expected = [{'area': 15, 'type': 'conditioned', 'eppykey': 'Zone', 'eppyname': 'zone1'}]
    for r1, e1 in zip(result, expected):
        assert r1 == e1
    assert epjsequence2dict(result) == epj['Zone']
    # - len()
    result = len(mm)
    assert result == len(epj)
    # - __setitem__ -> d['a'] = 1
    # completely new item
    newval = [{'long': 15, 'lat': 32, 'eppykey': 'Location', 'eppyname': 'City'}, 
        {'long': 25, 'lat': 42, 'eppykey': 'Location', 'eppyname': 'London'}]
    mm['Location'] = newval
    expected = epjsequence2dict(newval)
    assert epj['Location'] == expected
    # replace an existing item
    newval = [{'area': 105, 'type': 'unconditioned', 'eppykey': 'Zone', 'eppyname': 'zone2'}]
    mm['Zone'] = newval
    expected = epjsequence2dict(newval)
    assert epj['Zone'] == expected
    # - __delitem__ -> pop('a')
    mm.pop('Zone')
    assert set(epj.keys()) == {'Wall', 'Location'} # unordered
    
def test_epj_sequence_functions(make_epj):
    """py.test for EpjSequence functions
        - __getitem__ -> a = d[i]
        - len()
        - __setitem__ -> d[i] = 1, d.append('a'), d.extend(['a'])
        - insert -> d.insert(i, 'a')
        - __delitem__ -> remove('a'), pop(i), clear()
    ensure that the change is reflected in the epj
    """
    pass    
    epj = make_epj
    mm = EpjMapping(epj)
    # - __getitem__ -> a = d[i]
    zones = mm['Zone']
    result = epjsequence2dict(zones)
    assert result == epj['Zone']
    # - len()
    walls = mm['Wall']
    assert len(walls) == len(epj['Wall'])
    # - __setitem__ -> d.append('a')
    newval = {'area': 105, 'type': 'unconditioned', 'eppykey': 'Zone', 'eppyname': 'zone2'}
    zones = mm['Zone']
    expected = epjsequence2dict([zone for zone in zones] + [newval])
    zones.append(newval)
    result = epj['Zone']
    assert result == expected
    # - __getitem__ -> a = d[i]
    zones = mm['Zone']
    zone = zones[-1]
    assert zone == epj['Zone']['zone2']
    # - __delitem__ -> remove('a')
    newval = {'area': 105, 'type': 'unconditioned', 'eppykey': 'Zone', 'eppyname': 'zone2'} # same as before
    zones = mm['Zone']
    zones.remove(newval)
    assert len(epj['Zone']) == 1
    # - __setitem__ -> d.extend(['a'])
    newval = {'area': 105, 'type': 'unconditioned', 'eppykey': 'Zone', 'eppyname': 'zone2'}
    zones = mm['Zone']
    zones.extend([newval,])
    assert len(epj['Zone']) == 2
    # - __setitem__ -> d[i] = 1
    newval = {'area': 105, 'type': 'unconditioned', 'eppykey': 'Zone', 'eppyname': 'zone3'}
    zones = mm['Zone']
    zones[0] = newval
    assert len(epj['Zone']) == 2
    assert set(epj['Zone'].keys()) == {'zone2', 'zone3'}
    # - __delitem__ -> pop(i)
    zones = mm['Zone']
    popedval = zones.pop(0)
    assert popedval == newval
    assert len(epj['Zone']) == 1
    assert epj['Zone']['zone2'] == zones[0]
    # - __delitem__ -> clear()
    walls = mm['Wall']
    walls.clear()
    assert not epj['Wall'] # empty list
