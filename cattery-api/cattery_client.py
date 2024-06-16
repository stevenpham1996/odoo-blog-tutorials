from argparse import ArgumentParser
from cattery_xmlrpc import CatteryAPI as CatteryXMLRPC
from cattery_jsonrpc import CatteryAPI as CatteryJSONRPC
from cryptography.fernet import Fernet

parser = ArgumentParser(
    description="Cattery API client.",
    prog="kitten_client.py",
)

# define operation commands
parser.add_argument(
    "command",
    choices=["show","create","update","delete"],
)
# define entry arguments
parser.add_argument("params", nargs="*")

args = parser.parse_args()

# Function to load and decrypt the environment variables
def load_credentials():
    with open('secret.key', 'rb') as key_file:
        key = key_file.read()
    fernet = Fernet(key)

    with open('credentials.enc', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = fernet.decrypt(encrypted).decode().split('\n')

    return dict(line.split('=') for line in decrypted if line)

# Load and decrypt the server details
credentials = load_credentials()
host = credentials['HOST']
port = credentials['PORT']
db = credentials['DB']
user = credentials['USER']
pwd = credentials['PWD']

model = input("Please enter the model reference <module>.<model>: ")

while True: 
    user_api = input("Enter API protocol - 'jsonrpc' or 'xmlrpc': ").lower() 
    if user_api in ["jsonrpc", "xmlrpc"]: 
        break 
    else: 
        print("Invalid input. Make sure no typos and try again.")
if user_api == "jsonrpc":
    api = CatteryJSONRPC(host, port, db, user, pwd, model)
else:
    api = CatteryXMLRPC(host, port, db, user, pwd, model)

if args.command == "show":
    breed = args.params[0] if args.params else None
    kittens = api.search_read(breed)
    for kitten in kittens:
        print(f"{kitten['name']}, {kitten['age']}, {kitten['gender']}, {kitten['breed_id'][1]}")

if args.command == "create":
    if len(args.params) != 1:
        raise Exception("Please enter the kitten's breed")
    breed = args.params[0]
    kitten_id = api.create(breed)
    print(f"Kitten - ID: {kitten_id} has been listed")

if args.command == "update":
    if len(args.params) != 2:
        raise Exception("Please enter the kitten's ID and breed")
    kitten_id = args.params[0]
    breed = args.params[1]
    api.write(kitten_id, breed)
    print(f"Kitten - ID: {kitten_id} has been updated")

if args.command == "delete":
    if len(args.params) != 1:
        raise Exception("Please enter the kitten's ID")
    kitten_id = args.params[0]
    api.unlink(kitten_id)
    print(f"Kitten - ID: {kitten_id} has been deleted")