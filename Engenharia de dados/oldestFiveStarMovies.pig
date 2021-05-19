ratings = LOAD 'ml-100k/u.data' as (userID:int, movieID:int, rating:int, ratingTime:int);

metadata = LOAD 'ml-100k/u.item' USING PigStorage('|') AS (movieID:int, movieTitle:chararray, releaseDate:chararray, videoRelease:chararray, imdbLink:chararray);

nameLookup = FOREACH metadata GENERATE movieID, movieTitle, ToUnixTime(ToDate(releaseDate, 'dd-MMM-yyyy')) AS releaseTime;

ratingsByMovie = GROUP ratings BY movieID;

avgRatings = FOREACH ratingsByMovie GENERATE group AS movieID, AVG(ratings.rating) AS avgRating;

fiveStarMovies = FILTER avgRatings BY avgRating > 4.0;

fiveStarWithData = JOIN fiveStarMovies BY movieID, nameLookup BY movieID;

oldestFiveStarMovies = ORDER fiveStarWithData BY nameLookup::releaseTime;

DUMP oldestFiveStarMovies;

-- LOAD STORE DUMP
-- FILTER DISTINCT  FOREACH/GENERATE MAPREDUCE STREAM SAMPLE
-- JOIN COGROUP GROUP CROSS CUBE
-- ORDER RANK LIMIT
-- UNION SPLIT;