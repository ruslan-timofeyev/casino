import random

def spin_wheel():
    segments = [
        ("🔴 0", 0),
        ("🟢 0.5", 0.5),
        ("🟡 1", 1),
        ("🟣 2", 2),
        ("🔵 Джекпот! 5", 5)
    ]
    result = random.choice(segments)
    return result
