$ psql gis

gis=> SELECT ST_AsText(way)
FROM planet_osm_point
WHERE "name" LIKE 'Hyatt%';
                 st_astext
-------------------------------------------
 POINT(-9481012.96880667 3941017.3930227)
 POINT(-9399929.12076633 3983988.17286583)
 POINT(-9341209.61445808 4159288.58929291)
 POINT(-9027126.42457084 3774062.70553924)
(4 rows)
