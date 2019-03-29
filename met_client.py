import grpc
from random import randint
from timeit import default_timer as timer

import MY_example_pb2
import MY_example_pb2_grpc


start_ch=timer()

# open a gRPC channel
channel=grpc.insecure_channel('localhost:50051')

stub=MY_example_pb2_grpc.multiplicationStub(channel)
end_ch=timer()

start = timer()

requestans=MY_example_pb2.features(a=int(input()),b=int(input()))
responseans=stub.met(requestans)


print("The ans is :",responseans.p)
print('done!')

end = timer()
all_time = end - start
ch_time = end_ch - start_ch
#print ('Time spent for {} ans is {}'.format(len(MSSubClass),(all_time)))
#print('In average, {} second for each prediction'.format(all_time/len(MSSubClass)))
#print('That means you can do {} predictions in one second'.format(int(1/(all_time/len(MSSubClass)))))
print('Time for connecting to server = {}'.format(ch_time))