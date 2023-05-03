from datetime import datetime

def get_season(now, month, day):
    seasons = {'winter': (1, 3, 'Winter'), 'spring': (4, 6, 'Spring'),
               'summer': (7, 9, 'Summer'), 'fall': (10, 12, 'Fall')}
    for season in seasons:
        start_month, end_month, season_name = seasons[season]
        if start_month <= month <= end_month:
            return season_name + ' ' + str(now.year)
    return 'Winter ' + str(now.year+1) if month == 12 and day > 20 else 'Winter ' + str(now.year)


def minutes_since_jan_1_2000(date):
    start_date = datetime.strptime('2000-01-01', '%Y-%m-%d')
    diff = date - start_date
    return diff.days * 1440 + diff.seconds // 60


def minutes_to_words(minutes):
    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
             'seventeen', 'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if minutes == 0:
        return 'zero'
    words = []
    if minutes >= 1000000:
        words.extend(minutes_to_words(minutes // 1000000))
        words.append('million')
        minutes %= 1000000
    if minutes >= 1000:
        words.extend(minutes_to_words(minutes // 1000))
        words.append('thousand')
        minutes %= 1000
    if minutes >= 100:
        words.append(ones[minutes // 100])
        words.append('hundred')
        minutes %= 100
    if minutes >= 20:
        words.append(tens[minutes // 10 - 2])
        minutes %= 10
    if 10 <= minutes < 20:
        words.append(teens[minutes - 10])
        minutes = 0
    if minutes < 10:
        words.append(ones[minutes])
    return ' '.join(words)


def main():
    today = datetime(2000, 1, 1)
    test_cases = ['1999-01-01', '2001-01-01', '1995-01-01', '2020-06-01', '1998-06-20']

    for date_str in test_cases:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        minutes = minutes_since_jan_1_2000(date)
        words = minutes_to_words(minutes)
        season = get_season(today, date.month, date.day)
        print(f"{date_str}: {words} minutes since Jan 1, 2000, {season}")

if __name__ == '__main__':
    main()
