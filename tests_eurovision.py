import sqlite_lib
import pytest




@pytest.fixture
def before_after_operations_db():
    # BEFORE
    sqlite_lib.connect('eurovision_db.db')

    yield  # test_get_years



    # AFTER
    sqlite_lib.close()


#1
def test_winning_number (before_after_operations_db):
    number_of_songs = sqlite_lib.run_query_select("""SELECT COUNT (*) FROM eurovision_winners ew""")
    assert number_of_songs == [(68,)]

def test_songs_number (before_after_operations_db):
    number_of_songs = sqlite_lib.run_query_select("""SELECT COUNT (*) FROM song_details sd""")
    assert number_of_songs == [(68,)]

#4
def test_question_3_True (before_after_operations_db):
    from Homework import country_year_winner_for_test
    result = country_year_winner_for_test('Israel', 2018)
    assert result == 'Toy'

def test_question_3_False (before_after_operations_db):
    from Homework import country_year_winner_for_test
    result = country_year_winner_for_test('sweden', 2016)
    assert result == 'Wrong'

def test_question_3_full_chart_True (before_after_operations_db):
    from Homework import country_year_winner_for_test
    table: list(tuple()) = sqlite_lib.run_query_select("SELECT * FROM eurovision_winners ew")
    for song in table:
        year, country, winner, host_country, song_name = song
        result = country_year_winner_for_test('Israel', 1978)
        if song[1]==result[1] and song[0] == result[0]:
            assert result == 'A-Ba-Ni-Bi'

def test_question_3_full_chart_False (before_after_operations_db):
    from question_3_for_test import country_year_winner_for_test
    table: list(tuple()) = sqlite_lib.run_query_select("SELECT * FROM eurovision_winners ew")
    for song in table:
        year, country, winner, host_country, song_name = song
        result = country_year_winner_for_test('Israel', 1965)
        if song[1] != result[1] or song[0] != result[0]:
            assert result == 'Wrong'



