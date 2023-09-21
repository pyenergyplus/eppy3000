"""open an idf file as an epj"""

import os.path
import eppy
import eppy3000.oldeppy as oldeppy



def openidf(fname, wfile, epjschema=None):
    """opens an idf into an epj. Just like eppy.openidf
    
    TODO : make it as 
    
        - openidf(fname, idd=None, epjschema=None, wfile=None)
        - needs pytest
    """
    idf = eppy.openidf(fname, epw=wfile) # needs a weather file to work. TODO: open an issue and fix this
    if not epjschema:
        version = idf.idfobjects['version'][0]
        versionid = version.Version_Identifier
        iddfile = eppy.easyopen.getiddfile(versionid)
        head, tail = os.path.split(iddfile)
        epjschema = f"{head}/Energy+.schema.epJSON"
    epj = oldeppy.idf2epj(idf, open(epjschema, 'r'))
    return epj