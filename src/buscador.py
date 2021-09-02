from flask import Flask, request, jsonify
import cache
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/inventory/search")
def search_inventory():
    search_query = request.args.get("q")                    # obtiene el parametro q
    cache_products = cache.cache_load_products(key=search_query)        # busca en el cache

    if cache_products:                                         # si hay resultado en el cache
        return jsonify({"products_list":cache_products})       # arma el json y lo manda

    else:
        # es decir el string de la b ́usqueda es la llave y el valor es el resultado
        return f"no result for \"{search_query}\""
    

if __name__ == "__main__":
    app.run(debug=True)