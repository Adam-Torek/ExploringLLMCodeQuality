from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
/0x0D-SQL_introduction/10-top_score.sql
-- lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
SELECT score, name FROM second_table ORDER BY score DESC;
/0x0D-SQL_introduction/13-change_class.sql
-- removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.
DELETE FROM second_table WHERE score <= 5;
/0x0D-SQL_introduction/14-average.sql
-- computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.
SELECT AVG(score) AS average FROM second_table;
/0x0D-SQL_introduction/15-groups.sql
-- lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
/0x0D-SQL_introduction/12-no_cheating.sql
-- updates the score of Bob to 10 in the table second_table.
UPDATE second_table SET score = 10 WHERE name = 'Bob';
/0x0D-SQL_introduction/11-best_score.sql
-- lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
/0x0D-SQL_introduction/16-no_link.sql
-- lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
/0x0D-SQL_introduction/100-move_to_utf8.sql
-- converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
/0x0D-SQL_introduction/1-create_database_if_missing.sql
-- creates the database hbtn_0c_0 in your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
/0x0D-SQL_introduction/101-avg_temperatures.sql
-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
/0x0D-SQL_introduction/102-top_city.sql
-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
/0x0D-SQL_introduction/103-max_state.sql
-- displays the max temperature of each state (ordered by State name).
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
/0x0D-SQL_introduction/104-avg_temperatures.sql
-- displays the average temperature (Fahrenheit) by city ordered by temperature