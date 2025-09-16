
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





file_DBH = open("/tmp/DBH_" + id + ".json", "w")
file_DBH.write(json.dumps(DBH))
file_DBH.close()
file_Species = open("/tmp/Species_" + id + ".json", "w")
file_Species.write(json.dumps(Species))
file_Species.close()
file_TreeDensity = open("/tmp/TreeDensity_" + id + ".json", "w")
file_TreeDensity.write(json.dumps(TreeDensity))
file_TreeDensity.close()
