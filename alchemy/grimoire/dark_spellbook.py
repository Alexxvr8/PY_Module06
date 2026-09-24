"""dark_spellbook.py: dark magic spellbook, circular import on purpose."""


from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """Return the ingredients allowed in dark magic."""
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """Return whether the spell is recorded or rejected by the validator."""
    result = validate_ingredients(ingredients)
    if result.endswith(" - INVALID"):
        return f"Spell rejected: {spell_name} ({result})"
    return f"Spell recorded: {spell_name} ({result})"
