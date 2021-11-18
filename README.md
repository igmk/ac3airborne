# ac3airborne: AC3 airborne python tools 

This package intents to make the access to the airborne data collected within the various [AC3](http://www.ac3-tr.de/) airborne campaigns more easy. To make use of the package, it is best to study the [how_to_ac3airborne](https://igmk.github.io/how_to_ac3airborne/intro.html), which is a description of most of the data and a collection of examples and tools.

## installation

At the moment the package is still in the testing phase. Before installing ac3airborne it is recommended to install the dependencies needed to run the module. Here is the only available way to install it (the version on TestPyPI will not be updated anymore):

```bash
pip install aiohttp intake!=0.6.1 intake_xarray netCDF4 h5netcdf
pip install git+https://github.com/igmk/ac3airborne.git
```

If you want to get an update, just reinstall the package.

## usage

The package provides a few functions to obtain data from the campaigns and can be used in the following way.

```ipython
In [1]: import ac3airborne
```

### obtaining informations about flights and segments

```ipython
In [2]: flightinfo = ac3airborne.get_flight_segments()

In [3]: flightinfo['P5']['ACLOUD_P5_RF14']['takeoff']
Out[3]: datetime.datetime(2017, 6, 8, 7, 36, 50)
```

### getting the intake catalogues

```ipython
In [4]: cat = ac3airborne.get_intake_catalog()
In [5]: list(cat.Polar5.MIRAC_A)                                                                                                                                                                                      
Out[5]: 
['ACLOUD_P5_RF04',
 'ACLOUD_P5_RF05',
 ...
 'MOSAiC-ACA_P5_RF11']
```
