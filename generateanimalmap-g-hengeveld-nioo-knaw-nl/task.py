
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--DBH', action='store', type=str, required=True, dest='DBH')

arg_parser.add_argument('--landuse', action='store', type=str, required=True, dest='landuse')

arg_parser.add_argument('--management', action='store', type=str, required=True, dest='management')

arg_parser.add_argument('--Species', action='store', type=str, required=True, dest='Species')

arg_parser.add_argument('--TreeDensity', action='store', type=str, required=True, dest='TreeDensity')

arg_parser.add_argument('--treeSpecies', action='store', type=str, required=True, dest='treeSpecies')


args = arg_parser.parse_args()
print(args)

id = args.id

DBH = json.loads(args.DBH)
landuse = args.landuse.replace('"','')
management = args.management.replace('"','')
Species = args.Species.replace('"','')
TreeDensity = json.loads(args.TreeDensity)
treeSpecies = json.loads(args.treeSpecies)





file_Abundance = open("/tmp/Abundance_" + id + ".json", "w")
file_Abundance.write(json.dumps(Abundance))
file_Abundance.close()
file_Species = open("/tmp/Species_" + id + ".json", "w")
file_Species.write(json.dumps(Species))
file_Species.close()
