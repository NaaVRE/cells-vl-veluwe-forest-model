
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--DBH', action='store', type=str, required=True, dest='DBH')

arg_parser.add_argument('--landuse', action='store', type=str, required=True, dest='landuse')

arg_parser.add_argument('--management', action='store', type=str, required=True, dest='management')

arg_parser.add_argument('--Plotnr', action='store', type=str, required=True, dest='Plotnr')

arg_parser.add_argument('--treeSpecies', action='store', type=str, required=True, dest='treeSpecies')

arg_parser.add_argument('--treeSpecies', action='store', type=str, required=True, dest='treeSpecies')


args = arg_parser.parse_args()
print(args)

id = args.id

DBH = args.DBH.replace('"','')
landuse = args.landuse.replace('"','')
management = args.management.replace('"','')
Plotnr = args.Plotnr.replace('"','')
treeSpecies = args.treeSpecies.replace('"','')
treeSpecies = args.treeSpecies.replace('"','')





file_DBH = open("/tmp/DBH_" + id + ".json", "w")
file_DBH.write(json.dumps(DBH))
file_DBH.close()
file_Species = open("/tmp/Species_" + id + ".json", "w")
file_Species.write(json.dumps(Species))
file_Species.close()
file_TreeDensity = open("/tmp/TreeDensity_" + id + ".json", "w")
file_TreeDensity.write(json.dumps(TreeDensity))
file_TreeDensity.close()
