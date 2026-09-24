#!/usr/bin/env python3
"""ft_distillation_1.py: brew potions through the alchemy package."""


import alchemy


def main() -> None:
    """Brew the strength potion and the heal alias from the package."""
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    print(f"Testing heal alias: {alchemy.heal()}")


if __name__ == "__main__":
    main()
    print("\n=== End of Program ===")
