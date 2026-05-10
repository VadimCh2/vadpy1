with open('airport-codes_csv (6).csv', mode='r', encoding='utf-8') as file:
    for ua_airports in file:
        iso_country = ua_airports.split(';')[5]
        if iso_country ==  "UA":
            name = ua_airports.split(';')[2]
            print(name)