from itertools import count

import sqlite_lib

sqlite_lib.connect('eurovision_db.db')

#2
def eurovision_table ():
    table:list[tuple] = sqlite_lib.run_query_select("""SELECT * FROM eurovision_winners ew""")
    print("Year"," "*3,"Country"," "*11,"Winner"," "*33,"Host Country"," "*6,"Song Name")
    print("="*100)
    for row in table:
        year,country,winner,host_country,song_name = row
        print(f"{year:<9}{country:<20}{winner:<41}{host_country:<20}{song_name}")


    sqlite_lib.close()

if __name__ == "__main__":
    print(eurovision_table())

#3.1

def country_year_winner ():
    sqlite_lib.connect('eurovision_db.db')
    country = input("Country?")
    year = input("Year?")
    song_name = sqlite_lib.run_query_select(f"SELECT song_name FROM eurovision_winners ew WHERE country LIKE '{country}' AND year LIKE {year}")
    if song_name:
        return song_name [0][0]

    else:
        return "Wrong"

    sqlite_lib.close()

if __name__ == "__main__":
    (country_year_winner())


def country_year_winner_for_test (country, year):
    sqlite_lib.connect('eurovision_db.db')
    song_name = sqlite_lib.run_query_select(f"SELECT song_name FROM eurovision_winners ew WHERE country LIKE '{country}' AND year LIKE {year}")
    if song_name:
        return song_name [0][0]
    else:
        return "Wrong"
    sqlite_lib.close()


#3.2

# def check_winner_filter(country, year):
#     result_sql = sqlite_lib.run_query_select(f"SELECT song_name from eurovision_winners ew;")
#     # print(result) [(), () ...]
#     # for row in results:
#     #     year, country, winner, host_country, song_name = row
#     result = list(filter(lambda winner: winner[1] == country and winner[0] == year, result_sql))
#     if result:
#         return result[0][2]  # [(Toy,)]
#     else:
#         return "wrong"

# def main():
#     print(check_winner_filter('israel', 2018))
#     sqlite_lib.connect('hw.db')
#     country = input('country?')
#     year = int(input('year?'))
#     result = check_winner(country, year)
#     print(result)
#     sqlite_lib.close()
#
# print(check_winner_filter(country,year))


# def song_name_filter (country, year):
#     sqlite_lib.connect('eurovision_db.db')
#     country = input("Country?")
#     year = input("Year?")
#     table = sqlite_lib.run_query_select("SELECT song_name FROM eurovision_winners ew")
#     song_name = list(filter(lambda winner: winner[1] == country and winner[0] == year, table))
#     if song_name:
#         return song_name
#     # else:
#     #     return "Wrong"
# print(song_name_filter(country,year,genre=None))

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

(country_year_genre())






