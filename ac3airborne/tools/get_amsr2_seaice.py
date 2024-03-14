import intake_xarray
from intake.catalog import Catalog
from intake.catalog.local import LocalCatalogEntry

def get_amsr2_seaice(campaign,yyyymmdd):
	'''This routine gets the AMSR2 sea ice coverage for the date specified in the arguments (yyyymmdd).

	The data is retrieved from the meereisportal in Bremen in hdf format and converted to netcdf by a cron script. 
	'''
	mycat = Catalog.from_dict({'flight_id': LocalCatalogEntry(name='sea_ice',
	        description='', 
	        driver=intake_xarray.netcdf.NetCDFSource, 
	        args=dict(urlpath='https://atmos.meteo.uni-koeln.de/ac3/'+campaign+'/auxiliary/amsr2_seaice/daily_grid/asi-AMSR2-n6250-'+yyyymmdd+'-v5.4.nc'))
	                           })

	return mycat['flight_id'].to_dask()
