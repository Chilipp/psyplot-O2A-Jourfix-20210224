"""Transform a FESOM style mesh and data file to the UGRID conventions."""
import numpy as np

import xarray as xr


def fesom_to_ugrid(data_ds: xr.Dataset, mesh_ds: xr.Dataset) -> xr.Dataset:
    """Transform a FESOM dataset to follow the UGRID conventions.

    This function takes the data and mesh from FESOM and transforms it to the
    UGRID conventions [1]_.

    Parameters
    ----------
    data_ds: xr.Dataset
        The dataset containing the data variables with dimensions ``nodes_2d``
        and ``nodes_3d``
    mesh_ds: xr.Dataset
        The dataset containing the mesh definition, i.e. ``ele``, ``lon``,
        ``nod32``, etc.

    Returns
    -------
    xr.Dataset
        The combined dataset following the UGRID-conventions

    References
    ----------
    .. [1] https://ugrid-conventions.github.io/ugrid-conventions/
    """
    ds = data_ds.copy(False).update(mesh_ds)

    ds["mesh"] = (
        (), 1, {"face_node_connectivity": "ele", "node_coordinates": "lon lat"}
    )
    ds["ele"] = ds["ele"].copy(False)
    ds["ele"].attrs["start_index"] = 1

    ds = ds.swap_dims({"nodes_2d": "node", "nlayer": "layer", "T": "time"})

    # create an array for the 3D variables.
    ntime = ds.dims["time"]
    arr3d = np.empty_like(ds.nod32.T, dtype=ds.u.dtype)[None].repeat(ntime, 0)
    arr3d.fill(np.nan)
    mask = (ds.nod32.T.values != -999)[None].repeat(ntime, 0)

    for var in data_ds:
        if "nodes_3d" in ds[var].dims:
            data = arr3d.copy()
            data[mask] = ds[var].values.ravel()
            attrs = ds[var].attrs.copy()
            attrs.update({"mesh": "mesh", "location": "node"})
            ds[var] = (("time", "layer", "node"), data, attrs)
        elif "node" in ds[var].dims:
            ds[var] = ds[var].copy(False)
            ds[var].attrs.update({"mesh": "mesh", "location": "node"})
        if "description" in ds[var].attrs:
            ds[var].attrs["long_name"] = ds[var].attrs.pop("description")
    del ds["nod32"]
    return ds.set_coords(["mesh", "ele", "lon", "lat"])