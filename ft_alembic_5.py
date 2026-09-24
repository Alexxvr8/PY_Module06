#!/usr/bin/env python3
"""ft_alembic_5.py: access the alchemy package with 'from alchemy import'."""


from alchemy import create_air


def main() -> None:
    """Create air through the public interface of the package."""
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
    print("\n=== End of Program ===")
