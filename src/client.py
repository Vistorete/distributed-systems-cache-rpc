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


if __name__ == '__main__':

    client = SearchClient()
    result = client.get_url(message="Hello Server you there?")
    print(f'server: {result}')
    # print(result.product[0].name + "*******")