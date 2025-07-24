# outdated.py

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date_input = input("Date: ").strip()

    # Try numeric format: MM/DD/YYYY
    try:
        month, day, year = date_input.split("/")
        month = int(month)
        day = int(day)
        year = int(year)

        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year:04}-{month:02}-{day:02}")
            break
    except:
        pass

    # Try full-text format: Month DD, YYYY
    try:
        if "," in date_input:
            month_str, day_year = date_input.split(" ", 1)
            day_str, year_str = day_year.split(",")
            day = int(day_str.strip())
            year = int(year_str.strip())

            if month_str in months and 1 <= day <= 31:
                month = months.index(month_str) + 1
                print(f"{year:04}-{month:02}-{day:02}")
                break
    except:
        pass
