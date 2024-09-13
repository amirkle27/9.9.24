
import sqlite_lib

sqlite_lib.connect('eurovision_db.db')

answer: list[tuple] = sqlite_lib.run_query_select('''
        SELECT ew.song_name , ew.country , ew.year,
	    sd.song_length_seconds 
        FROM eurovision_winners ew
        JOIN song_details sd USING(YEAR)
        ORDER BY sd.song_length_seconds desc;
    ''')
print(answer)

sheilta15: list[tuple] = sqlite_lib.run_query_select( '''
        SELECT ew.song_name, year 
        FROM eurovision_winners ew
        WHERE ew.country LIKE 'Israel' AND 
            YEAR=(SELECT MIN(YEAR) 
                    FROM eurovision_winners ew
                    WHERE ew.country LIKE 'Israel') 
            OR YEAR=(SELECT MAX(YEAR) 
                    FROM eurovision_winners ew
                    WHERE ew.country LIKE 'Israel');
    ''')
print(sheilta15)

sheilta12: list[tuple] = sqlite_lib.run_query_select('''
        SELECT ew.country, count(ew.country) cnt
        FROM eurovision_winners ew
        GROUP BY ew.country
        HAVING cnt = (SELECT max(cnt) FROM (
        SELECT ew.country, count(ew.country) cnt
        FROM eurovision_winners ew
        GROUP BY ew.country));
    ''')
print(sheilta12)

neta: list[tuple] = sqlite_lib.run_query_select('''
        SELECT *
        FROM song_details 
        WHERE "year" = 2018;
    ''')
print(neta)

sqlite_lib.run_query_update('''
        UPDATE song_details
        SET song_length_seconds = 1750
        WHERE "year" = 2018;
    ''')

neta: list[tuple] = sqlite_lib.run_query_select('''
        SELECT *
        FROM song_details 
        WHERE "year" = 2018;
    ''')
print(neta)

sqlite_lib.close()








#
# if __name__ == '__main__':
#     print_hi('PyCharm')


