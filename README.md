# ac3airborne: AC3 airborne python tools 

The package intents to make the access to the airborne data collected within the various [AC3](http://www.ac3-tr.de/) airborne campaigns more easy. To make use of the package, it is best to study the [how_to_ac3airborne](https://igmk.github.io/how_to_ac3airborne/intro.html), which is a description of most of the data sets and a collection of examples and tools.

## installation
The package can be installed by:
```bash
pip install git+https://github.com/igmk/ac3airborne.git
```

We are continously working on *ac3airborne*. If you want to install an updated version, just reinstall the package by the command above.

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
