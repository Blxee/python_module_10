"""Exercise 1: Higher Realm."""

from sys import stderr
from typing import Callable, Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Combine two spells."""
    if not callable(spell1) or not callable(spell2):
        print(
            "[Error]: invalid argument types for spell_combiner()",
            file=stderr,
        )
        exit(1)
    print(
        f"[INFO]: combining \x1b[33m{spell1.__name__}\x1b[0m "
        f"with \x1b[33m{spell2.__name__}\x1b[0m"
    )

    def result(*args, **kwargs) -> tuple[Any, Any]:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))

    return result


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Amplify spell power."""
    if not callable(base_spell) or not isinstance(multiplier, int):
        print(
            "[Error]: invalid argument types for power_amplifier()",
            file=stderr,
        )
        exit(1)
    print(
        f"[INFO]: amplifying \x1b[33m{base_spell.__name__}\x1b[0m "
        f"\x1b[31m{multiplier}\x1b[0m times"
    )

    def result(*args, **kwargs) -> int:
        return base_spell(*args, **kwargs) * multiplier

    return result


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Cast spell conditionally."""
    if not callable(condition) or not callable(spell):
        print(
            "[Error]: invalid argument types for conditional_caster()",
            file=stderr,
        )
        exit(1)
    print(f"[INFO]: adding condition to \x1b[33m{spell.__name__}\x1b[0m ")

    def result(*args, **kwargs) -> Any | str:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"

    return result


def spell_sequence(spells: list[Callable]) -> Callable:
    """Create spell sequence."""
    if any(not callable(spell) for spell in spells):
        print(
            "[Error]: invalid argument types for spell_sequence()",
            file=stderr,
        )
        exit(1)
    print(
        "[INFO]: making a spell sequence:",
        ", ".join(f"\x1b[33m{spell.__name__}\x1b[0m" for spell in spells),
    )

    def result(*args, **kwargs) -> list[Any]:
        return [spell(*args, **kwargs) for spell in spells]

    return result


def main() -> None:
    """Define main entry of the program."""

    def fire_ball(target: str) -> str:
        return f"Casting a blazing fire ball at the poor {target}..."

    def laser_beam(target: str) -> str:
        return f"Casting a deadly beam of light through {target}..."

    def meteor_shower(target):
        return f"Casting a god damn meteor over {target}'s head D:..."

    def get_power() -> int:
        return 21

    target: str = "Evil Wizard"

    print("\nTesting spell combiner...")
    laser_fire: Callable = spell_combiner(fire_ball, meteor_shower)
    print(laser_fire(target))

    print("\nTesting power amplifier...")
    double_power: Callable = power_amplifier(get_power, 2)
    print("New doubled power:", double_power())

    print("\nTesting conditional caster...")
    cast_if_target: Callable = conditional_caster(
        lambda target: target == "Evil Wizard", fire_ball
    )
    print(cast_if_target(target))
    print(cast_if_target("Good Npc"))

    print("\nTesting spell sequence...")
    demolish_target: Callable = spell_sequence(
        [fire_ball, laser_beam, meteor_shower]
    )
    print(demolish_target(target))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("[Error]:", error, file=stderr)
