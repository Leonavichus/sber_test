-- MySql
WITH RECURSIVE date_generator AS (
    SELECT 1 AS row_num,
        CURDATE() AS random_date
    UNION ALL
    SELECT row_num + 1,
        DATE_ADD(random_date, INTERVAL (ABS(RAND()) % 6 + 2) DAY)
    FROM date_generator
    WHERE row_num < 100
)
SELECT random_date
FROM date_generator;
-- SQL
WITH date_generator AS (
    SELECT 1 AS row_num,
        CAST(GETDATE() AS DATE) AS random_date
    UNION ALL
    SELECT row_num + 1,
        DATEADD(DAY, RAND() * 6 + 2, random_date)
    FROM date_generator
    WHERE row_num < 100
)
SELECT random_date
FROM date_generator;