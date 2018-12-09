=====
Usage
=====

Read the file
-------------

To use eppy3000 in a project::

    import eppy3000.readidf.readidfjson as readidfjson
    idf = readidfjson('pathtofile/filename.epJSON')


Use the dot syntax
------------------

Or in more detail::

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
    idf = readidfjson(sio)
    abuilding = idf.Building.Bldg
    print(abuilding.solar_distribution)
    print(abuilding.terrain)
    
    >> MinimalShadowing
    >> Suburbs