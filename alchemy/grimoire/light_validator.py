"""light_validator.py: validate ingredients against the light spellbook."""


def validate_ingredients(ingredients: str) -> str:
    """Return the ingredients tagged as VALID or INVALID for light magic."""
    from .light_spellbook import light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
    lowered = ingredients.lower()
    if any(word in lowered for word in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
