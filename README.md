# ResilientDB kv-Service Python API(Get and Set Command)

## Description
This project is to allow users to directly use kv-service of the ResilientDB without going through 
GraphQL

## How to Run
1. Make sure you have installed bazel5.0 and pybind11
2. Run command `bazel build :pybind_kv_so`
3. From `kv_operation.py` import `get_value` and `set_value` function into your Python file to use it

## Example
TODO