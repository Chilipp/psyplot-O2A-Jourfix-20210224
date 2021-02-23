#  Visualizing and analyzing HZG model data using the HCDC framework psyplot

Presentation material for the O2A Jourfix on February 24th, 2021

Philipp S. Sommer

## Note

Some of the features presented are still in development mode and cannot be
used with the latest libraries.


## About this presentation

This presentation uses material from the
[DKRZ TechTalk from November, 17th 2020][techtalk] and the presentation at the
[KS Seminar on January 28th, 2021][ks-seminar]. It is, however, less technical
and puts more emphasis on new developments concerning the visualization of
transects, and the FESOM model.

[techtalk]: https://github.com/Chilipp/psyplot-DKRZ-TechTalk-20201117
[ks-seminar]: https://github.com/Chilipp/psyplot-KS-Seminar-20210228

### Static version

This presentation is a jupyter notebook presented with [RISE][rise]. You can
access the raw notebook at
[psyplot-framework-presentation.ipynb](psyplot-framework-presentation.ipynb).

### interactive version on AWIs Jupyterhub

You can also run this presentation notebook in [jupyterhub](https://jupyterhub.awi.de). Use the `Python [conda env:Anaconda-Python3.7]` kernel and install the
latest development versions to explore all the options via:

```bash
python -m pip install --user -U \
    git+https://github.com/Chilipp/gridded@dual_node_mesh \
    git+https://github.com/Chilipp/psyplot@ugrid \
    git+https://github.com/psyplot/psy-transect
```

Clonse this repository and open the jupyter notebook within the jupyterhub.

To explore the 3D-visualization, please have a look at the examples in the
[psy-vtk](https://github.com/psyplot/psy-vtk) repository

## License

The contents of this repository is published under the Creative Commons
Attribution 4.0 International Public License (CC BY 4.0).

See the [LICENSE](LICENSE) file for more details.

Copyright (c) 2021, Philipp S. Sommer, HZG.