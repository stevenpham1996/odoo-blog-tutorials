import odoorpc

class CatteryAPI():
    
    def __init__(self, host, port, db, user, password, model:str):
        self.api = odoorpc.ODOO(host, protocol='jsonrpc', port=port)
        self.api.login(db, user, password)
        self.uid = self.api.env.uid
        self._model = model
        self.model = self.api.env[self._model]

    def _execute(self, method:str, arg_list, kwarg_dict=None):
        return self.api.execute_kw(
            self._model, method, arg_list, kwarg_dict or {})
        
    def search_read(self, breed=None):
        domain = [('breed_id', 'ilike', breed)] if breed else []
        fields = ['name', 'gender', 'age', 'breed_id']
        return self.model.search_read(domain, fields)
    
    def create(self, breed):
        breed_id = self.search_read(breed)[0]['breed_id'][0]
        entries = {'breed_id': breed_id}
        num_entries = int(input("How many entries does the record have? "))
        for i in range(num_entries):
            field = input(f"Enter field {i+1}: ").lower()
            value = input(f"Enter value for field '{field}': ")
            entries[field] = value
        return self.model.create(entries)
    
    def write(self, kitten_id, breed):
        breed_id = self.search_read(breed)[0]['breed_id'][0]
        entries = {'breed_id': breed_id}
        num_entries = int(input("How many entries to update? "))
        for i in range(num_entries):
            field = input(f"Enter field {i+1}: ").lower()
            value = input(f"Enter value for field '{field}': ")
            entries[field] = value
        return self.model.write(kitten_id, entries)
    
    def unlink(self, kitten_id):
        return self.model.unlink(kitten_id)
    
if __name__ == "__main__":
    # Sample test
    from dotenv import load_dotenv
    import os
    load_dotenv()
    
    host = os.getenv("HOST")
    port = os.getenv("PORT")
    db = os.getenv("DB")
    user = os.getenv("USER")
    pwd = os.getenv("PWD")
    model=input("Please enter the model reference <module>.<model>: ")
    
    api = CatteryAPI(host, port, db, user, pwd, model)
    
    from pprint import pprint
    pprint(api._execute("search", [[("name", "=", "Zara")]]))
    print()
    pprint(api._execute("read", [3, ["name", "age", "gender", "breed_id"]]))
    print()
    pprint(api.search_read("Bengal"))
