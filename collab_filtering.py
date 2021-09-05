import numpy as np
from math import sqrt


def sim_pearson(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    if len(si) == 0:
        return 0

    # Расчёт коэффициента корреляции Пирсона
    sum1 = sum([prefs[person1][item] for item in si])
    sum2 = sum([prefs[person2][item] for item in si])

    sum1_sq = sum([pow(prefs[person1][item], 2) for item in si])
    sum2_sq = sum([pow(prefs[person2][item], 2) for item in si])

    p_sum = sum([prefs[person1][item] * prefs[person2][item] for item in si])
    num = p_sum - (sum1 * sum2 / len(si))
    den = sqrt((sum1_sq - pow(sum1, 2) / len(si)) * (sum2_sq - pow(sum2, 2) / len(si)))

    if den == 0: return 0
    return num/den

    # Расчёт в одну строку
    # return np.corrcoef([prefs[person1][item] for item in si], [prefs[person2][item] for item in si])[0, 1]


def top_matches(prefs, person, n=3, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]

    scores.sort()
    scores.reverse()
    return scores[0:n]


def get_recommendations(prefs, person, similarity=sim_pearson):
    totals = {}  # хранит к.п. * на оценку
    sim_sums = {}  # к.п.
    for other in prefs:
        if other == person: continue
        sim = similarity(prefs, person, other)
        if sim <= 0: continue
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item] == 0:
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item]*sim

                sim_sums.setdefault(item, 0)
                sim_sums[item] += sim
    rank = [(total / sim_sums[item], item) for item, total in totals.items()]
    rank.sort()
    rank.reverse()
    return rank


# test
users = {
    'User1': {
        'Киров-Советск': 2.5,
        'Киров-Котельнич': 3.5,
        'Киров-Нолинск': 3.0,
        'Киров-Вятские поляны': 3.5,
        'Киров-Яранск': 2.5,
        'Киров-Орлов': 3.0
    },
    'User2': {
        'Киров-Котельнич': 4.5,
        'Киров-Яранск': 1.0,
        'Киров-Вятские поляны': 4.0
    },
    'User3': {
        'Киров-Советск': 2.5,
        'Киров-Котельнич': 3.0,
        'Киров-Вятские поляны': 3.5,
        'Киров-Яранск': 2.0,
        'Киров-Орлов': 3.0
    },
    'User4': {
        'Киров-Орлов': 3.5,
        'Киров-Слободской': 5.0,
        'Киров-Кирово-Чепецк': 2.0
    },
}

print(top_matches(users, 'User2'))
print(get_recommendations(users, 'User2'))
