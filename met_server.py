import grpc
from concurrent import futures
import time

import MY_example_pb2
import MY_example_pb2_grpc

import mult

c=mult.A()
class multiplicationServicer(MY_example_pb2_grpc.multiplicationServicer):
    def met(self, request, context):
        response =MY_example_pb2.ans()
        response.p=c.met(request.a,request.b)
        return response

server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
MY_example_pb2_grpc.add_multiplicationServicer_to_server(multiplicationServicer(), server)
MY_example_pb2_grpc.add_multiplicationServicer_to_server(multiplicationServicer,server)

print("starting server. listening to port 50051.")
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)