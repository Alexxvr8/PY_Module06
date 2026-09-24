#!/usr/bin/env python3
"""ft_alembic_4.py: show that the alchemy package only exposes some names."""


import alchemy


def main() -> None:
    """Create air, then try to reach the non-exposed create_earth."""
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")

    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    try:
        print(f"Testing the hidden create_earth: {alchemy.create_earth()}")
    except AttributeError as error:
        print(
            "Testing the hidden create_earth: "
            f"{type(error).__name__}: {error}"
        )


if __name__ == "__main__":
    main()
    print("\n=== End of Program ===")
