def route_agent(problem):

    problem = problem.lower()


    habit_keywords = [
        "habit",
        "sleep",
        "wake",
        "exercise",
        "health",
        "routine",
        "lifestyle",
        "social media",
        "morning",
        "daily habits",
        "healthy"
    ]


    productivity_keywords = [
        "assignment",
        "deadline",
        "task",
        "project",
        "study",
        "time management",
        "productivity",
        "focus",
        "work",
        "office"
    ]


    habit_score = 0
    productivity_score = 0


    for word in habit_keywords:
        if word in problem:
            habit_score += 1


    for word in productivity_keywords:
        if word in problem:
            productivity_score += 1



    if habit_score > productivity_score:
        return "habit"


    elif productivity_score > habit_score:
        return "productivity"


    else:
        return "productivity"