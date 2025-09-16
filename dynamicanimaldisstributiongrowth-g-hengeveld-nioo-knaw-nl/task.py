
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--Abundance', action='store', type=str, required=True, dest='Abundance')

arg_parser.add_argument('--Animal', action='store', type=str, required=True, dest='Animal')

arg_parser.add_argument('--DBH', action='store', type=str, required=True, dest='DBH')

arg_parser.add_argument('--Species', action='store', type=str, required=True, dest='Species')

arg_parser.add_argument('--TreeDensity', action='store', type=str, required=True, dest='TreeDensity')


args = arg_parser.parse_args()
print(args)

id = args.id

Abundance = json.loads(args.Abundance)
Animal = json.loads(args.Animal)
DBH = json.loads(args.DBH)
Species = json.loads(args.Species)
TreeDensity = json.loads(args.TreeDensity)





file_Abundance_out = open("/tmp/Abundance_out_" + id + ".json", "w")
file_Abundance_out.write(json.dumps(Abundance_out))
file_Abundance_out.close()
file_Animal_out = open("/tmp/Animal_out_" + id + ".json", "w")
file_Animal_out.write(json.dumps(Animal_out))
file_Animal_out.close()
