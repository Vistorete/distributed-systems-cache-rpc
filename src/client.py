import grpc
import search_pb2_grpc as pb2_grpc
import search_pb2 as pb2
# test

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


if __name__ == '__main__':

    search_client = SearchClient()
    key_word = "gb"
    result = search_client.get_url(message=key_word)
    # result = dict(result)
    products = []
    for i in result.product:
        dict = {
            "name": i.name,
            "price": i.price,
            "stock": i.stock
        }
        print(dict)
        products.append(dict)

    print(products)
    
    # print(r"{}".format(result))
    # print(f': {result}')
    # print(result.product[0].name + "*******")