Title: ogr2ogr cheatsheet
Date: 2020-02-07 09:25
Slug: ogr2ogr
Author: Ashley Felton
Summary: Cheatsheet for ogr2ogr, ogrinfo and gdal

ogr2ogr commands
-------

ogr2ogr cheatsheet: <https://www.bostongis.com/PrinterFriendly.aspx?content_name=ogr_cheatsheet>

To convert a projected shapefile (GDA94 / MGA zone 50) to WGS84:

~~~~bash
ogr2ogr -s_srs EPSG:28350 -t_srs EPSG:4326 dest_unprojected.shp source_projected.shp
~~~~

To obtain summary information about a dataset:

~~~~bash
ogrinfo -so sourcedata.shp layername1 [layername2 ...]
~~~~

To convert a shapefile to GeoJSON using WGS84 projection:

~~~~bash
ogr2ogr -t_srs EPSG:4326 -f GeoJSON output.geojson source.shp
~~~~

Raster (GeoTIFF) compression using GDAL
------

Source: <http://blog.cleverelephant.ca/2015/02/geotiff-compression-for-dummies.html>

gdal_translate: <https://www.gdal.org/gdal_translate.html>

gdaladdo: <https://www.gdal.org/gdaladdo.html>

More info: <http://docs.geonode.org/en/master/tutorials/advanced/adv_data_mgmt/adv_raster/processing.html>

Compression steps:

~~~~bash
gdalinfo source.tif
# Use gdal_translate to implement JPEG compression:
gdal_translate -co COMPRESS=JPEG -co TILED=YES source.tif output.tif
# Use the YCBCR colour space during compression (if it has bands, we need to use the first three and discard any fourth alpha band):
gdal_translate -b 1 -b 2 -b 3 -co COMPRESS=JPEG -co PHOTOMETRIC=YCBCR -co
TILED=YES source.tif output.tif
# Add overviews to the compressed image:
gdaladdo --config COMPRESS_OVERVIEW JPEG --config PHOTOMETRIC_OVERVIEW YCBCR --config INTERLEAVE_OVERVIEW PIXEL -r average output.tif 2 4 8 16 32
~~~~
