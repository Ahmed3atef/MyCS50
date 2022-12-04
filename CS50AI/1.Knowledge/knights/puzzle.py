from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # it can't be both but can one of them
    Not(And(AKnight,AKnave)),
    Or(AKnight,AKnave),
    Biconditional(AKnight,And(AKnight,AKnave)),
    Biconditional(AKnave,Not(And(AKnight,AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # it can't be both but can one of them
    Not(And(AKnight,AKnave)),
    Not(And(BKnight,BKnave)),
    Or(AKnight,AKnave),
    Or(BKnight,BKnave),

    # A --> we are both knaves
    # B --> nothing
    Biconditional(AKnight,And(BKnave,AKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # it can't be both but can one of them
    Not(And(AKnight,AKnave)),
    Not(And(BKnight,BKnave)),
    Or(AKnight,AKnave),
    Or(BKnight,BKnave),

    # A ---> same kind
    Biconditional(AKnight,Or(And(AKnight,BKnight),And(AKnave,BKnave))),
    # B ---> different
    Biconditional(AKnave,Or(Not(And(AKnave,BKnave)),Not(And(AKnight,BKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # it can't be both but can one of them
    Not(And(AKnight,AKnave)),
    Not(And(BKnight,BKnave)),
    Not(And(CKnight,CKnave)),
    Or(AKnight,AKnave),
    Or(BKnight,BKnave),
    Or(CKnight,CKnave),

    # 1- I am knight or knave if it true then must he is a knight 
    Biconditional(AKnight,Or(AKnight,AKnave)),
    # 2- a said i am a knave if Aknave == false and Aknight == false then he will be knight 
    Biconditional(BKnight,Biconditional(AKnight,AKnave)),
    # 3- c is a knave if bknight is true then cknave must be true
    Biconditional(BKnight,CKnave),
    # 4- a is a knight 
    Biconditional(CKnight,AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
