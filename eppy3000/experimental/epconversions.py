# Copyright (c) 2023 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================

"""Conversion functions for EnergyPlus"""

TXT = """! Default IP conversions (no ip-units necessary)
!      $/(m3/s)               =>   $/(ft3/min)         0.000472000059660808
!      $/(W/K)                =>   $/(Btu/h-F)         0.52667614683731
!      $/kW                   =>   $/(kBtuh/h)         0.293083235638921
!      $/m2                   =>   $/ft2               0.0928939733269818
!      $/m3                   =>   $/ft3               0.0283127014102352
!      (kg/s)/W               =>   (lbm/sec)/(Btu/hr)  0.646078115385742
!      1/K                    =>   1/F                 0.555555555555556
!      1/m                    =>   1/ft                0.3048
!      A/K                    =>   A/F                 0.555555555555556
!      C                      =>   F                   1.8 (plus 32)
!      cm                     =>   in                  0.3937
!      cm2                    =>   inch2               0.15500031000062
!      deltaC                 =>   deltaF              1.8
!      deltaC/hr              =>   deltaF/hr           1.8
!      deltaJ/kg              =>   deltaBtu/lb         0.0004299
!      g/GJ                   =>   lb/MWh              0.00793664091373665
!      g/kg                   =>   grains/lb           7
!      g/MJ                   =>   lb/MWh              7.93664091373665
!      g/mol                  =>   lb/mol              0.0022046
!      g/m-s                  =>   lb/ft-s             0.000671968949659
!      g/m-s-K                =>   lb/ft-s-F           0.000373574867724868
!      GJ                     =>   ton-hrs             78.9889415481832
!      J                      =>   Wh                  0.000277777777777778
!      J/K                    =>   Btu/F               526.565
!      J/kg                   =>   Btu/lb              0.00042986
!      J/kg-K                 =>   Btu/lb-F            0.000239005736137667
!      J/kg-K2                =>   Btu/lb-F2           0.000132889924714692
!      J/kg-K3                =>   Btu/lb-F3           7.38277359526066E-05
!      J/m2-K                 =>   Btu/ft2-F           4.89224766847393E-05
!      J/m3                   =>   Btu/ft3             2.68096514745308E-05
!      J/m3-K                 =>   Btu/ft3-F           1.49237004739337E-05
!      K                      =>   R                   1.8
!      K/m                    =>   F/ft                0.54861322767449
!      kg                     =>   lb                  2.2046
!      kg/J                   =>   lb/Btu              2325.83774250441
!      kg/kg-K                =>   lb/lb-F             0.555555555555556
!      kg/m                   =>   lb/ft               0.67196893069637
!      kg/m2                  =>   lb/ft2              0.204794053596664
!      kg/m3                  =>   lb/ft3              0.062428
!      kg/m-s                 =>   lb/ft-s             0.67196893069637
!      kg/m-s-K               =>   lb/ft-s-F           0.373316072609094
!      kg/m-s-K2              =>   lb/ft-s-F2          0.207397818116164
!      kg/Pa-s-m2             =>   lb/psi-s-ft2        1412.00523459398
!      kg/s                   =>   lb/s                2.20462247603796
!      kg/s2                  =>   lb/s2               2.2046
!      kg/s-m                 =>   lb/s-ft             0.67196893069637
!      kJ/kg                  =>   Btu/lb              0.429925
!      kPa                    =>   psi                 0.145038
!      L/day                  =>   pint/day            2.11337629827348
!      L/GJ                   =>   gal/kWh             0.000951022349025202
!      L/kWh                  =>   pint/kWh            2.11337629827348
!      L/MJ                   =>   gal/kWh             0.951022349025202
!      lux                    =>   foot-candles        0.092902267
!      m                      =>   ft                  3.28083989501312
!      m/hr                   =>   ft/hr               3.28083989501312
!      m/s                    =>   ft/min              196.850393700787
!      m/s                    =>   miles/hr            2.2369362920544
!      m/yr                   =>   inch/yr             39.3700787401575
!      m2                     =>   ft2                 10.7639104167097
!      m2/m                   =>   ft2/ft              3.28083989501312
!      m2/person              =>   ft2/person          10.764961
!      m2/s                   =>   ft2/s               10.7639104167097
!      m2-K/W                 =>   ft2-F-hr/Btu        5.678263
!      m3                     =>   ft3                 35.3146667214886
!      m3                     =>   gal                 264.172037284185
!      m3/GJ                  =>   ft3/MWh             127.13292
!      m3/hr                  =>   ft3/hr              35.3146667214886
!      m3/hr-m2               =>   ft3/hr-ft2          3.28083989501312
!      m3/hr-person           =>   ft3/hr-person       35.3146667214886
!      m3/kg                  =>   ft3/lb              16.018
!      m3/m2                  =>   ft3/ft2             3.28083989501312
!      m3/MJ                  =>   ft3/kWh             127.13292
!      m3/person              =>   ft3/person          35.3146667214886
!      m3/s                   =>   ft3/min             2118.88000328931
!      m3/s-m                 =>   ft3/min-ft          645.89
!      m3/s-m2                =>   ft3/min-ft2         196.85
!      m3/s-person            =>   ft3/min-person      2118.6438
!      m3/s-W                 =>   (ft3/min)/(Btu/h)   621.099127332943
!      N-m                    =>   lbf-in              8.85074900525547
!      N-s/m2                 =>   lbf-s/ft2           0.0208857913669065
!      Pa                     =>   psi                 0.000145037743897283
!      percent/K              =>   percent/F           0.555555555555556
!      person/m2              =>   person/ft2          0.0928939733269818
!      s/m                    =>   s/ft                0.3048
!      V/K                    =>   V/F                 0.555555555555556
!      W                      =>   Btu/h               3.4121412858518
!      W/((m3/s)-Pa)          =>   W/((gal/min)-ftH20) 0.188582274697355
!      W/((m3/s)-Pa)          =>   W/((ft3/min)-inH2O) 0.117556910599482
!      W/(m3/s)               =>   W/(ft3/min)         0.0004719475
!      W/K                    =>   Btu/h-F             1.89563404769544
!      W/m                    =>   Btu/h-ft            1.04072
!      W/m2                   =>   Btu/h-ft2           0.316957210776545
!      W/m2                   =>   W/ft2               0.09290304
!      W/m2-K                 =>   Btu/h-ft2-F         0.176110194261872
!      W/m2-K2                =>   Btu/h-ft2-F2        0.097826
!      W/m-K                  =>   Btu-in/h-ft2-F      6.93481276005548
!      W/m-K2                 =>   Btu/h-F2-ft         0.321418310071648
!      W/m-K3                 =>   Btu/h-F3-ft         0.178565727817582
!      W/person               =>   Btu/h-person        3.4121412858518
!
! Other conversions supported (needs the \ip-units code)
!
!      kPa                    =>   inHg                0.29523
!      m                      =>   in                  39.3700787401575
!      m3/hr                  =>   gal/hr              264.172037284185
!      m3/hr-m2               =>   gal/hr-ft2          24.5423853466941
!      m3/hr-person           =>   gal/hr-person       264.172037284185
!      m3/m2                  =>   gal/ft2             24.5423853466941
!      m3/person              =>   gal/person          264.172037284185
!      m3/s                   =>   gal/min             15850.3222370511
!      m3/s-m                 =>   gal/min-ft          4831.17821785317
!      m3/s-W                 =>   (gal/min)/(Btu/h)   4645.27137336702
!      Pa                     =>   ftH2O               0.00033455
!      Pa                     =>   inH2O               0.00401463
!      Pa                     =>   inHg                0.00029613
!      Pa                     =>   Pa                  1
!      W                      =>   W                   1
!      W/(m3/s)               =>   W/(gal/min)         0.0000630902
!      W/m2                   =>   W/m2                1
!      W/m-K                  =>   Btu/h-ft-F          0.577796066000163
!      W/person               =>   W/person            1
!
! Units fields that are not translated
!      $
!      1/hr
!      A
!      A/V
!      Ah
!      Availability
!      Control
!      cycles/hr
!      days
!      deg
!      dimensionless
!      eV
!      hr
!      J/J
!      kg/kg
!      kg-H2O/kg-air
!      kmol
!      kmol/s
!      m3/m3
!      micron
!      minutes
!      Mode
!      ms
!      ohms
!      percent
!      ppm
!      rev/min
!      s
!      V
!      VA
!      W/m2 or deg C
!      W/m2, W or deg C
!      W/s
!      W/W
!      years
! **************************************************************************
"""

# there are 3 kinds of conversions
# 1. no ip-units -> use 1st
# 2. expected ip-units -> use second
# 3. use the unit as is if it is in the 3rd category

SI = {
    "$": {"$": None, "defaultkey": "$"},
    "$/(W/K)": {"$/(Btu/h-F)": 0.52667614683731, "defaultkey": "$/(Btu/h-F)"},
    "$/(m3/s)": {"$/(ft3/min)": 0.000472000059660808, "defaultkey": "$/(ft3/min)"},
    "$/kW": {"$/(kBtuh/h)": 0.293083235638921, "defaultkey": "$/(kBtuh/h)"},
    "$/m2": {"$/ft2": 0.0928939733269818, "defaultkey": "$/ft2"},
    "$/m3": {"$/ft3": 0.0283127014102352, "defaultkey": "$/ft3"},
    "(kg/s)/W": {
        "(lbm/sec)/(Btu/hr)": 0.646078115385742,
        "defaultkey": "(lbm/sec)/(Btu/hr)",
    },
    "1/K": {"1/F": 0.555555555555556, "defaultkey": "1/F"},
    "1/hr": {"1/hr": None, "defaultkey": "1/hr"},
    "1/m": {"1/ft": 0.3048, "defaultkey": "1/ft"},
    "A": {"A": None, "defaultkey": "A"},
    "A/K": {"A/F": 0.555555555555556, "defaultkey": "A/F"},
    "A/V": {"A/V": None, "defaultkey": "A/V"},
    "Ah": {"Ah": None, "defaultkey": "Ah"},
    "Availability": {"Availability": None, "defaultkey": "Availability"},
    "C": {"C": None, "F": ["1.8", "(plus", "32)"], "defaultkey": "F"},
    "Control": {"Control": None, "defaultkey": "Control"},
    "GJ": {"defaultkey": "ton-hrs", "ton-hrs": 78.9889415481832},
    "J": {"Wh": 0.000277777777777778, "defaultkey": "Wh"},
    "J/J": {"J/J": None, "defaultkey": "J/J"},
    "J/K": {"Btu/F": 526.565, "defaultkey": "Btu/F"},
    "J/kg": {"Btu/lb": 0.00042986, "defaultkey": "Btu/lb"},
    "J/kg-K": {"Btu/lb-F": 0.000239005736137667, "defaultkey": "Btu/lb-F"},
    "J/kg-K2": {"Btu/lb-F2": 0.000132889924714692, "defaultkey": "Btu/lb-F2"},
    "J/kg-K3": {"Btu/lb-F3": 7.38277359526066e-05, "defaultkey": "Btu/lb-F3"},
    "J/m2-K": {"Btu/ft2-F": 4.89224766847393e-05, "defaultkey": "Btu/ft2-F"},
    "J/m3": {"Btu/ft3": 2.68096514745308e-05, "defaultkey": "Btu/ft3"},
    "J/m3-K": {"Btu/ft3-F": 1.49237004739337e-05, "defaultkey": "Btu/ft3-F"},
    "K": {"R": 1.8, "defaultkey": "R"},
    "K/m": {"F/ft": 0.54861322767449, "defaultkey": "F/ft"},
    "L/GJ": {"defaultkey": "gal/kWh", "gal/kWh": 0.000951022349025202},
    "L/MJ": {"defaultkey": "gal/kWh", "gal/kWh": 0.951022349025202},
    "L/day": {"defaultkey": "pint/day", "pint/day": 2.11337629827348},
    "L/kWh": {"defaultkey": "pint/kWh", "pint/kWh": 2.11337629827348},
    "Mode": {"Mode": None, "defaultkey": "Mode"},
    "N-m": {"defaultkey": "lbf-in", "lbf-in": 8.85074900525547},
    "N-s/m2": {"defaultkey": "lbf-s/ft2", "lbf-s/ft2": 0.0208857913669065},
    "Pa": {
        "Pa": 1.0,
        "defaultkey": "psi",
        "ftH2O": 0.00033455,
        "inH2O": 0.00401463,
        "inHg": 0.00029613,
        "psi": 0.000145037743897283,
    },
    "V": {"V": None, "defaultkey": "V"},
    "V/K": {"V/F": 0.555555555555556, "defaultkey": "V/F"},
    "VA": {"VA": None, "defaultkey": "VA"},
    "W": {"Btu/h": 3.4121412858518, "W": 1.0, "defaultkey": "Btu/h"},
    "W/((m3/s)-Pa)": {
        "W/((ft3/min)-inH2O)": 0.117556910599482,
        "W/((gal/min)-ftH20)": 0.188582274697355,
        "defaultkey": "W/((gal/min)-ftH20)",
    },
    "W/(m3/s)": {
        "W/(ft3/min)": 0.0004719475,
        "W/(gal/min)": 6.30902e-05,
        "defaultkey": "W/(ft3/min)",
    },
    "W/K": {"Btu/h-F": 1.89563404769544, "defaultkey": "Btu/h-F"},
    "W/W": {"W/W": None, "defaultkey": "W/W"},
    "W/m": {"Btu/h-ft": 1.04072, "defaultkey": "Btu/h-ft"},
    "W/m-K": {
        "Btu-in/h-ft2-F": 6.93481276005548,
        "Btu/h-ft-F": 0.577796066000163,
        "defaultkey": "Btu-in/h-ft2-F",
    },
    "W/m-K2": {"Btu/h-F2-ft": 0.321418310071648, "defaultkey": "Btu/h-F2-ft"},
    "W/m-K3": {"Btu/h-F3-ft": 0.178565727817582, "defaultkey": "Btu/h-F3-ft"},
    "W/m2": {
        "Btu/h-ft2": 0.316957210776545,
        "W/ft2": 0.09290304,
        "W/m2": 1.0,
        "defaultkey": "Btu/h-ft2",
    },
    "W/m2-K": {"Btu/h-ft2-F": 0.176110194261872, "defaultkey": "Btu/h-ft2-F"},
    "W/m2-K2": {"Btu/h-ft2-F2": 0.097826, "defaultkey": "Btu/h-ft2-F2"},
    "W/person": {
        "Btu/h-person": 3.4121412858518,
        "W/person": 1.0,
        "defaultkey": "Btu/h-person",
    },
    "W/s": {"W/s": None, "defaultkey": "W/s"},
    "cm": {"defaultkey": "in", "in": 0.3937},
    "cm2": {"defaultkey": "inch2", "inch2": 0.15500031000062},
    "cycles/hr": {"cycles/hr": None, "defaultkey": "cycles/hr"},
    "days": {"days": None, "defaultkey": "days"},
    "deg": {"defaultkey": "deg", "deg": None},
    "deltaC": {"defaultkey": "deltaF", "deltaF": 1.8},
    "deltaC/hr": {"defaultkey": "deltaF/hr", "deltaF/hr": 1.8},
    "deltaJ/kg": {"defaultkey": "deltaBtu/lb", "deltaBtu/lb": 0.0004299},
    "dimensionless": {"defaultkey": "dimensionless", "dimensionless": None},
    "eV": {"defaultkey": "eV", "eV": None},
    "g/GJ": {"defaultkey": "lb/MWh", "lb/MWh": 0.00793664091373665},
    "g/MJ": {"defaultkey": "lb/MWh", "lb/MWh": 7.93664091373665},
    "g/kg": {"defaultkey": "grains/lb", "grains/lb": 7.0},
    "g/m-s": {"defaultkey": "lb/ft-s", "lb/ft-s": 0.000671968949659},
    "g/m-s-K": {"defaultkey": "lb/ft-s-F", "lb/ft-s-F": 0.000373574867724868},
    "g/mol": {"defaultkey": "lb/mol", "lb/mol": 0.0022046},
    "hr": {"defaultkey": "hr", "hr": None},
    "kJ/kg": {"Btu/lb": 0.429925, "defaultkey": "Btu/lb"},
    "kPa": {"defaultkey": "psi", "inHg": 0.29523, "psi": 0.145038},
    "kg": {"defaultkey": "lb", "lb": 2.2046},
    "kg-H2O/kg-air": {"defaultkey": "kg-H2O/kg-air", "kg-H2O/kg-air": None},
    "kg/J": {"defaultkey": "lb/Btu", "lb/Btu": 2325.83774250441},
    "kg/Pa-s-m2": {"defaultkey": "lb/psi-s-ft2", "lb/psi-s-ft2": 1412.00523459398},
    "kg/kg": {"defaultkey": "kg/kg", "kg/kg": None},
    "kg/kg-K": {"defaultkey": "lb/lb-F", "lb/lb-F": 0.555555555555556},
    "kg/m": {"defaultkey": "lb/ft", "lb/ft": 0.67196893069637},
    "kg/m-s": {"defaultkey": "lb/ft-s", "lb/ft-s": 0.67196893069637},
    "kg/m-s-K": {"defaultkey": "lb/ft-s-F", "lb/ft-s-F": 0.373316072609094},
    "kg/m-s-K2": {"defaultkey": "lb/ft-s-F2", "lb/ft-s-F2": 0.207397818116164},
    "kg/m2": {"defaultkey": "lb/ft2", "lb/ft2": 0.204794053596664},
    "kg/m3": {"defaultkey": "lb/ft3", "lb/ft3": 0.062428},
    "kg/s": {"defaultkey": "lb/s", "lb/s": 2.20462247603796},
    "kg/s-m": {"defaultkey": "lb/s-ft", "lb/s-ft": 0.67196893069637},
    "kg/s2": {"defaultkey": "lb/s2", "lb/s2": 2.2046},
    "kmol": {"defaultkey": "kmol", "kmol": None},
    "kmol/s": {"defaultkey": "kmol/s", "kmol/s": None},
    "lux": {"defaultkey": "foot-candles", "foot-candles": 0.092902267},
    "m": {"defaultkey": "ft", "ft": 3.28083989501312, "in": 39.3700787401575},
    "m/hr": {"defaultkey": "ft/hr", "ft/hr": 3.28083989501312},
    "m/s": {
        "defaultkey": "ft/min",
        "ft/min": 196.850393700787,
        "miles/hr": 2.2369362920544,
    },
    "m/yr": {"defaultkey": "inch/yr", "inch/yr": 39.3700787401575},
    "m2": {"defaultkey": "ft2", "ft2": 10.7639104167097},
    "m2-K/W": {"defaultkey": "ft2-F-hr/Btu", "ft2-F-hr/Btu": 5.678263},
    "m2/m": {"defaultkey": "ft2/ft", "ft2/ft": 3.28083989501312},
    "m2/person": {"defaultkey": "ft2/person", "ft2/person": 10.764961},
    "m2/s": {"defaultkey": "ft2/s", "ft2/s": 10.7639104167097},
    "m3": {"defaultkey": "ft3", "ft3": 35.3146667214886, "gal": 264.172037284185},
    "m3/GJ": {"defaultkey": "ft3/MWh", "ft3/MWh": 127.13292},
    "m3/MJ": {"defaultkey": "ft3/kWh", "ft3/kWh": 127.13292},
    "m3/hr": {
        "defaultkey": "ft3/hr",
        "ft3/hr": 35.3146667214886,
        "gal/hr": 264.172037284185,
    },
    "m3/hr-m2": {
        "defaultkey": "ft3/hr-ft2",
        "ft3/hr-ft2": 3.28083989501312,
        "gal/hr-ft2": 24.5423853466941,
    },
    "m3/hr-person": {
        "defaultkey": "ft3/hr-person",
        "ft3/hr-person": 35.3146667214886,
        "gal/hr-person": 264.172037284185,
    },
    "m3/kg": {"defaultkey": "ft3/lb", "ft3/lb": 16.018},
    "m3/m2": {
        "defaultkey": "ft3/ft2",
        "ft3/ft2": 3.28083989501312,
        "gal/ft2": 24.5423853466941,
    },
    "m3/m3": {"defaultkey": "m3/m3", "m3/m3": None},
    "m3/person": {
        "defaultkey": "ft3/person",
        "ft3/person": 35.3146667214886,
        "gal/person": 264.172037284185,
    },
    "m3/s": {
        "defaultkey": "ft3/min",
        "ft3/min": 2118.88000328931,
        "gal/min": 15850.3222370511,
    },
    "m3/s-W": {
        "(ft3/min)/(Btu/h)": 621.099127332943,
        "(gal/min)/(Btu/h)": 4645.27137336702,
        "defaultkey": "(ft3/min)/(Btu/h)",
    },
    "m3/s-m": {
        "defaultkey": "ft3/min-ft",
        "ft3/min-ft": 645.89,
        "gal/min-ft": 4831.17821785317,
    },
    "m3/s-m2": {"defaultkey": "ft3/min-ft2", "ft3/min-ft2": 196.85},
    "m3/s-person": {"defaultkey": "ft3/min-person", "ft3/min-person": 2118.6438},
    "micron": {"defaultkey": "micron", "micron": None},
    "minutes": {"defaultkey": "minutes", "minutes": None},
    "ms": {"defaultkey": "ms", "ms": None},
    "ohms": {"defaultkey": "ohms", "ohms": None},
    "percent": {"defaultkey": "percent", "percent": None},
    "percent/K": {"defaultkey": "percent/F", "percent/F": 0.555555555555556},
    "person/m2": {"defaultkey": "person/ft2", "person/ft2": 0.0928939733269818},
    "ppm": {"defaultkey": "ppm", "ppm": None},
    "rev/min": {"defaultkey": "rev/min", "rev/min": None},
    "s": {"defaultkey": "s", "s": None},
    "s/m": {"defaultkey": "s/ft", "s/ft": 0.3048},
    "years": {"defaultkey": "years", "years": None},
}

IP = {
    "$": {"$": None, "defaultkey": "$"},
    "$/(Btu/h-F)": {"$/(W/K)": 0.52667614683731, "defaultkey": "$/(W/K)"},
    "$/(ft3/min)": {"$/(m3/s)": 0.000472000059660808, "defaultkey": "$/(m3/s)"},
    "$/(kBtuh/h)": {"$/kW": 0.293083235638921, "defaultkey": "$/kW"},
    "$/ft2": {"$/m2": 0.0928939733269818, "defaultkey": "$/m2"},
    "$/ft3": {"$/m3": 0.0283127014102352, "defaultkey": "$/m3"},
    "(ft3/min)/(Btu/h)": {"defaultkey": "m3/s-W", "m3/s-W": 621.099127332943},
    "(gal/min)/(Btu/h)": {"defaultkey": "m3/s-W", "m3/s-W": 4645.27137336702},
    "(lbm/sec)/(Btu/hr)": {"(kg/s)/W": 0.646078115385742, "defaultkey": "(kg/s)/W"},
    "1/F": {"1/K": 0.555555555555556, "defaultkey": "1/K"},
    "1/ft": {"1/m": 0.3048, "defaultkey": "1/m"},
    "1/hr": {"1/hr": None, "defaultkey": "1/hr"},
    "A": {"A": None, "defaultkey": "A"},
    "A/F": {"A/K": 0.555555555555556, "defaultkey": "A/K"},
    "A/V": {"A/V": None, "defaultkey": "A/V"},
    "Ah": {"Ah": None, "defaultkey": "Ah"},
    "Availability": {"Availability": None, "defaultkey": "Availability"},
    "Btu-in/h-ft2-F": {"W/m-K": 6.93481276005548, "defaultkey": "W/m-K"},
    "Btu/F": {"J/K": 526.565, "defaultkey": "J/K"},
    "Btu/ft2-F": {"J/m2-K": 4.89224766847393e-05, "defaultkey": "J/m2-K"},
    "Btu/ft3": {"J/m3": 2.68096514745308e-05, "defaultkey": "J/m3"},
    "Btu/ft3-F": {"J/m3-K": 1.49237004739337e-05, "defaultkey": "J/m3-K"},
    "Btu/h": {"W": 3.4121412858518, "defaultkey": "W"},
    "Btu/h-F": {"W/K": 1.89563404769544, "defaultkey": "W/K"},
    "Btu/h-F2-ft": {"W/m-K2": 0.321418310071648, "defaultkey": "W/m-K2"},
    "Btu/h-F3-ft": {"W/m-K3": 0.178565727817582, "defaultkey": "W/m-K3"},
    "Btu/h-ft": {"W/m": 1.04072, "defaultkey": "W/m"},
    "Btu/h-ft-F": {"W/m-K": 0.577796066000163, "defaultkey": "W/m-K"},
    "Btu/h-ft2": {"W/m2": 0.316957210776545, "defaultkey": "W/m2"},
    "Btu/h-ft2-F": {"W/m2-K": 0.176110194261872, "defaultkey": "W/m2-K"},
    "Btu/h-ft2-F2": {"W/m2-K2": 0.097826, "defaultkey": "W/m2-K2"},
    "Btu/h-person": {"W/person": 3.4121412858518, "defaultkey": "W/person"},
    "Btu/lb": {"J/kg": 0.00042986, "defaultkey": "J/kg", "kJ/kg": 0.429925},
    "Btu/lb-F": {"J/kg-K": 0.000239005736137667, "defaultkey": "J/kg-K"},
    "Btu/lb-F2": {"J/kg-K2": 0.000132889924714692, "defaultkey": "J/kg-K2"},
    "Btu/lb-F3": {"J/kg-K3": 7.38277359526066e-05, "defaultkey": "J/kg-K3"},
    "C": {"C": None, "defaultkey": "C"},
    "Control": {"Control": None, "defaultkey": "Control"},
    "F": {"C": ["1.8", "(plus", "32)"], "defaultkey": "C"},
    "F/ft": {"K/m": 0.54861322767449, "defaultkey": "K/m"},
    "J/J": {"J/J": None, "defaultkey": "J/J"},
    "Mode": {"Mode": None, "defaultkey": "Mode"},
    "Pa": {"Pa": 1.0, "defaultkey": "Pa"},
    "R": {"K": 1.8, "defaultkey": "K"},
    "V": {"V": None, "defaultkey": "V"},
    "V/F": {"V/K": 0.555555555555556, "defaultkey": "V/K"},
    "VA": {"VA": None, "defaultkey": "VA"},
    "W": {"W": 1.0, "defaultkey": "W"},
    "W/((ft3/min)-inH2O)": {
        "W/((m3/s)-Pa)": 0.117556910599482,
        "defaultkey": "W/((m3/s)-Pa)",
    },
    "W/((gal/min)-ftH20)": {
        "W/((m3/s)-Pa)": 0.188582274697355,
        "defaultkey": "W/((m3/s)-Pa)",
    },
    "W/(ft3/min)": {"W/(m3/s)": 0.0004719475, "defaultkey": "W/(m3/s)"},
    "W/(gal/min)": {"W/(m3/s)": 6.30902e-05, "defaultkey": "W/(m3/s)"},
    "W/W": {"W/W": None, "defaultkey": "W/W"},
    "W/ft2": {"W/m2": 0.09290304, "defaultkey": "W/m2"},
    "W/m2": {"W/m2": 1.0, "defaultkey": "W/m2"},
    "W/person": {"W/person": 1.0, "defaultkey": "W/person"},
    "W/s": {"W/s": None, "defaultkey": "W/s"},
    "Wh": {"J": 0.000277777777777778, "defaultkey": "J"},
    "cycles/hr": {"cycles/hr": None, "defaultkey": "cycles/hr"},
    "days": {"days": None, "defaultkey": "days"},
    "deg": {"defaultkey": "deg", "deg": None},
    "deltaBtu/lb": {"defaultkey": "deltaJ/kg", "deltaJ/kg": 0.0004299},
    "deltaF": {"defaultkey": "deltaC", "deltaC": 1.8},
    "deltaF/hr": {"defaultkey": "deltaC/hr", "deltaC/hr": 1.8},
    "dimensionless": {"defaultkey": "dimensionless", "dimensionless": None},
    "eV": {"defaultkey": "eV", "eV": None},
    "foot-candles": {"defaultkey": "lux", "lux": 0.092902267},
    "ft": {"defaultkey": "m", "m": 3.28083989501312},
    "ft/hr": {"defaultkey": "m/hr", "m/hr": 3.28083989501312},
    "ft/min": {"defaultkey": "m/s", "m/s": 196.850393700787},
    "ft2": {"defaultkey": "m2", "m2": 10.7639104167097},
    "ft2-F-hr/Btu": {"defaultkey": "m2-K/W", "m2-K/W": 5.678263},
    "ft2/ft": {"defaultkey": "m2/m", "m2/m": 3.28083989501312},
    "ft2/person": {"defaultkey": "m2/person", "m2/person": 10.764961},
    "ft2/s": {"defaultkey": "m2/s", "m2/s": 10.7639104167097},
    "ft3": {"defaultkey": "m3", "m3": 35.3146667214886},
    "ft3/MWh": {"defaultkey": "m3/GJ", "m3/GJ": 127.13292},
    "ft3/ft2": {"defaultkey": "m3/m2", "m3/m2": 3.28083989501312},
    "ft3/hr": {"defaultkey": "m3/hr", "m3/hr": 35.3146667214886},
    "ft3/hr-ft2": {"defaultkey": "m3/hr-m2", "m3/hr-m2": 3.28083989501312},
    "ft3/hr-person": {"defaultkey": "m3/hr-person", "m3/hr-person": 35.3146667214886},
    "ft3/kWh": {"defaultkey": "m3/MJ", "m3/MJ": 127.13292},
    "ft3/lb": {"defaultkey": "m3/kg", "m3/kg": 16.018},
    "ft3/min": {"defaultkey": "m3/s", "m3/s": 2118.88000328931},
    "ft3/min-ft": {"defaultkey": "m3/s-m", "m3/s-m": 645.89},
    "ft3/min-ft2": {"defaultkey": "m3/s-m2", "m3/s-m2": 196.85},
    "ft3/min-person": {"defaultkey": "m3/s-person", "m3/s-person": 2118.6438},
    "ft3/person": {"defaultkey": "m3/person", "m3/person": 35.3146667214886},
    "ftH2O": {"Pa": 0.00033455, "defaultkey": "Pa"},
    "gal": {"defaultkey": "m3", "m3": 264.172037284185},
    "gal/ft2": {"defaultkey": "m3/m2", "m3/m2": 24.5423853466941},
    "gal/hr": {"defaultkey": "m3/hr", "m3/hr": 264.172037284185},
    "gal/hr-ft2": {"defaultkey": "m3/hr-m2", "m3/hr-m2": 24.5423853466941},
    "gal/hr-person": {"defaultkey": "m3/hr-person", "m3/hr-person": 264.172037284185},
    "gal/kWh": {
        "L/GJ": 0.000951022349025202,
        "L/MJ": 0.951022349025202,
        "defaultkey": "L/GJ",
    },
    "gal/min": {"defaultkey": "m3/s", "m3/s": 15850.3222370511},
    "gal/min-ft": {"defaultkey": "m3/s-m", "m3/s-m": 4831.17821785317},
    "gal/person": {"defaultkey": "m3/person", "m3/person": 264.172037284185},
    "grains/lb": {"defaultkey": "g/kg", "g/kg": 7.0},
    "hr": {"defaultkey": "hr", "hr": None},
    "in": {"cm": 0.3937, "defaultkey": "cm", "m": 39.3700787401575},
    "inH2O": {"Pa": 0.00401463, "defaultkey": "Pa"},
    "inHg": {"Pa": 0.00029613, "defaultkey": "kPa", "kPa": 0.29523},
    "inch/yr": {"defaultkey": "m/yr", "m/yr": 39.3700787401575},
    "inch2": {"cm2": 0.15500031000062, "defaultkey": "cm2"},
    "kg-H2O/kg-air": {"defaultkey": "kg-H2O/kg-air", "kg-H2O/kg-air": None},
    "kg/kg": {"defaultkey": "kg/kg", "kg/kg": None},
    "kmol": {"defaultkey": "kmol", "kmol": None},
    "kmol/s": {"defaultkey": "kmol/s", "kmol/s": None},
    "lb": {"defaultkey": "kg", "kg": 2.2046},
    "lb/Btu": {"defaultkey": "kg/J", "kg/J": 2325.83774250441},
    "lb/MWh": {
        "defaultkey": "g/GJ",
        "g/GJ": 0.00793664091373665,
        "g/MJ": 7.93664091373665,
    },
    "lb/ft": {"defaultkey": "kg/m", "kg/m": 0.67196893069637},
    "lb/ft-s": {
        "defaultkey": "g/m-s",
        "g/m-s": 0.000671968949659,
        "kg/m-s": 0.67196893069637,
    },
    "lb/ft-s-F": {
        "defaultkey": "g/m-s-K",
        "g/m-s-K": 0.000373574867724868,
        "kg/m-s-K": 0.373316072609094,
    },
    "lb/ft-s-F2": {"defaultkey": "kg/m-s-K2", "kg/m-s-K2": 0.207397818116164},
    "lb/ft2": {"defaultkey": "kg/m2", "kg/m2": 0.204794053596664},
    "lb/ft3": {"defaultkey": "kg/m3", "kg/m3": 0.062428},
    "lb/lb-F": {"defaultkey": "kg/kg-K", "kg/kg-K": 0.555555555555556},
    "lb/mol": {"defaultkey": "g/mol", "g/mol": 0.0022046},
    "lb/psi-s-ft2": {"defaultkey": "kg/Pa-s-m2", "kg/Pa-s-m2": 1412.00523459398},
    "lb/s": {"defaultkey": "kg/s", "kg/s": 2.20462247603796},
    "lb/s-ft": {"defaultkey": "kg/s-m", "kg/s-m": 0.67196893069637},
    "lb/s2": {"defaultkey": "kg/s2", "kg/s2": 2.2046},
    "lbf-in": {"N-m": 8.85074900525547, "defaultkey": "N-m"},
    "lbf-s/ft2": {"N-s/m2": 0.0208857913669065, "defaultkey": "N-s/m2"},
    "m3/m3": {"defaultkey": "m3/m3", "m3/m3": None},
    "micron": {"defaultkey": "micron", "micron": None},
    "miles/hr": {"defaultkey": "m/s", "m/s": 2.2369362920544},
    "minutes": {"defaultkey": "minutes", "minutes": None},
    "ms": {"defaultkey": "ms", "ms": None},
    "ohms": {"defaultkey": "ohms", "ohms": None},
    "percent": {"defaultkey": "percent", "percent": None},
    "percent/F": {"defaultkey": "percent/K", "percent/K": 0.555555555555556},
    "person/ft2": {"defaultkey": "person/m2", "person/m2": 0.0928939733269818},
    "pint/day": {"L/day": 2.11337629827348, "defaultkey": "L/day"},
    "pint/kWh": {"L/kWh": 2.11337629827348, "defaultkey": "L/kWh"},
    "ppm": {"defaultkey": "ppm", "ppm": None},
    "psi": {"Pa": 0.000145037743897283, "defaultkey": "kPa", "kPa": 0.145038},
    "rev/min": {"defaultkey": "rev/min", "rev/min": None},
    "s": {"defaultkey": "s", "s": None},
    "s/ft": {"defaultkey": "s/m", "s/m": 0.3048},
    "ton-hrs": {"GJ": 78.9889415481832, "defaultkey": "GJ"},
    "years": {"defaultkey": "years", "years": None},
}


def getconversions(txt=TXT):
    """create the conversion data structure"""
    msp = txt.split("!\n")
    c1 = msp[0].splitlines()
    c1.pop(0)

    si = dict()
    ip = dict()

    for c in c1:
        cc = c.split()
        cc.pop(0)
        cc.pop(1)
        try:
            si.setdefault(cc[0], []).append((cc[1], float(cc[-1])))
            ip.setdefault(cc[1], []).append((cc[0], float(cc[-1])))
        except ValueError as e:
            si.setdefault(cc[0], []).append((cc[1], cc[2:]))
            ip.setdefault(cc[1], []).append((cc[0], cc[2:]))
    c1 = msp[2].splitlines()
    for c in c1:
        cc = c.split()
        cc.pop(0)
        cc.pop(1)
        try:
            si.setdefault(cc[0], []).append((cc[1], float(cc[-1])))
            ip.setdefault(cc[1], []).append((cc[0], float(cc[-1])))
        except ValueError as e:
            si.setdefault(cc[0], []).append((cc[1], cc[2:]))
            ip.setdefault(cc[1], []).append((cc[0], cc[2:]))
    c2 = msp[3].splitlines()
    c2.pop(0)
    c2.pop(-1)
    for c in [c.split()[-1] for c in c2]:
        si.setdefault(c, []).append((c, None))
        ip.setdefault(c, []).append((c, None))
    return setdefaultindct(si), setdefaultindct(ip)


def setdefaultindct(dct):
    newdct = {}
    for key in dct:
        d = dict(defaultkey=dct[key][0][0])
        d.update(dict(dct[key]))
        newdct[key] = d
    return newdct


def convert2ip(val, siunits, ipunits=None, unitstr=True, wrapin=None):
    """convert val from si units to ip units
    It can also return a unit string wrapped in something like `[ft]`"""
    # calculates the new value
    # get conversion factor
    if not siunits:
        conv = 1
    elif siunits not in SI:
        conv = 1
    elif not ipunits:
        default = SI[siunits]["defaultkey"]
        conv = SI[siunits][default]
    else:
        conv = SI[siunits][ipunits]

    # do conversion
    new_val = doconversion(val, conv)

    # make the unit string
    ustr = ""
    if unitstr:
        if not siunits:
            ustr = ""
        elif siunits not in SI:
            ustr = siunits
        elif ipunits:
            ustr = ipunits
        else:
            ustr = default
        # wrap the unitstr
        if not wrapin:
            wrapin = "X"
        elif ustr:
            ustr = wrapin.replace("X", ustr)
        else:
            pass

    # return the results
    if unitstr:
        return new_val, ustr
    else:
        return new_val


def convert2si(val, ipunits, siunits=None, unitstr=True, wrapin=None):
    """keep the si units
    It can also return a unit string wrapped in something like `[C]`"""
    # calculates the new value
    # get conversion factor
    if not ipunits:
        conv = 1
    elif ipunits not in IP:
        conv = 1
    elif not siunits:
        default = IP[ipunits]["defaultkey"]
        conv = IP[ipunits][default]
    else:
        conv = IP[ipunits][siunits]

    # do conversion
    new_val = doconversion(val, conv, reverse=True)

    # make the unit string
    ustr = ""
    if unitstr:
        if not ipunits:
            ustr = ""
        elif ipunits not in IP:
            ustr = ipunits
        elif siunits:
            ustr = siunits
        else:
            ustr = default
        # wrap the unitstr
        if not wrapin:
            wrapin = "X"
        elif ustr:
            ustr = wrapin.replace("X", ustr)
        else:
            pass

    # return the results
    if unitstr:
        return new_val, ustr
    else:
        return new_val


def doconversion(val, conv, reverse=False):
    if reverse:
        try:
            conv = 1 / conv
        except TypeError as e:
            pass
    try:
        if conv == ["1.8", "(plus", "32)"]:
            if reverse:
                new_val = (val - 32) / 1.8
            else:
                new_val = (val * 1.8) + 32
        else:
            new_val = val * conv
    except TypeError as e:
        new_val = val
    return new_val


def allsiunits():
    """return a list of all SI units"""
    return list(SI.keys())


def allipunits():
    """return a list of all the IP units"""
    return list(IP.keys())


def getipunits(siunit):
    """return all the ip units avaliable for this si unit"""
    dct = dict(SI[siunit])
    dct.pop("defaultkey")
    return list(dct.keys())


def noconversion(val, siunits, unitstr=True, wrapin=None):
    """make no conversion.
    Used to put the correct units in place"""
    # calculates the new value
    # get conversion factor
    #     if not siunits:
    #         conv = 1
    #     elif siunits not in SI:
    #         conv = 1
    #     elif not ipunits:
    #         default = SI[siunits]["defaultkey"]
    #         conv = SI[siunits][default]
    #     else:
    #         conv = SI[siunits][ipunits]

    # do conversion
    # new_val = doconversion(val, conv)
    new_val = val

    # make the unit string
    ustr = ""
    if unitstr:
        if not siunits:
            ustr = ""
        else:
            ustr = siunits

        # wrap the unitstr
        if not wrapin:
            wrapin = "X"
        elif ustr:
            ustr = wrapin.replace("X", ustr)
        else:
            pass

    # return the results
    if unitstr:
        return new_val, ustr
    else:
        return new_val


# functions needed:
#
# DONE
# - convert2ip(val, siunits, ipunits=None, unitstr=True, wrapin='[]')
# - convert2si(val, ipunits, siunits=None, unitstr=True, wrapin='[]')
# - allsiunits()
# - allipunits()
# TODO
# - getipunits(siunit)
# - getsiunits(ipunit)
# - getconversioncategories() # length, volume, u-value etc (make this manually using schema.epJSON)
#
# code to get the categories of the units
# extract and hand edit
# epj = read an epj file
# dd = {}
# for kkey in epj.epschema.epschemaobjects:
#     o = epj.epschema.epschemaobjects[kkey]
#     for key in o:
#         if 'units' in o[key]:
#             cat = o[key]['units']
#             print(key, cat)
#             dd.setdefault(cat, []).append(key)
#
# for key in dd:
#     for item in dd[key]:
#         print(f"{key},{item}")
