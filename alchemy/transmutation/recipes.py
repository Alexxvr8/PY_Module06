"""recipes.py: transmutation recipes mixing elements and potions."""


from elements import create_fire as fire
from ..elements import create_air as air
from alchemy.potions import strength_potion as strength


def lead_to_gold() -> str:
    """Return the recipe that transmutes lead into gold."""
    return (
        f"Recipe transmuting Lead to Gold: brew '{air()}' "
        f"and '{strength()}' mixed with '{fire()}'"
    )
