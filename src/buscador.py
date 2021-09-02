from flask import Flask, request, jsonify
import cache
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/inventory/search")
def search_inventory():
    search_query = request.args.get("q")
    cache_items = cache.cache_load_json(key=search_query)

    if cache_items:
        return jsonify({"products_list":cache_items})

    else:
        # es decir el string de la b ́usqueda es la llave y el valor es el resultado
        return f"no result for \"{search_query}\""
    

if __name__ == "__main__":
    app.run(debug=True)