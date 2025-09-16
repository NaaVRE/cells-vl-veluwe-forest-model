
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





file_DBH = open("/tmp/DBH_" + id + ".json", "w")
file_DBH.write(json.dumps(DBH))
file_DBH.close()
file_Height = open("/tmp/Height_" + id + ".json", "w")
file_Height.write(json.dumps(Height))
file_Height.close()
file_Plotnr = open("/tmp/Plotnr_" + id + ".json", "w")
file_Plotnr.write(json.dumps(Plotnr))
file_Plotnr.close()
file_Species = open("/tmp/Species_" + id + ".json", "w")
file_Species.write(json.dumps(Species))
file_Species.close()
