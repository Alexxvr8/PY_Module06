#!/usr/bin/env python3
"""ft_alembic_0.py: access elements.py with the 'import ...' structure."""


import elements


def main() -> None:
    """Create fire through a plain module import."""
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    print(f"Testing create_fire: {elements.create_fire()}")


if __name__ == "__main__":
    main()
    print("\n=== End of Program ===")
