
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id






file_my_dataset310 = open("/tmp/my_dataset310_" + id + ".json", "w")
file_my_dataset310.write(json.dumps(my_dataset310))
file_my_dataset310.close()
