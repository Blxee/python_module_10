"""Exercise 2: Memory Depths."""

from sys import stderr
from typing import Callable, Any, Hashable


def mage_counter() -> Callable:
    """Create a counting closure."""
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    """Create power accumulator."""
    total_power: int = initial_power

    def increase_power(power: int) -> int:
        nonlocal total_power
        total_power += power
        return total_power

    return increase_power


def enchantment_factory(enchantment_type: str) -> Callable:
    """Create enchantment functions."""

    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    """Create a memory management system."""
    data: dict = {}

    def store(key: Hashable, value: Any) -> None:
        nonlocal data
        data[key] = value

    def recall(key: Hashable) -> Any:
        return data.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall,
    }


def main() -> None:
    """Define main entry of the program."""
    print("\nTesting mage counter...")
    counter = mage_counter()
    print(f"{counter() = }")
    print(f"{counter() = }")
    print(f"{counter() = }")

    print("\nTesting spell accumulator...")
    add_power = spell_accumulator(10)
    print(f"{add_power(4) = }")
    print(f"{add_power(6) = }")
    print(f"{add_power(1) = }")

    print("\nTesting enchantment factory...")
    enchant = enchantment_factory("Flaming")
    print(f"{enchant('Sword') = }")
    print(f"{enchant('Bow') = }")
    enchant = enchantment_factory("Deadly")
    print(f"{enchant('Waraxe') = }")

    print("\nTesting memory vault...")
    data_operations: dict[str, Callable] = memory_vault()
    store: Callable = data_operations["store"]
    recall: Callable = data_operations["recall"]

    print("[INFO]: storing armor and weapon:")
    print(f"{store('armor', 'Diamond Chestplate') = }")
    print(f"{store('weapon', 'Great Fire Sword') = }")
    print("[INFO]: retrieving armor and weapon:")
    print(f"{recall('armor') = }")
    print(f"{recall('weapon') = }")
    print(f"{recall('shield') = }")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("[Error]:", error, file=stderr)
