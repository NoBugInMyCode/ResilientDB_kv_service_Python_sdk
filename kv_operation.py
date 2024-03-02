import os
import sys

sys.path.append("bazel-out/k8-fastbuild/bin/")
import pybind_kv


def set_value(key: str or int or float, value: str or int or float, config_path: str) -> bool:
    return pybind_kv.set(str(key), str(value), os.path.abspath(config_path))


def get_value(key: str or int or float, config_path: str) -> str:
    return pybind_kv.get(str(key), os.path.abspath(config_path))
