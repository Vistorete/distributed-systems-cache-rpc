from typing import ItemsView
import redis
import json

def cache_load_json(key):
    r = redis.Redis(host="localhost", port=6379, db=0)
    value = r.get(key)
    print(value)
    if value:
        return json.loads(value)
    
    else:
        return None

def cache_save_json(key, value_dict):
    r = redis.Redis(host="localhost", port=6379, db=0)
    r.set(key, json.dumps(value_dict))



if __name__ == "__main__":
    r = redis.Redis(host="localhost", port=6379, db=0)
    products= [
        {'name':'test', 'stock':22}, 
        {'name':'test bruh', 'stock':213123},
        {'name':'asddasdasd test', 'stock':3}
    ]
    cache_save_json("test", products)
    cache_items = cache_load_json("test")
    print(f"cache: {cache_items}")
