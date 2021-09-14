# distributed systems cache rpc
 
## Redis install
https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-20-04-es

## gRPC proto3
python -m grpc_tools.protoc --proto_path=. ./search.proto --python_out=. --grpc_python_out=.


config set maxmemory 20M
config get maxmemory

config set maxmemory-policy volatile-lru
config get maxmemory-policy
test
asdas