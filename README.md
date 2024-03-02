# ResilientDB kv-Service Python API(Get and Set Command)

## Description
This project is to allow users to directly use kv-service of the ResilientDB without going through 
GraphQL

## How to Run
1. Run command`./INSTALL.sh`to install bazel5.0 and pybind11
2. From `kv_operation.py` import `get_value` and `set_value` function into your Python file to use it
3. Parameters:
   1. key: The key of the value you want to set or get
   2. value: The key's corresponding value you want to set
   3. config_path: THe path to config file of the blockchain(For main chain the config file should be `5 44.193.63.142 17005`)
   This hasn't to be a absolute path.