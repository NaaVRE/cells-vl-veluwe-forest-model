
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





file_Abundance = open("/tmp/Abundance_" + id + ".json", "w")
file_Abundance.write(json.dumps(Abundance))
file_Abundance.close()
file_PQnr = open("/tmp/PQnr_" + id + ".json", "w")
file_PQnr.write(json.dumps(PQnr))
file_PQnr.close()
file_Species = open("/tmp/Species_" + id + ".json", "w")
file_Species.write(json.dumps(Species))
file_Species.close()
