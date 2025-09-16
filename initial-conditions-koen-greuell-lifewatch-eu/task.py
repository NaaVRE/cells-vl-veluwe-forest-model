
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




intial_stored_tree_mass = 1.

file_intial_stored_tree_mass = open("/tmp/intial_stored_tree_mass_" + id + ".json", "w")
file_intial_stored_tree_mass.write(json.dumps(intial_stored_tree_mass))
file_intial_stored_tree_mass.close()
