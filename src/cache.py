from typing import ItemsView
import redis
import json
PORT = 6379
DB = 0

def cache_fetch_products(key):
    r = redis.Redis(host="localhost", port=PORT, db=DB)  # se conecta a redis
    value = r.get(key)
    if value:
        return json.loads(value)    # retorna una lista con diccionario
    else:
        return None                 # retorna una vacio

def cache_insert_json(key, dict):
    r = redis.Redis(host="localhost", port=PORT, db=DB) # se conecta a redis
    value = json.dumps(dict)
    r.set(key, value)



if __name__ == "__main__":
    products= [
        {'name':'test', 'stock':22}, 
        {'name':'test bruh', 'stock':213123},
        {'name':'asddasdasd test', 'stock':3}
    ]
    cache_insert_json("test", products)
    cache_items = cache_fetch_products("test")
    print(f"cache: {cache_items}")
