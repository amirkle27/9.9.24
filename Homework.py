import sqlite_lib

sqlite_lib.connect('eurovision_db.db')

#2
def eurovision_table ():
    table:list[tuple] = sqlite_lib.run_query_select("""SELECT * FROM eurovision_winners ew""")
    print("Year"," "*3,"Country"," "*11,"Winner"," "*33,"Host Country"," "*6,"Song Name")
    print("="*100)
    for row in table:
        year,country,winner,host_country,song_name = row
        print (f"{year:<9}{country:<20}{winner:<41}{host_country:<20}{song_name}")
    sqlite_lib.close()

if __name__ == "__main__":
    (eurovision_table())

#3.1
def ask_for_country_and_year ():
    country = input("Which Country?")
    year = input("Which Year?")
    return country, year


def country_year_winner(country: str = 'israel', year: str = '2018'):
    sqlite_lib.connect('eurovision_db.db')
    country, year = ask_for_country_and_year()
    song_name = sqlite_lib.run_query_select(f"SELECT song_name FROM eurovision_winners ew WHERE country LIKE '{country}' AND year = {year}")
    if song_name:
        return (song_name [0][0])
    else:
        return "Wrong"

    sqlite_lib.close()

if __name__ == "__main__":
    print(country_year_winner())

#3.2

def check_winner_filter(country:str = 'israel', year:str = '2018'):
    sqlite_lib.connect('eurovision_db.db')
    result_sql = sqlite_lib.run_query_select(f"SELECT * from eurovision_winners")
    ask_for_country_and_year()
    for details in result_sql:
        Year, Country,winner, host_country, song_name = details
        result = list(filter(lambda details: details[1] == country and str(details[0]) == year, result_sql))
    if result:
        print(result[0][4])
    else:
        print("Wrong")
    sqlite_lib.close()

if __name__ == "__main__":
    check_winner_filter()


#5
def country_year_genre ():
    sqlite_lib.connect('eurovision_db.db')
    result = country_year_winner()
    if result != 'Wrong':
        current_genre = sqlite_lib.run_query_select(f"SELECT genre FROM song_details WHERE year = (SELECT year FROM eurovision_winners WHERE song_name LIKE'{result}')")
        current_genre_value = current_genre[0][0] if current_genre else None
        genre = input("Enter the Genre")
        while genre == current_genre_value:
            genre = input("Enter a new Genre")
        sqlite_lib.run_query_update(
            f"UPDATE song_details SET genre = '{genre}'WHERE year = (SELECT year FROM eurovision_winners WHERE song_name LIKE '{result}')")
        print('Done')
    sqlite_lib.close()
if __name__ == "__main__":
    country_year_genre()



def country_year_winner_for_test (country, year):
    sqlite_lib.connect('eurovision_db.db')
    song_name = sqlite_lib.run_query_select(f"SELECT song_name FROM eurovision_winners ew WHERE country LIKE '{country}' AND year LIKE {year}")
    if song_name:
        return song_name [0][0]
    else:
        return "Wrong"
    sqlite_lib.close()



