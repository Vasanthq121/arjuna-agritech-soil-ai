def calculate_score(parameters):

    score = 100

    for p in parameters:

        if p["rating"] == "Low":
            score -= 8

        elif p["rating"] == "Medium":
            score -= 3

        elif p["rating"] == "High":
            score -= 1

    return max(score, 0)