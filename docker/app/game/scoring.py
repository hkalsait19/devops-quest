def calculate_score(base_points, difficulty):
    multiplier = {
        "easy": 1,
        "medium": 2,
        "hard": 3
    }

    return base_points * multiplier.get(difficulty, 1)


def calculate_level(xp):
    if xp >= 1000:
        return "Senior DevOps Engineer"

    if xp >= 500:
        return "DevOps Engineer"

    if xp >= 200:
        return "Junior DevOps Engineer"

    return "Trainee"



from app.game.scoring import calculate_score, calculate_level


def test_score():
    assert calculate_score(100, "easy") == 100


def test_hard_score():
    assert calculate_score(100, "hard") == 300


def test_level():
    assert calculate_level(600) == "DevOps Engineer"