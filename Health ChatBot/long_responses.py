import random





def unknown():
    response = ["Could you please say it again ? ",
                "...",
                "what?",
                "What does that mean?"][
        random.randrange(4)]
    return response