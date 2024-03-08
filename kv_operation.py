import os
import sys

sys.path.append("bazel-out/k8-fastbuild/bin/")
import pybind_kv

# Change this to your local blockchain
config_path = "ip_address.config"


def set_value(key: str or int or float, value: str or int or float) -> bool:
    """

    :param key: The key you want to set your value to.
    :param value: The key's corresponding value in key value pair.
    :return: True if value has been set successfully.
    """
    return pybind_kv.set(str(key), str(value), os.path.abspath(config_path))


def get_value(key: str or int or float) -> str:
    """

    :param key: The key of the value you want to get in key value pair.
    :return: A string of the key's corresponding value.
    """
    return pybind_kv.get(str(key), os.path.abspath(config_path))
