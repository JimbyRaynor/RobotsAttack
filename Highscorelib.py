def save_high_score(myhighscore, filename="highscore.txt"):
    with open(filename, "w") as file:  # file is automatically closed when with block is completed
        file.write(str(myhighscore))

def load_high_score(filename="highscore.txt"):
    try:
        with open(filename, "r") as file:  # file is automatically closed when with block is completed
            return int(file.read())
    except FileNotFoundError:
        return 0  # Default to 0 if no high score file exists