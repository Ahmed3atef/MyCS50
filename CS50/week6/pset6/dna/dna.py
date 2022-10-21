from sys import argv, exit
import csv

# calculate the maximum number of times a substring is repeated
def Max_of_length(s, sub):

    ans = [0] * len(s)

    for i in range(len(s) - len(sub), -1, -1):

        if s[i: i + len(sub)] == sub:

            if i + len(sub) > len(s) - 1:
                ans[i] = 1
            else:
                ans[i] =  1 + ans[i + len(sub)]

    return max(ans)

def print_match(r, a):

    for line in r:

        person = line[0]
        value = [ int(val) for val in line[1:] ]
        if value == a:
            print(person)
            return

    print("No match")

def main():
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)
        
    csv_path = argv[1]

    with open(csv_path) as csv_file:

        reader = csv.reader(csv_file)
        #for row in reader:
        #   print()
        all_seq = next(reader)[1:]

        txt_path = argv[2]

        with open(txt_path) as txt_file:

            s = txt_file.read()

            actual = [Max_of_length(s, seq) for seq in all_seq]


        print_match(reader, actual)


if __name__ == "__main__":
    main()