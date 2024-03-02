py_library(
    name = "your_python_package",
    srcs = glob(["*.py"]),
    data = ["//cpp_source:pybind_kv.so"],  # 引用 cpp_source/BUILD 中定义的目标
    deps = [
        # Python 依赖
    ],
)