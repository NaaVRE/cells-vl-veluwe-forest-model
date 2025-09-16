
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id






file_my_dataset3 = open("/tmp/my_dataset3_" + id + ".json", "w")
file_my_dataset3.write(json.dumps(my_dataset3))
file_my_dataset3.close()
file_my_dataset4 = open("/tmp/my_dataset4_" + id + ".json", "w")
file_my_dataset4.write(json.dumps(my_dataset4))
file_my_dataset4.close()
