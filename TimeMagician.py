def dates(month):
    month_days = (30, 14, 30, 31, 30, 31, 30, 31, 30, 31, 30, 31)
    if 1 <= month <= 12:
        return month_days[month-1]
    return -1

def find_date(day, month):
    month_days = (30, 14, 30, 31, 30, 31, 30, 31, 30, 31, 30, 31)
    total_days = sum(month_days[:month-1]) + day - 5
    
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days_of_week[total_days % 7]

def main():
    x = int(input())
    y = int(input())

    if x < 1 or x > dates(y):
        print("Invalid Time")
    else:
        print(find_date(x, y))

if __name__ == "__main__":
    main()
