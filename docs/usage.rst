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

You can also access the IDD for an IDF object from within the IDF object::

    cracsystem = idf.idfobjects['AirLoopHVAC'][0]
    pprint(crac.eppy_objidd.fieldnames())
    print()
    pprint(crac.eppy_objidd.fieldproperty('demand_side_inlet_node_names'))

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
    >
    > {'note': 'Name of a Node or NodeList containing the inlet node(s) supplying '
    >          'air to zone equipment.',
    >  'type': 'string'}


Nested lists or arrays as fields
--------------------------------

The old E+ had objects with a flat list of fields. As a result some objects needed repeating or extensible fields. An example of repeating/extensible fields are the coordinates in the object `BuildingSurface:Detailed`. These are the coordinates of the surface and the number of fields can vary depending on the shape of the surface.

The new JSON format treats the extensible fields as an array (an array in json and a list in python). Let us explore how to access and modify these list in eppy3000. Let us look at a single surface::

    txt = """
    {
        "BuildingSurface:Detailed": {
            "Zn001:Flr001": {
                "construction_name": "FLOOR",
                "idf_max_extensible_fields": 12,
                "idf_max_fields": 22,
                "idf_order": 27,
                "number_of_vertices": 4,
                "outside_boundary_condition": "Surface",
                "outside_boundary_condition_object": "Zn001:Flr001",
                "sun_exposure": "NoSun",
                "surface_type": "Floor",
                "vertices": [
                    {
                        "vertex_x_coordinate": 15.24,
                        "vertex_y_coordinate": 0.0,
                        "vertex_z_coordinate": 0.0
                    },
                    {
                        "vertex_x_coordinate": 0.0,
                        "vertex_y_coordinate": 0.0,
                        "vertex_z_coordinate": 0.0
                    },
                    {
                        "vertex_x_coordinate": 0.0,
                        "vertex_y_coordinate": 15.24,
                        "vertex_z_coordinate": 0.0
                    },
                    {
                        "vertex_x_coordinate": 15.24,
                        "vertex_y_coordinate": 15.24,
                        "vertex_z_coordinate": 0.0
                    }
                ],
                "view_factor_to_ground": 1.0,
                "wind_exposure": "NoWind",
                "zone_name": "Main Zone"
            }
        }
    }"""

Let us open this as an IDF()::

    from io import StringIO
    from eppy3000.modelmaker import IDF
    from pprint iport pprint

    fhandle = StringIO(txt)
    idf = IDF(idfname=fhandle, iddname=iddfname)
    print(idf)


    > BuildingSurface:Detailed                         !-  KEY
    >             Zn001:Flr001                         !-  NAME
    >             FLOOR                                !-  construction_name
    >             12                                   !-  idf_max_extensible_fields
    >             22                                   !-  idf_max_fields
    >             27                                   !-  idf_order
    >             4                                    !-  number_of_vertices
    >             Surface                              !-  outside_boundary_condition
    >             Zn001:Flr001                         !-  outside_boundary_condition_object
    >             NoSun                                !-  sun_exposure
    >             Floor                                !-  surface_type
    >                                                  !-  vertices
    >                 15.24                                !-  vertex_x_coordinate #1
    >                 0.0                                  !-  vertex_y_coordinate #1
    >                 0.0                                  !-  vertex_z_coordinate #1
    >                 0.0                                  !-  vertex_x_coordinate #2
    >                 0.0                                  !-  vertex_y_coordinate #2
    >                 0.0                                  !-  vertex_z_coordinate #2
    >                 0.0                                  !-  vertex_x_coordinate #3
    >                 15.24                                !-  vertex_y_coordinate #3
    >                 0.0                                  !-  vertex_z_coordinate #3
    >                 15.24                                !-  vertex_x_coordinate #4
    >                 15.24                                !-  vertex_y_coordinate #4
    >                 0.0                                  !-  vertex_z_coordinate #4
    >             1.0                                  !-  view_factor_to_ground
    >             NoWind                               !-  wind_exposure
    >             Main Zone                            !-  zone_name

Notice how the array items are inset. How dow we access the array items ?

Let us print the field names of `BuildingSurface:Detailed` object::

    surfs = idf.idfobjects["BuildingSurface:Detailed"]
    surf = surfs[0]
    print(surf.eppy_objidd.fieldnames())

    > ['surface_type',
    >  'number_of_vertices',
    >  'outside_boundary_condition_object',
    >  'construction_name',
    >  'wind_exposure',
    >  'vertices',
    >  'view_factor_to_ground',
    >  'zone_name',
    >  'sun_exposure',
    >  'outside_boundary_condition']

Notice the field vertices. Let us print and see what is in it::

    pprint(surf.vertices)

    > [{'vertex_x_coordinate': 15.24,
    >   'vertex_y_coordinate': 0.0,
    >   'vertex_z_coordinate': 0.0},
    >  {'vertex_x_coordinate': 0.0,
    >   'vertex_y_coordinate': 0.0,
    >   'vertex_z_coordinate': 0.0},
    >  {'vertex_x_coordinate': 0.0,
    >   'vertex_y_coordinate': 15.24,
    >   'vertex_z_coordinate': 0.0},
    >  {'vertex_x_coordinate': 15.24,
    >   'vertex_y_coordinate': 15.24,
    >   'vertex_z_coordinate': 0.0}]

Now let is print one vertex::

    pprint(surf.vertices[0])

    > {'vertex_x_coordinate': 15.24,
    >  'vertex_y_coordinate': 0.0,
    >  'vertex_z_coordinate': 0.0}

Looking at one coordinate::

    print(surf.vertices[0].vertex_x_coordinate)

    > 15.24

Now modifying the vertices::

    surf.vertices[0].vertex_x_coordinate = 88
    surf.vertices.append(dict(vertex_x_coordinate=1.2,
                            vertex_y_coordinate=2.3,
                            vertex_z_coordinate=3.4))

How did our file change? ::

    print(idf)

    > BuildingSurface:Detailed                         !-  KEY
    >             Zn001:Flr001                                 !-  NAME
    >             FLOOR                                !-  construction_name
    >             12                                   !-  idf_max_extensible_fields
    >             22                                   !-  idf_max_fields
    >             27                                   !-  idf_order
    >             4                                    !-  number_of_vertices
    >             Surface                              !-  outside_boundary_condition
    >             Zn001:Flr001                         !-  outside_boundary_condition_object
    >             NoSun                                !-  sun_exposure
    >             Floor                                !-  surface_type
    >                                                  !-  vertices
    >                 88                                   !-  vertex_x_coordinate #1
    >                 0.0                                  !-  vertex_y_coordinate #1
    >                 0.0                                  !-  vertex_z_coordinate #1
    >                 0.0                                  !-  vertex_x_coordinate #2
    >                 0.0                                  !-  vertex_y_coordinate #2
    >                 0.0                                  !-  vertex_z_coordinate #2
    >                 0.0                                  !-  vertex_x_coordinate #3
    >                 15.24                                !-  vertex_y_coordinate #3
    >                 0.0                                  !-  vertex_z_coordinate #3
    >                 15.24                                !-  vertex_x_coordinate #4
    >                 15.24                                !-  vertex_y_coordinate #4
    >                 0.0                                  !-  vertex_z_coordinate #4
    >                 1.2                                  !-  vertex_x_coordinate #5
    >                 2.3                                  !-  vertex_y_coordinate #5
    >                 3.4                                  !-  vertex_z_coordinate #5
    >             1.0                                  !-  view_factor_to_ground
    >             NoWind                               !-  wind_exposure
    >             Main Zone                            !-  zone_name
    >


Note that we have added one set of coordinate points and changed the firat x-coordinate

Deleting, Copying and Creating idfobjects
-----------------------------------------

The following functions are siilar to those in eppy.

Creating new idfobjects
~~~~~~~~~~~~~~~~~~~~~~~

Let us start with a blank file::

    from io import StringIO
    from pprint import pprint
    from eppy3000.modelmaker import IDF


    iddfname = "/Applications/EnergyPlus-8-9-0/Energy+.schema.epJSON"
    idf = IDF(idfname=StringIO("{}"), iddname=iddfname)

Now let us create a new `BuildingSurface:Detailed` object in it::

    key = "BuildingSurface:Detailed"
    objname = "wall1"
    idf.newidfobject(key, objname)
    print(idf)

    > BuildingSurface:Detailed                         !-  KEY
    >             wall1                                !-  NAME
    >             Autocalculate                        !-  number_of_vertices
    >             WindExposed                          !-  wind_exposure
    >             Autocalculate                        !-  view_factor_to_ground
    >             SunExposed                           !-  sun_exposure

Notice how it put in all the default values. But what if we wanted to create the new object without the default values::

    objname = "wall2"
    idf.newidfobject(key, objname, defaultvalues=False)
    print(idf)

    > BuildingSurface:Detailed                         !-  KEY
    >             wall1                                        !-  NAME
    >             Autocalculate                        !-  number_of_vertices
    >             WindExposed                          !-  wind_exposure
    >             Autocalculate                        !-  view_factor_to_ground
    >             SunExposed                           !-  sun_exposure
    >
    > BuildingSurface:Detailed                         !-  KEY
    >             wall2                                        !-  NAME

Wall2 does not include the default values. Now let us add more values using keyword arguments::

    objname = "wall3"
    lastobj = idf.newidfobject(key, objname, defaultvalues=True,
                    outside_boundary_condition="Surface",
                    vertices=[{'vertex_x_coordinate': 15.24,
                                'vertex_y_coordinate': 0.0,
                                'vertex_z_coordinate': 0.0}])

    print(idf)

    > BuildingSurface:Detailed                         !-  KEY
    >             wall1                                        !-  NAME
    >             Autocalculate                        !-  number_of_vertices
    >             WindExposed                          !-  wind_exposure
    >             Autocalculate                        !-  view_factor_to_ground
    >             SunExposed                           !-  sun_exposure
    >
    > BuildingSurface:Detailed                         !-  KEY
    >             wall2                                        !-  NAME
    >
    > BuildingSurface:Detailed                         !-  KEY
    >             wall3                                        !-  NAME
    >             Autocalculate                        !-  number_of_vertices
    >             WindExposed                          !-  wind_exposure
    >             Autocalculate                        !-  view_factor_to_ground
    >             SunExposed                           !-  sun_exposure
    >             Surface                              !-  outside_boundary_condition
    >                                                  !-  vertices
    >                 15.24                                !-  vertex_x_coordinate #1
    >                 0.0                                  !-  vertex_y_coordinate #1
    >                 0.0                                  !-  vertex_z_coordinate #1


Deleting an idfobject
~~~~~~~~~~~~~~~~~~~~~

Deleting an idfobject is equally simple::

    idf.removeidfobject(key, "wall1")
    print(idf)

    > BuildingSurface:Detailed                         !-  KEY
    >             wall2                                        !-  NAME
    >
    > BuildingSurface:Detailed                         !-  KEY
    >             wall3                                        !-  NAME
    >             Autocalculate                        !-  number_of_vertices
    >             WindExposed                          !-  wind_exposure
    >             Autocalculate                        !-  view_factor_to_ground
    >             SunExposed                           !-  sun_exposure
    >             Surface                              !-  outside_boundary_condition
    >                                                  !-  vertices
    >                 15.24                                !-  vertex_x_coordinate #1
    >                 0.0                                  !-  vertex_y_coordinate #1
    >                 0.0                                  !-  vertex_z_coordinate #1

How about copying an idfobject::

    idf.copyidfobject(key, "wall3", "wall4")
    print(idf)

    > BuildingSurface:Detailed                         !-  KEY
    >             wall2                                        !-  NAME
    >
    > BuildingSurface:Detailed                         !-  KEY
    >             wall3                                        !-  NAME
    >             Autocalculate                        !-  number_of_vertices
    >             WindExposed                          !-  wind_exposure
    >             Autocalculate                        !-  view_factor_to_ground
    >             SunExposed                           !-  sun_exposure
    >             Surface                              !-  outside_boundary_condition
    >                                                  !-  vertices
    >                 15.24                                !-  vertex_x_coordinate #1
    >                 0.0                                  !-  vertex_y_coordinate #1
    >                 0.0                                  !-  vertex_z_coordinate #1
    >
    > BuildingSurface:Detailed                         !-  KEY
    >             wall4                                        !-  NAME
    >             Autocalculate                        !-  number_of_vertices
    >             WindExposed                          !-  wind_exposure
    >             Autocalculate                        !-  view_factor_to_ground
    >             SunExposed                           !-  sun_exposure
    >             Surface                              !-  outside_boundary_condition
    >                                                  !-  vertices
    >                 15.24                                !-  vertex_x_coordinate #1
    >                 0.0                                  !-  vertex_y_coordinate #1
    >                 0.0                                  !-  vertex_z_coordinate #1
