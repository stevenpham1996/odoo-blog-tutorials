from argparse import ArgumentParser
from cattery_xmlrpc import CatteryClient
from pprint import pprint

parser = ArgumentParser(
    description="Cattery XML-RPC client for Kitten Catalog. ",
    prog="kitten_catalog.py",
)
# define operation commands
parser.add_argument(
    "command",
    choices=["show","create","update","delete"],
)
# define data arguments
parser.add_argument("params", nargs="*")
args = parser.parse_args()

url, db = "localhost:8069", "blog_tutorials"
user, pwd = "admin", "admin"
api = CatteryClient(url, db, user, pwd)

if args.command == "show":
    breed = args.params[0] if args.params else None
    kittens = api.search_read(breed)
    for kitten in kittens:
        pprint(f"{kitten['name']}, {kitten['age']}, {kitten['gender']}, {kitten['breed_id'][1]}")

if args.command == "create":
    if len(args.params) != 1:
        raise Exception("Please enter the kitten's breed")
    breed = args.params[0]
    kitten_id = api.create(breed)
    for kitten in kittens:
        pprint(f"Kitten - ID: {kitten_id} has been listed")

if args.command == "update":
    if len(args.params) != 2:
        raise Exception("Please enter the kitten's ID and breed")
    kitten_id = args.params[0]
    breed = args.params[1]
    api.write(kitten_id, breed)
    pprint(f"Kitten - ID: {kitten_id} has been updated")

if args.command == "delete":
    if len(args.params) != 2:
        raise Exception("Please enter the kitten's ID")
    kitten_id = args.params[0]
    api.unlink(kitten_id)
    pprint(f"Kitten - ID: {kitten_id} has been deleted")