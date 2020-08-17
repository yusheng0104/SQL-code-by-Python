#
# CSCI E-66: Problem Set 1, SQL Programming Problems
#

#
# For each problem, use a text editor to add the appropriate SQL
# command between the triple quotes provided for that problem's variable.
#
# For example, here is how you would include a query that finds the
# names and years of all movies in the database with an R rating:
#
sample = """
	 SELECT name, year
         FROM Movie
         WHERE rating = 'R';
         """

#
# Problem 5. Put your SQL command between the triple quotes found below.
#
problem5 = """
	   SELECT name, dob, pob
	   FROM Person
	   WHERE name = 'Emma Stone' OR name = 'Rachel Weisz';
           """

#
# Problem 6. Put your SQL command between the triple quotes found below.
#
problem6 = """
	   SELECT count(*)
	   FROM Movie
	   WHERE runtime>200;
           """

#
# Problem 7. Put your SQL command between the triple quotes found below.
#
problem7 = """
	   SELECT movie.name, Oscar.type, oscar.year
	   FROM Oscar LEFT JOIN Movie on movie.id = Oscar.movie_id
	   WHERE Oscar.person_id = (SELECT id										    FROM Person										    WHERE name='Christian Bale');
           """

#
# Problem 8. Put your SQL command between the triple quotes found below.
#
problem8 = """
           SELECT count(*)
	   FROM Person
	   WHERE id in (SELECT director_id
	        	FROM Director
			WHERE movie_id in (SELECT movie_id
					   FROM Actor
					   WHERE actor_id in (SELECT id
							      FROM Person
							      WHERE id in (SELECT actor_id FROM Actor) AND pob not like '%USA'
							      GROUP by id))) AND pob not like '%USA';
           """

#
# Problem 9. Put your SQL command between the triple quotes found below.
#
problem9 = """
           SELECT DISTINCT year, avg(runtime)
	   FROM Movie
	   where year>1999
	   group by year;
           """

#
# Problem 10. Put your SQL command between the triple quotes found below.
#
problem10 = """
            SELECT name, dob
	    FROM Person
	    WHERE name like 'Sam %';
            """

#
# Problem 11. Put your SQL command between the triple quotes found below.
#
problem11 = """
            SELECT name 
	    FROM Movie
	    WHERE runtime < (SELECT min(m.runtime)
			     FROM Oscar o LEFT OUTER JOIN Movie m on o.movie_id=m.id
			     WHERE type like 'Best-Picture');
            """

#
# Problem 12. Put your SQL command between the triple quotes found below.
#
problem12 = """
            SELECT p.name, target.num
	    FROM (SELECT d.director_id d_id, count(*) num
	          FROM Movie m LEFT OUTER JOIN Director d on m.id = d.movie_id
		  WHERE m.earnings_rank NOTNULL
		  GROUP by d.director_id
		  ORDER by num DESC) target LEFT OUTER JOIN Person p on target.d_id=p.id
	    WHERE target.num>3;
            """

#
# Problem 13. Put your SQL command between the triple quotes found below.
#
problem13 = """
            SELECT m.earnings_rank, m.name, count(o.type)
	    FROM Movie m LEFT OUTER JOIN Oscar o on m.id = o.movie_id
	    WHERE m.earnings_rank NOTNULL AND m.earnings_rank<26
	    GROUP by m.name
	    ORDER by m.earnings_rank;
            """

#
# Problem 14. Put your SQL command between the triple quotes found below.
#
problem14 = """
	    SELECT count(*)
	    FROM(SELECT actor_id
	         FROM Actor
	         WHERE actor_id NOT in (SELECT actor_id 
					FROM Actor
					WHERE movie_id in (SELECT id
							   FROM Movie
							   WHERE earnings_rank NOTNULL))
	    GROUP by actor_id);
            """

#
# Problem 15. Put your SQL command between the triple quotes found below.
#
problem15 = """
            SELECT name movie, 'actor' function
	    FROM Movie
	    WHERE id in(SELECT movie_id
			FROM Actor
			WHERE actor_id in (SELECT id
					   FROM Person
					   WHERE name ='Denzel Washington'))
	    UNION
	    SELECT name movie, 'Director' function
	    FROM Movie
	    WHERE id in(SELECT movie_id
			FROM Director
			WHERE director_id in (SELECT id
					      FROM Person
		  			      WHERE name ='Denzel Washington'));
            """

#
# Problem 16. Put your SQL command between the triple quotes found below.
#
problem16 = """
            SELECT Gmovie.name, max(bPicture.year) 
	    FROM (
	    SELECT movie_id, year 
	    FROM Oscar
	    WHERE type ='BEST-PICTURE') bPicture JOIN (SELECT id, name
	    FROM Movie
	    WHERE rating ='G') Gmovie on Gmovie.id=bPicture.movie_id;
            """

#
# Problem 17. Put your SQL command between the triple quotes found below.
#
problem17 = """
            UPDATE Movie
	    SET rating = 'PG-13'
	    WHERE name = 'Indiana Jones and the Temple of Doom';
            """

#
# Problem 18 (required for grad-credit students; optional for others). 
# Put your SQL command between the triple quotes found below.
#
problem18 = """
            SELECT name, comb.year
	    FROM Movie, (
	        SELECT o1.id1, o1.year
	        FROM (SELECT movie_id id1, year
	            FROM Oscar
	            WHERE type = 'BEST-DIRECTOR') o1 JOIN 
	             (SELECT movie_id id2, year 
		    FROM Oscar 
		    WHERE type='BEST-PICTURE') o2 on o1.id1 =o2.id2) comb
	    WHERE Movie.id = comb.id1;
            """

#
# Problem 19 (required for grad-credit students; optional for others). 
# Put your SQL command between the triple quotes found below.
#
problem19 = """
            SELECT ratingTable.rating, min(ratingTable.avgtime)
	    FROM (SELECT rating, avg(runtime) avgtime
	    FROM Movie
	    GROUP by rating) ratingTable;
            """
