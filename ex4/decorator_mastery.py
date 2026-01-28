"""Exercise 4: Master’s Tower."""

from sys import stderr
from typing import Callable
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    """Time execution decorator."""

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        print(f"Casting {func.__name__}...")
        func(*args, **kwargs)
        print("Spell completed in time seconds")

    return wrapper


def power_validator(min_power: int) -> Callable:
    """Parameterized validation decorator."""

    def decorator(func) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> None:
            if power >= min_power:
                func(*args, **kwargs)
            else:
                print("Insufficient power for this spell")

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Retry decorator."""

    def decorator(func) -> Callable:
        def wrapper(*args, **kwargs) -> None:
            for i in range(max_attempts):
                try:
                    return func()
                except Exception:
                    print(f"Spell failed, retrying... ({i}/{max_attempts})")
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


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("[Error]:", error, file=stderr)
