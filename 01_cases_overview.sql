CREATE OR REPLACE TABLE case_overview AS
WITH active_cases AS (
SELECT
     country
   , state
   , date_reported
   , case_type
   , case_cnt
   , SUM(case_cnt) OVER(PARTITION BY case_type ORDER BY date_reported) AS total_case_cnt
FROM media_markt.mm_schema.cases_cnt
WHERE UPPER(case_type) IN ('ACTIVE','RECOVERED')
AND UPPER(country) = 'GERMANY'
AND UPPER(STATE) = 'BAYERN'
)
SELECT
     country
   , state
   , date_reported
   , case_type
   , total_case_cnt
FROM
   active_cases
WHERE
   date_reported = LAST_DAY(date_reported);