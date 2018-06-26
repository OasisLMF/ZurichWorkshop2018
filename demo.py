from __future__ import print_function

import copy, io, json, os, sys, time

import pandas as pd, six

import shapely, shapely.geometry
from shapely.geometry import Point, Polygon, MultiPolygon, box

from oasislmf.utils.data import get_dataframe
from oasislmf.utils.peril import PerilAreasIndex, DEFAULT_RTREE_INDEX_PROPS

from oasislmf.keys.lookup import OasisLookupFactory as olf

# Create a copy of the default Rtree properties dict and set
# leaf capacity and fill factor to create as small an index as possible
props = copy.deepcopy(DEFAULT_RTREE_INDEX_PROPS); props['leaf_capacity'] = 1000; props['fill_factor'] = 0.9

# Create an EUWS lookup (combines peril and vulnerability lookup) using the
# Oasis lookup factory
info, euws = olf.create(lookup_config_fp='lookup.json')
print('\nEUWS model info: {}'.format(info))
print('\nCombined EUWS lookup (peril + vuln): {}'.format(euws))

# Get the config dict from the lookup (loaded in from the file path you
# provided to create the lookup)
config = euws.config
#print('lookup config: {}'.format(config))

# Check that keys data path look correct
keys_data_path = config.get('keys_data_path')
print('\nkeys data path: {}'.format(keys_data_path), end='')
print('; exists: {}'.format(os.path.exists(keys_data_path)))

# Check that the peril and vulnerability configs look OK
print('\nperil config: {}'.format(config.get('peril')))
print('\nvulnerability config: {}'.format(config.get('vulnerability')))

# Check that the locations config looks OK
print('\nlocations config: {}'.format(config.get('locations')))

# Get the peril and vulnerabiity lookups from the main lookup - they are stored
# as attributes
plookup = euws.peril_lookup
print('\nperil lookup: {}'.format(plookup))

vlookup = euws.vulnerability_lookup
print('\nvuln lookup: {}'.format(vlookup))

# Get the areas index and check the pickling protocol used to create it
areas_index = plookup.peril_areas_index
print('\nareas index: {}'.format(areas_index))

print('\nareas index pickling protocol: {}'.format(areas_index.protocol))

# Get the properties of the index as an attribute
props = areas_index.properties.as_dict()
print('\nindex props: {}'.format(props))

# Get the bounds of the convex hull of all the area polygons stored in the index
# should be consistent with the areas defined in the source areas file
print('\nglobal areas bounds: {}'.format(areas_index.bounds))

# Get the leaf levels of the index
leaf_levels = areas_index.leaves()
n = len(leaf_levels)
print('\nnum. leaf levels in the index: {} '.format(n))

 # Sum of number of leaves at each leaf level should equal the number of areas in the areas file
print('\nnum. areas stored in the index: {}'.format(sum(len(leaf_levels[i][1]) for i in range(n))))

# Can also get global areas boundary from the `peril_areas_boundary` attribute from peril lookup
print('\nglobal areas boundary from peril lookup: {}'.format(plookup.peril_areas_boundary.bounds))

# Get the centre of the convex hull of all the area polygons
print('\ncentre of all the areas: {}'.format(plookup.peril_areas_centre))

# Get the vulnerability dict - should be consistent with the source file
# key columns are represented as tuple keys in the dict, and the vuln IDs
# are the values of keys in the dict
print('\nvuln dict: {}'.format(vlookup.vulnerabilities))
print('\nvuln file key columns: {}'.format(vlookup.key_cols))

# Create a locations dataframe from a test locations file
loc_df = get_dataframe(
    src_fp='keys_data/EuWs/model_loc_test.csv',
    non_na_cols=('ID', 'LONGITUDE', 'LATITUDE','VULNERABILITY',),
    col_dtypes={'ID': int, 'LONGITUDE': float, 'LATITUDE': float, 'VULNERABILITY': int},
    sort_col='ID'
)

# Do a combined, peril and vuln lookup for an individual location
# the combined lookup does the peril and vuln lookup - the individual
# peril and vuln lookups should be consistent with the combined lookup
loc = loc_df.iloc[0]
print('\nloc: {}'.format(loc))

print('\nperil lookup: {}'.format(plookup.lookup(loc)))
print('\nvuln lookup: {}'.format(vlookup.lookup(loc)))
print('\ncombined lookup: {}'.format(euws.lookup(loc)))

# Do a bulk combined lookup and time it
t = time.time()
results = [res for res in euws.bulk_lookup(loc for _, loc in loc_df.iterrows())]
tt = time.time() - t
print('\nCompleted combined bulk lookup for {} locations in {} seconds'.format(len(loc_df), tt))

# Sample the results
print('\nSampling some results')
print('\n#1: {}'.format(results[0]))
print('\n#3: {}'.format(results[2]))
print('\n#5: {}'.format(results[4]))
print('\n#10: {}\n'.format(results[-1]))
