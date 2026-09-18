import random


challenges = {
    "happy": [
        "Придумай назву для своєї гри",
        "Напиши 3 речі, які сьогодні вдалися"
    ],
    "tired": [
        "Зроби перерву на 5 хвилин",
        "Намалюй простий план свого дня"
    ],
    "bored": [
        "Придумай нове правило для улюбленої гри",
        "Зміни щось маленьке у своїй кімнаті"
    ]
}


study_challenges = [
    "Повтори 3 нові Python-команди",
    "Поясни другу, що таке змінна",
    "Знайди одну помилку в маленькому коді",
    "Напиши 3 рядки коду з print()"
]


default_challenges = [
    "Випий води",
    "Запиши одну маленьку ціль на сьогодні"
]


def choose_challenge(mood, energy, mode):
    if mode == "study":
        challenge = random.choice(study_challenges)

    elif mood == "happy":
        challenge = random.choice(challenges["happy"])

    elif mood == "tired" or mood == "bored":
        challenge = random.choice(challenges[mood])

    else:
        challenge = random.choice(default_challenges)

    return challenge


def calculate_points(energy, mode):
    if energy < 1 or energy > 10:
        return 0

    points = 5

    if energy >= 7:
        points += 3

    elif energy <= 3:
        points += 1

    if mode == "study":
        points += 2

    return points


print("=== Генератор міні-челенджів ===")

name = input("Як тебе звати? ")

mood = input("Який у тебе настрій? happy / tired / bored: ").lower()

energy = int(input("Скільки в тебе енергії від 1 до 10? "))

mode = input("Обери режим fun або study: ").lower()

challenge = choose_challenge(mood, energy, mode)

points = calculate_points(energy, mode)

print()
print(f"{name}, твій челендж:")
print(challenge)
print(f"Бали за виконання: {points}")