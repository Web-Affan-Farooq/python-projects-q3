def main():
    age = int(input("Enter your age "))
    if ((age >= 16) and (age < 25) and (age < 48)):
        return f" You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48."
    elif ((age >= 16) and (age >= 25) and (age < 48)):
        return f" You can vote in Stanlau where the voting age is 25. You cannot vote in Peturksbouipo where the voting age is 16. You cannot vote in Mayengua where the voting age is 48."
    elif ((age >= 16) and (age >= 25) and (age >= 48)):
        return f"  You cannot vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You can vote in Mayengua where the voting age is 48."
    else :
        return f" You can nither vote in Peturksbouipo, Stanlau or Mayengua"
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    print(main())