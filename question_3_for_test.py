def country_year_winner_for_test (country, year):
    sqlite_lib.connect('eurovision_db.db')
    song_name = sqlite_lib.run_query_select(f"SELECT song_name FROM eurovision_winners ew WHERE country LIKE '{country}' AND year LIKE {year}")
    if song_name:
        return song_name [0][0]
    else:
        return "Wrong"
    sqlite_lib.close()