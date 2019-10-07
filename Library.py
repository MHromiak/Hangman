from random import randint as ri

level_1 = ["cat", "house", "ice cream", "basic", "acidic", "seven", "owl", "myth", "lose", "fear", "sun", "light"]
level_2 = ["cactus water", "python", "jazz", "nuclear", "bebop", "outer space", "kuiper belt", "jupiter"]
level_3 = ["diktat", "complete", "metallic", "arc de triumph", "whoops", "call me ishmael"]
level_4 = ["differentiation", "counterintuitive", "zephyr", "tellurian", "mythril", "the louvre", "youre a wizard harry"]
level_5 = ["apoptotic", "floccinaucinihilipilification", "tohubohu", "methylenedioxymethamphetamine", "doxology", "gymnopedie", "obfuscate", "perspicacity"]


def default():
    print("Try another input")
def getWord(difficulty):

    levelChosen = level_1 if difficulty == '1' else level_2 if difficulty == '2' else level_3 if difficulty == '3' else level_4 if difficulty == '4' else level_5
    wordIndex = ri(0, len(levelChosen) - 1)  # pseudo-random index for word choice. Becomes more usuful with larger word banks
    return levelChosen[wordIndex]




