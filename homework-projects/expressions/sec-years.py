DAYS_IN_YEAR = 365
HOURS_IN_DAY=24
MINUTES_IN_HOUR = 60
SECS_IN_MINUTES = 60
def main():
    secs = DAYS_IN_YEAR*HOURS_IN_DAY*MINUTES_IN_HOUR*SECS_IN_MINUTES
    return f"There are {secs} in one year"

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    print(main())