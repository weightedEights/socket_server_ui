"""
Funcs file.
"""


def func1() -> int:
    try:
        print(f"func1 running")
        return 1

    except Exception as e:
        print(f"{e}")
        return 0
