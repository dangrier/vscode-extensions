# Python: 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
# Library: scipy, version: 1.6.1
# Module: scipy.sparse._csparsetools, version: unspecified
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
def _lil_fancy_get_int32() -> typing.Any:
    ...

def _lil_fancy_get_int64() -> typing.Any:
    ...

def _lil_fancy_set_int32_bool_() -> typing.Any:
    ...

def _lil_fancy_set_int32_clongdouble() -> typing.Any:
    ...

def _lil_fancy_set_int32_complex128() -> typing.Any:
    ...

def _lil_fancy_set_int32_complex64() -> typing.Any:
    ...

def _lil_fancy_set_int32_float32() -> typing.Any:
    ...

def _lil_fancy_set_int32_float64() -> typing.Any:
    ...

def _lil_fancy_set_int32_int16() -> typing.Any:
    ...

def _lil_fancy_set_int32_int32() -> typing.Any:
    ...

def _lil_fancy_set_int32_int64() -> typing.Any:
    ...

def _lil_fancy_set_int32_int8() -> typing.Any:
    ...

def _lil_fancy_set_int32_longdouble() -> typing.Any:
    ...

def _lil_fancy_set_int32_uint16() -> typing.Any:
    ...

def _lil_fancy_set_int32_uint32() -> typing.Any:
    ...

def _lil_fancy_set_int32_uint64() -> typing.Any:
    ...

def _lil_fancy_set_int32_uint8() -> typing.Any:
    ...

def _lil_fancy_set_int64_bool_() -> typing.Any:
    ...

def _lil_fancy_set_int64_clongdouble() -> typing.Any:
    ...

def _lil_fancy_set_int64_complex128() -> typing.Any:
    ...

def _lil_fancy_set_int64_complex64() -> typing.Any:
    ...

def _lil_fancy_set_int64_float32() -> typing.Any:
    ...

def _lil_fancy_set_int64_float64() -> typing.Any:
    ...

def _lil_fancy_set_int64_int16() -> typing.Any:
    ...

def _lil_fancy_set_int64_int32() -> typing.Any:
    ...

def _lil_fancy_set_int64_int64() -> typing.Any:
    ...

def _lil_fancy_set_int64_int8() -> typing.Any:
    ...

def _lil_fancy_set_int64_longdouble() -> typing.Any:
    ...

def _lil_fancy_set_int64_uint16() -> typing.Any:
    ...

def _lil_fancy_set_int64_uint32() -> typing.Any:
    ...

def _lil_fancy_set_int64_uint64() -> typing.Any:
    ...

def _lil_fancy_set_int64_uint8() -> typing.Any:
    ...

def _lil_flatten_to_array_bool_() -> typing.Any:
    ...

def _lil_flatten_to_array_clongdouble() -> typing.Any:
    ...

def _lil_flatten_to_array_complex128() -> typing.Any:
    ...

def _lil_flatten_to_array_complex64() -> typing.Any:
    ...

def _lil_flatten_to_array_float32() -> typing.Any:
    ...

def _lil_flatten_to_array_float64() -> typing.Any:
    ...

def _lil_flatten_to_array_int16() -> typing.Any:
    ...

def _lil_flatten_to_array_int32() -> typing.Any:
    ...

def _lil_flatten_to_array_int64() -> typing.Any:
    ...

def _lil_flatten_to_array_int8() -> typing.Any:
    ...

def _lil_flatten_to_array_longdouble() -> typing.Any:
    ...

def _lil_flatten_to_array_uint16() -> typing.Any:
    ...

def _lil_flatten_to_array_uint32() -> typing.Any:
    ...

def _lil_flatten_to_array_uint64() -> typing.Any:
    ...

def _lil_flatten_to_array_uint8() -> typing.Any:
    ...

def _lil_get_lengths_int32() -> typing.Any:
    ...

def _lil_get_lengths_int64() -> typing.Any:
    ...

def lil_fancy_get() -> typing.Any:
    '\n    Get multiple items at given indices in LIL matrix and store to\n    another LIL.\n\n    Parameters\n    ----------\n    M, N, rows, data\n        LIL matrix data, initially empty\n    new_rows, new_idx\n        Data for LIL matrix to insert to.\n        Must be preallocated to shape `i_idx.shape`!\n    i_idx, j_idx\n        Indices of elements to insert to the new LIL matrix.\n\n    '
    ...

def lil_fancy_set() -> typing.Any:
    '\n    Set multiple items to a LIL matrix.\n\n    Checks for zero elements and deletes them.\n\n    Parameters\n    ----------\n    M, N, rows, data\n        LIL matrix data\n    i_idx, j_idx\n        Indices of elements to insert to the new LIL matrix.\n    values\n        Values of items to set.\n\n    '
    ...

def lil_flatten_to_array() -> typing.Any:
    ...

def lil_get1() -> typing.Any:
    "\n    Get a single item from LIL matrix.\n\n    Doesn't do output type conversion. Checks for bounds errors.\n\n    Parameters\n    ----------\n    M, N, rows, datas\n        Shape and data arrays for a LIL matrix\n    i, j : int\n        Indices at which to get\n\n    Returns\n    -------\n    x\n        Value at indices.\n\n    "
    ...

def lil_get_lengths() -> typing.Any:
    ...

def lil_get_row_ranges() -> typing.Any:
    '\n    Column-slicing fast path for LIL matrices.\n    Extracts values from rows/datas and inserts in to\n    new_rows/new_datas.\n    Parameters\n    ----------\n    M, N\n         Shape of input array\n    rows, datas\n         LIL data for input array, shape (M, N)\n    new_rows, new_datas\n         LIL data for output array, shape (len(irows), nj)\n    irows : iterator\n         Iterator yielding row indices\n    j_start, j_stop, j_stride\n         Column range(j_start, j_stop, j_stride) to get\n    nj : int\n         Number of columns corresponding to j_* variables.\n    '
    ...

def lil_insert() -> typing.Any:
    '\n    Insert a single item to LIL matrix.\n\n    Checks for bounds errors and deletes item if x is zero.\n\n    Parameters\n    ----------\n    M, N, rows, datas\n        Shape and data arrays for a LIL matrix\n    i, j : int\n        Indices at which to get\n    x\n        Value to insert.\n\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

