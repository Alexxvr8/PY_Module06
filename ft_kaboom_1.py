#!/usr/bin/env python3
"""ft_kaboom_1.py: import dark_spellbook.py directly and trigger a cycle."""


def main() -> None:
    """Import the dark spellbook late so the explosion follows the prints."""
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire.dark_spellbook import dark_spell_record

    spell = dark_spell_record("Nightmare", "Bats and frogs")
    print(f"Testing record dark spell: {spell}")


if __name__ == "__main__":
    main()
    print("\n=== End of Program ===")
