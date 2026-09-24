#!/usr/bin/env python3
"""ft_distillation_0.py: access alchemy/potions.py with 'from ... import'."""


from alchemy.potions import healing_potion, strength_potion


def main() -> None:
    """Brew both potions through a direct import from the submodule."""
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_potion: {strength_potion()}")
    print(f"Testing healing_potion: {healing_potion()}")


if __name__ == "__main__":
    main()
    print("\n=== End of Program ===")
