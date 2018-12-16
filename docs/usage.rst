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


Accessing the IDD
-----------------

Note that you have been opening the IDF file without referring to the IDD file. You can also open the IDF file with an IDD file. The code would look like this::

    from eppy3000.modelmaker import IDF
    from pprint import pprint

    iddfname = "/Applications/EnergyPlus-8-9-0/Energy+.schema.epJSON"
    fname = "./eppy3000/resources/snippets/V8_9/a.epJSON"
    idf = IDF(idfname=fname, iddname=iddfname)
    print(idf.idfobjects['AirLoopHVAC'][0])
    
    > AirLoopHVAC                              !-  KEY
    >     CRAC system                          !-  NAME
    >     CRAC 1 Availability List             !-  availability_manager_list_name
    >     Air Loop Branches                    !-  branch_list_name
    >     Zone Equipment Inlet Node            !-  demand_side_inlet_node_names
    >     Zone Equipment Outlet Node           !-  demand_side_outlet_node_name
    >     8.5                                  !-  design_supply_air_flow_rate
    >     0                                    !-  idf_max_extensible_fields
    >     10                                   !-  idf_max_fields
    >     31                                   !-  idf_order
    >     Supply Inlet Node                    !-  supply_side_inlet_node_name
    >     Supply Outlet Node                   !-  supply_side_outlet_node_names
    
Now you have access to the IDD variables::

    pprint(idf.idd.iddobjects['AirLoopHVAC'].fieldnames())
    
    > ['branch_list_name',
    >  'demand_side_outlet_node_name',
    >  'supply_side_outlet_node_names',
    >  'connector_list_name',
    >  'design_return_air_flow_fraction_of_supply_air_flow',
    >  'controller_list_name',
    >  'availability_manager_list_name',
    >  'demand_side_inlet_node_names',
    >  'supply_side_inlet_node_name',
    >  'design_supply_air_flow_rate']
    
You can look at the property of a particular fieldname::

    pprint(idf.idd.iddobjects['AirLoopHVAC'].fieldproperty('branch_list_name))
    
    > {'data_type': 'object_list',
    >  'note': 'Name of a BranchList containing all the branches in this air loop',
    >  'object_list': ['BranchLists'],
    >  'type': 'string'}



