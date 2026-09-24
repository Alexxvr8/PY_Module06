"""light_spellbook.py: light magic spellbook recording validated spells."""


from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    """Return the ingredients allowed in light magic."""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Return whether the spell is recorded or rejected by the validator."""
    result = validate_ingredients(ingredients)
    if result.endswith(" - INVALID"):
        return f"Spell rejected: {spell_name} ({result})"
    return f"Spell recorded: {spell_name} ({result})"
