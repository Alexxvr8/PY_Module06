#!/usr/bin/env python3
"""ft_transmutation_1.py: reach the recipe through the transmutation module."""


import alchemy.transmutation


def main() -> None:
    """Transmute lead into gold using the transmutation subpackage."""
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    gold = alchemy.transmutation.lead_to_gold()
    print(f"Testing lead to gold: {gold}")


if __name__ == "__main__":
    main()
    print("\n=== End of Program ===")
