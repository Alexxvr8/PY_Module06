#!/usr/bin/env python3
"""ft_kaboom_0.py: record a light spell through the grimoire package."""


from alchemy.grimoire import light_spell_record


def main() -> None:
    """Record a light spell without triggering a circular import."""
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    spell = light_spell_record("Fantasy", "Earth, wind and fire")
    print(f"Testing record light spell: {spell}")


if __name__ == "__main__":
    main()
    print("\n=== End of Program ===")
