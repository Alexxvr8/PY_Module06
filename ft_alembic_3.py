#!/usr/bin/env python3
"""ft_alembic_3.py: access alchemy/elements.py with 'from ... import ...'."""


from alchemy.elements import create_air


def main() -> None:
    """Create air through a direct import from the submodule."""
    print("=== Alembic 3 ===")
    print(
        "Accessing alchemy/elements.py using 'from ... import ...' structure"
    )
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
    print("\n=== End of Program ===")
