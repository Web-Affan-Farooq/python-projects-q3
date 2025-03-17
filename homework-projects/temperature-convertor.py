def main():
    temperature = input("Enter temperature in farenheit and i'll convert that into celcius for you ")
    calc = (float(temperature) - 32 )* (5.0/9.0)
    print(f"{temperature} deg. farenheit = {calc:2f} deg. celcius")
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()