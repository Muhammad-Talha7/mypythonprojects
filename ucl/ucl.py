class Club:
    def __init__(self, name, nation, group):
        self.name = name
        self.nation = nation
        self.group = group
        self.played_against = {"A": 0, "B": 0, "C": 0, "D": 0}
        self.matches = set()

with open("D:\\Code\\git\\mypythonprojects\\ucl\\ucl.txt", "r") as f:

    clubs = []
    for line in f:
        name, nation, group = [x.strip().strip('"') for x in line.strip().split(",")]
        clubs.append(Club(name, nation, group))

fixtures = set()
for club in clubs:
    for opponent in clubs:
        if club.name == opponent.name:
            continue
        if club.nation == opponent.nation:
            continue
        if (club.name, opponent.name) in fixtures or (opponent.name, club.name) in fixtures:
            continue
        if club.played_against[opponent.group] >= 2 or opponent.played_against[club.group] >= 2:
            continue
        fixtures.add((club.name, opponent.name))
        club.played_against[opponent.group] += 1
        opponent.played_against[club.group] += 1
        club.matches.add(opponent.name)
        opponent.matches.add(club.name)

print("Fixtures:")
for fixture in fixtures:
    print(f"{fixture[0]} vs {fixture[1]}")

with open("D:\\Code\\git\\mypythonprojects\\ucl\\fixtures.txt", "w") as f:
    for fixture in fixtures:
        f.write(f"{fixture[0]} vs {fixture[1]}\n")
