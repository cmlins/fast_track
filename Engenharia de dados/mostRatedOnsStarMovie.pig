ratings = LOAD 'ml-100k/u.data' as (userID:int, movieID:int, rating:int, ratingTime:int);

metadata = LOAD 'ml-100k/u.item' USING PigStorage('|') AS (movieID:int, movieTitle:chararray, releaseDate:chararray, videoRelease:chararray, imdbLink:chararray);

nameLookup = FOREACH metadata GENERATE movieID, movieTitle, ToUnixTime(ToDate(releaseDate, 'dd-MMM-yyyy')) AS releaseTime;

groupedRatings = GROUP ratings BY movieID;

avgRatings = FOREACH groupedRatings GENERATE group AS movieID, AVG(ratings.rating) AS avgRating, COUNT(ratings.rating) AS numRatings;

badMovies = FILTER avgRatings BY avgRating < 2.0;

namedBadMovies = JOIN badMovies BY movieID, nameLookup BY movieID;

finalResults = FOREACH namedBadMovies GENERATE nameLookup::movieTitle AS movieName, badMovies::avgRating AS avgRating, badMovies::numRatings AS numRatings;

badMoviesSorted = ORDER finalResults BY numRatings DESC;

DUMP badMoviesSorted;