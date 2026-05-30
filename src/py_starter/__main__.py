"""Entry point: run via `python -m py_starter` or the `py-starter` script."""

from py_starter.math_utils import add, multiply


def main() -> None:
    a, b = 6, 7
    print(f"add({a}, {b}) = {add(a, b)}")
    print(f"multiply({a}, {b}) = {multiply(a, b)}")


if __name__ == "__main__":
    main()
