"""Exercise 0: Lambda Sanctum."""

from sys import stderr


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort artifacts based on power."""
    if not isinstance(artifacts, list) or any(
        not isinstance(i, dict) for i in artifacts
    ):
        print("[Error]: invalid arguments to artifact_sorter()", file=stderr)
        return []
    return sorted(
        artifacts, key=lambda artifact: artifact.get("power", 0), reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filter mages with power >= min_power."""
    if (
        not isinstance(mages, list)
        or any(not isinstance(i, dict) for i in mages)
        or not isinstance(min_power, int)
    ):
        print("[Error]: invalid arguments to power_filter()", file=stderr)
        return []
    return list(filter(lambda mage: mage.get("power", 0) >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Surround spell names with asterisk."""
    if not isinstance(spells, list) or any(
        not isinstance(i, str) for i in spells
    ):
        print("[Error]: invalid arguments to spell_transformer()", file=stderr)
        return []
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Calculate stats about the given mages."""
    if not isinstance(mages, list) or any(
        not isinstance(i, dict) for i in mages
    ):
        print("[Error]: invalid arguments to mage_stats()", file=stderr)
        return {}
    powers: list[int] = list(map(lambda mage: mage.get("power", 0), mages))
    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2),
    }


def main() -> None:
    """Define main entry of the program."""
    artifacts = [
        {"name": "Ice Wand", "power": 66, "type": "focus"},
        {"name": "Ice Wand", "power": 63, "type": "weapon"},
        {"name": "Shadow Blade", "power": 90, "type": "focus"},
        {"name": "Shadow Blade", "power": 73, "type": "weapon"},
    ]
    mages = [
        {"name": "Jordan", "power": 82, "element": "ice"},
        {"name": "Morgan", "power": 75, "element": "fire"},
        {"name": "Jordan", "power": 90, "element": "lightning"},
        {"name": "Ember", "power": 67, "element": "water"},
        {"name": "Phoenix", "power": 96, "element": "ice"},
    ]
    spells = ["shield", "fireball", "tornado", "blizzard"]

    print("\nTesting artifact sorter...")
    print(artifact_sorter(artifacts))

    print("\nTesting power filter...")
    print(power_filter(mages, 85))

    print("\nTesting spell transformer...")
    print(spell_transformer(spells))

    print("\nTesting mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("[Error]:", error, file=stderr)
