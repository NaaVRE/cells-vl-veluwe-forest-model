
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--location', action='store', type=str, required=True, dest='location')


args = arg_parser.parse_args()
print(args)

id = args.id

location = args.location.replace('"','')





file_landuse = open("/tmp/landuse_" + id + ".json", "w")
file_landuse.write(json.dumps(landuse))
file_landuse.close()
file_management = open("/tmp/management_" + id + ".json", "w")
file_management.write(json.dumps(management))
file_management.close()
file_soil = open("/tmp/soil_" + id + ".json", "w")
file_soil.write(json.dumps(soil))
file_soil.close()
file_vegetation = open("/tmp/vegetation_" + id + ".json", "w")
file_vegetation.write(json.dumps(vegetation))
file_vegetation.close()
