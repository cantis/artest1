import datetime
from arconverter import arConverter

def main():
    defaultResult = arConverter.convert(datetime.datetime.now())
    print(defaultResult)

    result = arConverter.convert(datetime.datetime(2020, 2, 1, 0, 0, 0))
    print(result)
    print(result.longDate())
    print(result.shortDate())
    print(result.month)
    print(result.day)
    print(result.year)
    print(result.weekday)
    print(result.weekdayNum)
    #print(result.weekdayShort)

if __name__ == "__main__":
    main()