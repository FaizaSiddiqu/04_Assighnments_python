DAY_IN_YEAR = 365
HOURS_IN_DAY = 24
MIN_PER_HOUR = 60
SECONDS_IN_MIN = 60

def main():
    total_seconds = DAY_IN_YEAR * HOURS_IN_DAY * MIN_PER_HOUR * SECONDS_IN_MIN
    print(f"There are {total_seconds} seconds in a year.")
    
if __name__ == "__main__":
    main()