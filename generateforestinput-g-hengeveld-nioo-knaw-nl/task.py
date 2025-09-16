
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





file_DBH_out = open("/tmp/DBH_out_" + id + ".json", "w")
file_DBH_out.write(json.dumps(DBH_out))
file_DBH_out.close()
file_Species_out = open("/tmp/Species_out_" + id + ".json", "w")
file_Species_out.write(json.dumps(Species_out))
file_Species_out.close()
file_TreeDensity_out = open("/tmp/TreeDensity_out_" + id + ".json", "w")
file_TreeDensity_out.write(json.dumps(TreeDensity_out))
file_TreeDensity_out.close()
