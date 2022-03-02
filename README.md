# ac3airborne: AC3 airborne python tools 

This package intents to make the access to the airborne data collected within the various [AC3](http://www.ac3-tr.de/) airborne campaigns more easy. To make use of the package, it is best to study the [how_to_ac3airborne](https://igmk.github.io/how_to_ac3airborne/intro.html), which is a description of most of the data and a collection of examples and tools.

## installation
```bash
pip install git+https://github.com/igmk/ac3airborne.git
```

**If you are interested in the growing package including the HALO-AC3 campaign, add *@halo-ac3* to the installation command.**

```bash
pip install git+https://github.com/igmk/ac3airborne.git@halo-ac3
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

In [3]: flightinfo['ACLOUD']['P5']['ACLOUD_P5_RF14']['takeoff']
Out[3]: datetime.datetime(2017, 6, 8, 7, 36, 50)
```

### getting the intake catalogues

```ipython
In [4]: cat = ac3airborne.get_intake_catalog()
In [5]: list(cat['ACLOUD']['P5']['MiRAC-A'])                                                                                                                                                                                      
Out[5]: 
['ACLOUD_P5_RF04',
 'ACLOUD_P5_RF05',
 ...
 'ACLOUD_P5_RF25']
```
