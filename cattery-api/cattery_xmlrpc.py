from xmlrpc import client

class CatteryAPI():
    
    def __init__(self, host, port, db, user, password, model:str):
        common = client.ServerProxy(f'http://{host}:{port}/xmlrpc/2/common')
        self.api = client.ServerProxy(f'http://{host}:{port}/xmlrpc/2/object')
        self.uid = common.authenticate(db, user, password, {})
        self.db = db
        self.password = password
        self.model = model

    def _execute(self, method:str, arg_list, kwarg_dict=None):
        return self.api.execute_kw(
            self.db, self.uid, self.password, self.model,
            method, arg_list, kwarg_dict or {}
            )
    
    def search_read(self, breed=None):
        domain = [('breed_id', 'ilike', breed)] if breed else []
        fields = ['name', 'gender', 'age', 'breed_id']
        return self._execute('search_read', [domain, fields])
    
    def create(self, breed):
        breed_id = self.search_read(breed)[0]['breed_id'][0]
        entries = {'breed_id': breed_id}
        num_entries = int(input("How many entries does the record have? "))
        for i in range(num_entries):
            field = input(f"Enter field {i+1}: ").lower()
            value = input(f"Enter value for field '{field}': ")
            entries[field] = value
        return self._execute('create', [entries])
    
    def write(self, kitten_id, breed):
        breed_id = self.search_read(breed)[0]['breed_id'][0]
        entries = {'breed_id': breed_id}
        num_entries = int(input("How many entries to update? "))
        for i in range(num_entries):
            field = input(f"Enter field {i+1}: ").lower()
            value = input(f"Enter value for field '{field}': ")
            entries[field] = value
        return self._execute('write', [kitten_id, entries])
        
    
    def unlink(self, kitten_id):
        return self._execute('unlink', [kitten_id])
   
    