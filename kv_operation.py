import os
import sys

sys.path.append("bazel-out/k8-fastbuild/bin/")
import pybind_kv


def set_value(key: str or int or float, value: str or int or float, config_path: str) -> bool:
    """

    :param key: The key you want to set your value to.
    :param value: The key's corresponding value in key value pair.
    :param config_path: The path to .config file of the blockchain(For main chain the config file should be `5 44.193.63.142 17005`)
    :return: True if value has been set successfully.
    """
    return pybind_kv.set(str(key), str(value), os.path.abspath(config_path))


def get_value(key: str or int or float, config_path: str) -> str:
    """

    :param key: The key of the value you want to get in key value pair.
    :param config_path: The path to .config file of the blockchain(For main chain the config file should be `5 44.193.63.142 17005`)
    :return: A string of the key's corresponding value.
    """
    return pybind_kv.get(str(key), os.path.abspath(config_path))


