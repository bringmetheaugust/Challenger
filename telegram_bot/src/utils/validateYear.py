import datetime

def validateYear(year: str) -> bool or list:
    try:
        isRange: bool = '-' in year
        year = year.strip()

        if isRange:
            years = map(lambda year: year.strip(), year.split('-'))
            
            return all(existedYear(item) for item in years) and years
        else:
            return existedYear(year) and year
    except:
        return False

def existedYear(year: int) -> bool:
    currentYear = datetime.datetime.now().year
    
    try:
        year = int(year)
    except:
        return False

    return year > 1900 and year <= currentYear
