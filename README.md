# pyac3airborne: AC3 airborne python tools 

This package intents to make the access to the airborne data collected within the various [AC3](http://www.ac3-tr.de/) airborne campaigns more easy. To make use of the package, it is best to study the [how_to_pyac3airborne](https://igmk.github.io/how_to_pyac3airborne/intro.html), which is a description of most of the data and a collection of examples and tools.

## installation

At the moment the package is still in the testing phase. There are two options to install it. Either download the package from github or get it from the pip test server. But before it is recommended to install dependencies needed to run the module.

```bash
pip install aiohttp intake!=0.6.1 intake_xarray netCDF4 h5netcdf
pip install -i https://test.pypi.org/simple/ ac3airborne
```

If you want to get an update, you first have to manually uninstall the old version. Updating does not work with the test server (to our knowledge).

```bash
pip uninstall ac3airborne
```
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