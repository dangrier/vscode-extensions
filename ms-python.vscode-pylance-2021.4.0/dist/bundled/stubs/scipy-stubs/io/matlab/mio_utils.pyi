# Python: 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
# Library: scipy, version: 1.6.1
# Module: scipy.io.matlab.mio_utils, version: unspecified
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__pyx_capi__: dict
__test__: dict
def chars_to_strings() -> typing.Any:
    " Convert final axis of char array to strings\n\n    Parameters\n    ----------\n    in_arr : array\n       dtype of 'U1'\n\n    Returns\n    -------\n    str_arr : array\n       dtype of 'UN' where N is the length of the last dimension of\n       ``arr``\n    "
    ...

def squeeze_element() -> typing.Any:
    ' Return squeezed element\n\n    The returned object may not be an ndarray - for example if we do\n    ``arr.item`` to return a ``mat_struct`` object from a struct array '
    ...

def __getattr__(name) -> typing.Any:
    ...
