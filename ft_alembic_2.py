#!/usr/bin/env python3
"""ft_alembic_2.py: access alchemy/elements.py with 'import ...'."""


import alchemy.elements


def main() -> None:
    """Create earth through the full dotted path of the submodule."""
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print(f"Testing create_earth: {alchemy.elements.create_earth()}")


if __name__ == "__main__":
    main()
    print("\n=== End of Program ===")
