def convert(time):
    hours, minutes = time.split(':')
    return float(hours) + float(minutes) / 60

def main():
    time = input('Enter the time (in 24-hour format, as ##:##): ')
    hour = convert(time)

    if 7 <= hour < 8:
        print('breakfast time!')
    elif 12 <= hour < 13:
        print('lunch time!')
    elif 18 <= hour < 19:
        print('dinner time!')

if __name__ == '__main__':
    main()
