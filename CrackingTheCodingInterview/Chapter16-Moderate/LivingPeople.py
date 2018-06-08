'''
Year with most people alive
All births and deaths between 1900 and 2000
'''

def max_living(births, deaths):
    births = sorted(births)
    deaths = sorted(deaths)
    b = d = count = m = m_year = 0

    year = 1900
    while year <= 2000 and b < len(births):
        while b < len(births) and births[b] == year:
            count += 1
            b += 1
            if count > m:
                m = count
                m_year = year

        while d < len(deaths) and deaths[d] == year:
            count -= 1
            d += 1
        year += 1
    return (m_year, m)

births = [1900, 1900, 1960]
deaths = [1950, 1950, 1960]
print(max_living(births, deaths))