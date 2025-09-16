
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





file_precip = open("/tmp/precip_" + id + ".json", "w")
file_precip.write(json.dumps(precip))
file_precip.close()
file_temp = open("/tmp/temp_" + id + ".json", "w")
file_temp.write(json.dumps(temp))
file_temp.close()
