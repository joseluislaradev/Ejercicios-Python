from contextlib import redirect_stdout
from io import StringIO


def countdown(n):
    if n <= 0:
        return n
    
    print(n)
    countdown(n-1)


def capture_countdown(n):
    output = StringIO()

    with redirect_stdout(output):
        countdown(n)

    return output.getvalue().splitlines()


assert capture_countdown(3) == ["3", "2", "1"]
assert capture_countdown(1) == ["1"]
assert capture_countdown(0) == []

print("All tests passed!")