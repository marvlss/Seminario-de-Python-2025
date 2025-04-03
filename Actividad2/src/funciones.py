# Mis funciones


def increase_values(ROriginal, RFinal):
    max = 0
    mvp = ""
    for player in RFinal:
        RFinal[player]["kills"] += ROriginal[player]["kills"]
        RFinal[player]["assists"] += ROriginal[player]["assists"]
        if ROriginal[player]["deaths"]:
            RFinal[player]["deaths"] += 1
        round_points = increase_points(ROriginal[player])
        RFinal[player]["points"] += round_points
        if round_points > max:
            max = round_points
            mvp = player
    RFinal[mvp]["mvps"] += 1

def increase_points(player):
    total = (player["kills"] * 3) + (player["assists"])
    if player["deaths"]:
        total -= 1
    return total