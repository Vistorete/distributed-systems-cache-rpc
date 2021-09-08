from time import sleep
import grpc
from concurrent import futures
import search_pb2_grpc as pb2_grpc
import search_pb2 as pb2
import json


class SearchService(pb2_grpc.SearchServicer):
    def __init__(self):
        pass
    

    def search_in_invetory(self, key_word):
        file = open("invetory_list.json",)
        data_list = json.load(file)
        items = []
        for item in data_list:
            if key_word.upper() in item["name"].upper():
                items.append(item)
                print(item)
        sleep(2)
        return items

    def GetServerResponse(self, request, context):
        message = request.message
        keyword_received = f'{message}'
        print(f"Keyword: {keyword_received}")
        # Aca se debe buscar en el inventario
        # print("inicio")
        result = self.search_in_invetory(keyword_received)
        # print("fin")
        
        # result = {'name': "yes, i am", 'price': 123, "stock": 123}
        search_res = {'product':result}
        return pb2.SearchResults(**search_res)




def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_SearchServicer_to_server(SearchService(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()