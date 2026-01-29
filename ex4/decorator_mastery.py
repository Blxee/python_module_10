"""Exercise 4: Master’s Tower."""

from sys import stderr
from typing import Callable, Any
from functools import wraps
from time import time, sleep


def spell_timer(func: Callable) -> Callable:
    """Time execution decorator."""

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        seconds: float = time()
        result = func(*args, **kwargs)
        seconds = time() - seconds
        print(f"Spell completed in time {seconds:.2}")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    """Parameterized validation decorator."""

    def decorator(func) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if "power" in kwargs:
                power = kwargs["power"]
            elif len(args) > 0 and isinstance(args[0], int):
                power = args[0]
            else:
                return "Insufficient power for this spell"

            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Retry decorator."""

    def decorator(func) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for i in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... ({i + 1}/{max_attempts})"
                    )
            print(f"Spell casting failed after {max_attempts} attempts")

        return wrapper

    return decorator


class MageGuild:
    """Demonstrate staticmethod."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Check whether name is valid."""
        return (
            isinstance(name, str)
            and len(name) >= 3
            and all(c == " " or c.isalpha() for c in name)
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell."""
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    """Define main entry of the program."""
    print("\n\x1b[32mTesting spell timer...\x1b[0m")

    @spell_timer
    def plasma_bolt(enchantment: str) -> str:
        """Cast an enchanted plasma bolt."""
        sleep(1)
        return f"Casting {enchantment} Plasma Bolt"

    print(f"{plasma_bolt('Deadly') = }")

    print("\n\x1b[32mTesting power validator...\x1b[0m")

    @power_validator(5)
    def fire_ball(power: int) -> str:
        return f"Casting Fire Ball with {power} power"

    print(f"{fire_ball(3) = }")
    print(f"{fire_ball(7) = }")

    print("\n\x1b[32mTesting retry spell...\x1b[0m")

    @retry_spell(2)
    def meteor_shower(mana: int) -> str:
        if mana < 8:
            raise ValueError("There is no enough mana to invoke meteors")
        else:
            return "Casting a Meteor Shower"

    print(f"{meteor_shower(3) = }")
    print(f"{meteor_shower(12) = }")

    print("\n\x1b[32mTesting MageGuild...\x1b[0m")
    print(f"{MageGuild.validate_mage_name('Gandalf the Gray') = }")
    print(f"{MageGuild.validate_mage_name('#4$%  343AAA') = }")

    guild: MageGuild = MageGuild()
    print(f"{guild.cast_spell('Ice Sickle', power=4) = }")
    print(f"{guild.cast_spell('Blinding Light', power=11) = }")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("[Error]:", error, file=stderr)
