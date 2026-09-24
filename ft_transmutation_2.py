#!/usr/bin/env python3
"""ft_transmutation_2.py: reach the recipe through the alchemy package."""


import alchemy


def main() -> None:
    """Transmute lead into gold using only the alchemy package."""
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    gold = alchemy.lead_to_gold()
    print(f"Testing lead to gold: {gold}")


if __name__ == "__main__":
    main()
    print("\n=== End of Program ===")
