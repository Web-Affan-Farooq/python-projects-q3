MAX_COUNT = 10000
def main():
    term_1 = 0
    term_2 = 1
    while (term_1 < MAX_COUNT):
        print(term_1)
        term_count = term_1 + term_2
        term_1 = term_2
        term_2 = term_count

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()