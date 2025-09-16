
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--Animal', action='store', type=str, required=True, dest='Animal')

arg_parser.add_argument('--Landuse', action='store', type=str, required=True, dest='Landuse')

arg_parser.add_argument('--Management', action='store', type=str, required=True, dest='Management')

arg_parser.add_argument('--Soil', action='store', type=str, required=True, dest='Soil')

arg_parser.add_argument('--Tree', action='store', type=str, required=True, dest='Tree')


args = arg_parser.parse_args()
print(args)

id = args.id

Animal = json.loads(args.Animal)
Landuse = json.loads(args.Landuse)
Management = json.loads(args.Management)
Soil = json.loads(args.Soil)
Tree = json.loads(args.Tree)





file_Animal_out = open("/tmp/Animal_out_" + id + ".json", "w")
file_Animal_out.write(json.dumps(Animal_out))
file_Animal_out.close()
file_Tree_out = open("/tmp/Tree_out_" + id + ".json", "w")
file_Tree_out.write(json.dumps(Tree_out))
file_Tree_out.close()
