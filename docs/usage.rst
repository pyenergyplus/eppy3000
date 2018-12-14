=====
Usage
=====

Read the file
-------------

To use eppy3000 in a project::

    from eppy3000.modelmaker import IDF

    fname = "./eppy3000/resources/snippets/V8_9/a.epJSON"
    idf = IDF(fname)

    print(idf.idfobjects['AirLoopHVAC'][0]) # print formattin is slightly broken


Use the dot syntax
------------------

Or in more detail::

    from eppy3000.modelmaker import IDF
    from io import StringIO

    txt = """
    {
        "Building": {
            "Bldg": {
                "idf_max_extensible_fields": 0,
                "idf_max_fields": 8,
                "idf_order": 3,
                "loads_convergence_tolerance_value": 0.05,
                "maximum_number_of_warmup_days": 30,
                "minimum_number_of_warmup_days": 6,
                "north_axis": 0.0,
                "solar_distribution": "MinimalShadowing",
                "temperature_convergence_tolerance_value": 0.05,
                "terrain": "Suburbs"
            }
        }
    }
    """

    sio = StringIO(txt)
    idf = IDF(sio)
    abuilding = idf.idf.Building.Bldg
    print(abuilding.solar_distribution)
    print(abuilding.terrain)

    > MinimalShadowing
    > Suburbs

    print(abuilding)

    > Building                                 !-  KEY
    >     Bldg                                 !-  NAME
    >     0                                    !-  idf_max_extensible_fields
    >     8                                    !-  idf_max_fields
    >     3                                    !-  idf_order
    >     0.05                                 !-  loads_convergence_tolerance_value
    >     30                                   !-  maximum_number_of_warmup_days
    >     6                                    !-  minimum_number_of_warmup_days
    >     0.0                                  !-  north_axis
    >     MinimalShadowing                     !-  solar_distribution
    >     0.05                                 !-  temperature_convergence_tolerance_value
    >     Suburbs                              !-  terrain
    >


IDF.idfobjects[key]
-------------------

You can use idfobjects like in eppy::

    buildings = idf.idfobjects["Building"]
    abuilding = buildings[0]
    print(abuilding.terrain)

    > Suburbs

Other IDF functions
-------------------

The following function also work:

- IDF.save()
- IDF.saveas()

