"""Exercise 3: Ancient Library."""

from sys import stderr
from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers."""
    operations: dict[str, Any] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min,
    }

    if operation not in operations:
        print("[Error]: there is no such operation:", operation, file=stderr)
        return 0
    else:
        return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Create partial applications."""
    fire_enchant: Callable = partial(
        base_enchantment, power=8, element="Blazing Fire"
    )
    ice_enchant: Callable = partial(
        base_enchantment, power=7, element="Frozen Essence"
    )
    lightning_enchant: Callable = partial(
        base_enchantment, power=12, element="Lightning Stone"
    )

    return {
        "fire_enchant": fire_enchant,
        "ice_enchant": ice_enchant,
        "lightning_enchant": lightning_enchant,
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    """Create cached fibonacci."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    """Create single dispatch system."""

    @singledispatch
    def cast_spell(arg: Any) -> str:
        """Cast anything."""
        return f"You just casted your damn {arg} ;-; ..."

    @cast_spell.register(int)
    def _(damage: int) -> str:
        """Cast with damage."""
        return f"Casting a spell with {damage} damage..."

    @cast_spell.register(str)
    def _(enchantment: str) -> str:
        """Cast with enchantment."""
        return f"Casting a spell with the {enchantment} enchantment..."

    @cast_spell.register(list)
    def _(spells: list[str]) -> str:
        """Cast multiple spells."""
        return f"Casting multiple spells: {', '.join(map(str, spells))}"

    return cast_spell


def main() -> None:
    """Define main entry of the program."""
    print("\nTesting spell reducer...")
    nums: list[int] = [12, 34, 6, 1, 67]
    print(f"\t{spell_reducer(nums, 'add')=}")
    print(f"\t{spell_reducer(nums, 'multiply')=}")
    print(f"\t{spell_reducer(nums, 'max')=}")
    print(f"\t{spell_reducer(nums, 'min')=}")

    def base_enchantment(target: str, power: int, element: str) -> str:
        return (
            f"Enchanted {target} using {element},"
            f" increasing power by {power}..."
        )

    print("\nTesting partial enchanter...")
    enchants: dict[str, Callable] = partial_enchanter(base_enchantment)
    fire_enchant = enchants["fire_enchant"]
    ice_enchant = enchants["ice_enchant"]
    lightning_enchant = enchants["lightning_enchant"]
    target: str = "Sword"
    print(f"\t{fire_enchant(target)=}")
    print(f"\t{ice_enchant(target)=}")
    print(f"\t{lightning_enchant(target)=}")

    print("\nTesting memoized fibonacci...")
    print(f"\t{memoized_fibonacci(10)=}")
    print(f"\t{memoized_fibonacci(15)=}")

    print("\nTesting spell dispatcher...")
    cast_magic: Callable = spell_dispatcher()
    print(
        f"\tCasting using damage: {cast_magic(12)}",
    )
    print(
        f"\tCasting with enchantment: {cast_magic('Lightning')}",
    )
    print(
        f"\tCasting using damage: {cast_magic(['Fire Ball', 'Ice Spear'])}",
    )
    print(
        f"\tCasting anything: {cast_magic(3.14)}",
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("[Error]:", error, file=stderr)
