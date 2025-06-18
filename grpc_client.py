import grpc
import hello_pb2
import hello_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = hello_pb2_grpc.HelloServiceStub(channel)

response = stub.SayHello(hello_pb2.HelloRequest(name="Mundo"))
print("Respuesta:", response.message)
