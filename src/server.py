import grpc
from concurrent import futures
import search_pb2_grpc as pb2_grpc
import search_pb2 as pb2



class SearchService(pb2_grpc.SearchServicer):
    def __init__(self):
        pass

    def GetServerResponse(self, request, context):
        message = request.message
        result = f'Message:"{message}"'
        print(result)
        # Aca se debe buscar en el inventario
        result = {'name': "yes, i am", 'price': 123, "stock": 123}
        search_res = {'product':[result]}
        return pb2.SearchResults(**search_res)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_SearchServicer_to_server(SearchService(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()