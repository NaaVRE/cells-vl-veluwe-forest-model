
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




nitrogen_uptake_factor = 1.
soil_nitrogen_compounds_concentration = 1.

file_nitrogen_uptake_factor = open("/tmp/nitrogen_uptake_factor_" + id + ".json", "w")
file_nitrogen_uptake_factor.write(json.dumps(nitrogen_uptake_factor))
file_nitrogen_uptake_factor.close()
file_soil_nitrogen_compounds_concentration = open("/tmp/soil_nitrogen_compounds_concentration_" + id + ".json", "w")
file_soil_nitrogen_compounds_concentration.write(json.dumps(soil_nitrogen_compounds_concentration))
file_soil_nitrogen_compounds_concentration.close()
