#!/usr/bin/env python3
"""ft_transmutation_0.py: reach recipes.py through its full dotted path."""


import alchemy.transmutation.recipes


def main() -> None:
    """Transmute lead into gold using the recipes submodule directly."""
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    gold = alchemy.transmutation.recipes.lead_to_gold()
    print(f"Testing lead to gold: {gold}")


if __name__ == "__main__":
    main()
    print("\n=== End of Program ===")
