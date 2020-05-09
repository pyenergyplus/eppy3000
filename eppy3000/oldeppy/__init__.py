class NeedsEppyError(Exception):
    pass

try:
    import eppy
except ModuleNotFoundError as e:
    raise NeedsEppyError("you need to install eppy to run these functions")
