from .__main__ import main
from .fibonacci_sequence import fibonacci_sequence
from typing import Any, Dict

main("Greetings from pr_var module")
value: Dict[str, Any] = fibonacci_sequence(4)

if not value:
    x: str = "Hello"
    print(x)
