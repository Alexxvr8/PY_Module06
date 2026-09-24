"""dark_validator.py: validate dark ingredients, circular import on purpose."""


from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Return the ingredients tagged as VALID or INVALID for dark magic."""
    allowed = dark_spell_allowed_ingredients()
    lowered = ingredients.lower()
    if any(word in lowered for word in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
