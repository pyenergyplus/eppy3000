TXT = """! Default IP conversions (no \ip-units necessary)
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


def getconversions(msp=TXT):
    msp = TXT.split("!\n")
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
    return si, ip


def setdefault(dct):
    newdct = {}
    for key in dct:
        d = dict(defaultkey=dct[key][0][0])
        d.update(dict(dct[key]))
        print(d)
        newdct[key] = d
    return newdct
