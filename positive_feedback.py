def positive_feedback(ratings):
    if len(ratings) == 0:
        return 0
    c = 0
    for r in ratings:
        if r >= 4:
            c+= 1
    return (c/ len(ratings)) * 100
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print("Positive Feedback:", positive_feedback(ratings), "%")
