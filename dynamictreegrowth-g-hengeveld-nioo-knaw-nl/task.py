
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--Abundance', action='store', type=str, required=True, dest='Abundance')

arg_parser.add_argument('--Animal', action='store', type=str, required=True, dest='Animal')

arg_parser.add_argument('--DBH', action='store', type=str, required=True, dest='DBH')

arg_parser.add_argument('--precipitation', action='store', type=str, required=True, dest='precipitation')

arg_parser.add_argument('--Soil', action='store', type=str, required=True, dest='Soil')

arg_parser.add_argument('--Species', action='store', type=str, required=True, dest='Species')

arg_parser.add_argument('--temperature', action='store', type=str, required=True, dest='temperature')

arg_parser.add_argument('--TreeDensity', action='store', type=str, required=True, dest='TreeDensity')


args = arg_parser.parse_args()
print(args)

id = args.id

Abundance = json.loads(args.Abundance)
Animal = json.loads(args.Animal)
DBH = json.loads(args.DBH)
precipitation = json.loads(args.precipitation)
Soil = json.loads(args.Soil)
Species = json.loads(args.Species)
temperature = json.loads(args.temperature)
TreeDensity = json.loads(args.TreeDensity)





file_DBH_out = open("/tmp/DBH_out_" + id + ".json", "w")
file_DBH_out.write(json.dumps(DBH_out))
file_DBH_out.close()
file_Species_out = open("/tmp/Species_out_" + id + ".json", "w")
file_Species_out.write(json.dumps(Species_out))
file_Species_out.close()
file_TreeDensity_out = open("/tmp/TreeDensity_out_" + id + ".json", "w")
file_TreeDensity_out.write(json.dumps(TreeDensity_out))
file_TreeDensity_out.close()
