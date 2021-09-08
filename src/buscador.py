from flask import Flask, request, jsonify
import cache
import grpc
import search_pb2_grpc as pb2_grpc
import search_pb2 as pb2

class SearchClient(object):
    def __init__(self):

        self.host = 'localhost'
        self.server_port = 50051
        
        # instancia un canal
        self.channel = grpc.insecure_channel(f'{self.host}:{self.server_port}')

        self.stub = pb2_grpc.SearchStub(self.channel)

    def get_url(self, message):
        message = pb2.Message(message=message)
        print(f'{message}')
        return self.stub.GetServerResponse(message)





def ask_for_products(keyword):
    search_client = SearchClient()
    products = []

    result = search_client.get_url(message=keyword)

    # protocol buffer class to dict
    for i in result.product:
        dict = {
            "name": i.name,
            "price": i.price,
            "stock": i.stock
        }
        products.append(dict)

    return products






app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/inventory/search")
def search_inventory():
    search_query = request.args.get("q")                    # obtiene el parametro q
    cache_products = cache.cache_fetch_products(key=search_query)        # busca en el cache

    if cache_products:                                         # si hay resultado en el cache
        return jsonify({"products_list":cache_products})       # arma el json y lo manda

    else:
        # es decir el string de la b ́usqueda es la llave y el valor es el resultado
        invetory_products = ask_for_products(search_query)
        cache.cache_insert_json(search_query, invetory_products)
        return jsonify({"products_list": invetory_products})

    

if __name__ == "__main__":
    app.run(debug=True)