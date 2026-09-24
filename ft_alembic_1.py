#!/usr/bin/env python3
"""ft_alembic_1.py: access elements.py with 'from ... import ...'."""


from elements import create_water


def main() -> None:
    """Create water through a direct function import."""
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...' structure to access elements.py")
    print(f"Testing create_water: {create_water()}")


if __name__ == "__main__":
    main()
    print("\n=== End of Program ===")
