
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id






file_location = open("/tmp/location_" + id + ".json", "w")
file_location.write(json.dumps(location))
file_location.close()
