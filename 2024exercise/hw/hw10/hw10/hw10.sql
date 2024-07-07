CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT child FROM parents JOIN dogs ON parent = name   ORDER BY height DESC ;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM  dogs, sizes WHERE height > min AND height <= max;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child AS first,b.child AS second FROM parents as a,parents as b WHERE a.parent = b.parent AND a.child < b.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT 'The two siblings, ' || first || ' and ' || second ||', have the same size: ' || a.size FROM siblings , size_of_dogs AS a,size_of_dogs AS b WHERE a.name = first AND b.name = second AND a.size = b.size;



-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  -- SELECT result_fur,height_range FROM (SELECT fur AS result_fur, AVG(height) AS average_height, MAX(height) - MIN(height) AS height_range FROM dogs GROUP BY fur) AS subquery JOIN dogs ON dogs.fur = subquery.result_fur WHERE (SELECT COUNT(*) FROM  subquery,dogs WHERE NOT dogs.height >= 0.7 * subquery.average_height AND dogs.height <= subquery.average_height * 1.3) = 0;
    SELECT fur, MAX(height) - MIN(height) FROM dogs GROUP BY fur HAVING MIN(height) >= 0.7 * AVG(height) AND MAX(height) <= 1.3 * AVG(height);