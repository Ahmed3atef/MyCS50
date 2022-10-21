# main program
def main():

    # user input
    st = input("Text: ")

    # counters
    wol = len(st)
    letter = 0
    word = 0
    sentence = 0
    key = True

    # char checker
    for i in range(wol):

        if (ord(st[i]) >= 65 and ord(st[i]) <= 90) or (ord(st[i]) >= 97 and ord(st[i]) <= 122):
            letter += 1

        if ord(st[i]) == 32:
            key = True

        else:
            if key == True and ((ord(st[i]) >= 65 and ord(st[i]) <= 90) or (ord(st[i]) >= 97 and ord(st[i]) <= 122)):
                word += 1
                key =False

        if (ord(st[i]) == 63) or (ord(st[i]) == 46) or (ord(st[i]) == 33):
            sentence += 1

    sum_of = ReadAbility_test(letter, sentence, word)

    if sum_of < 1:
        print("Before Grade 1")
    elif sum_of > 16:
        print("Grade 16+")
    else:
        print(f"Grade {round(sum_of)}")

# calculate the score
def ReadAbility_test(L, S, W):

    avg_l = float((L / W) * 100)
    avg_s = float((S / W) * 100)
    total = ((0.0588 * avg_l) - (0.296 * avg_s) - 15.8)
    return total

if __name__ == "__main__":
    main()