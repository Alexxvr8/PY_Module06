"""potions.py: alchemy submodule brewing potions from the four elements."""


from elements import create_fire, create_water
from alchemy.elements import create_earth, create_air


def healing_potion() -> str:
    """Return the healing potion brewed with earth and air."""
    return (
        f"Healing potion brewed with '{create_earth()}' "
        f"and '{create_air()}'"
    )


def strength_potion() -> str:
    """Return the strength potion brewed with fire and water."""
    return (
        f"Strength potion brewed with '{create_fire()}' "
        f"and '{create_water()}'"
    )
