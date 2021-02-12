CREATE OR REPLACE TABLE death_distribution_by_age AS
WITH age_details AS (
SELECT
     country
   , state
   , date_reported
   , age
   , CASE
      WHEN age >= 0  AND age < 13 THEN 'KIDS'
      WHEN age >= 13 AND age < 20 THEN 'TEENS'
      WHEN age >= 20 AND age < 35 THEN 'YOUNG'
      WHEN age >= 35 AND age < 55 THEN 'MIDDLE'
      WHEN age >= 55 THEN 'ELDERLY'
   END AS age_grp
FROM media_markt.mm_schema.deaths_data
WHERE UPPER(country) = 'GERMANY'
  AND UPPER(STATE) = 'BAYERN'
)
, cnt_by_age_grp AS (
  SELECT date_reported
   , age_grp
   , COUNT(age_grp) AS death_cnt
FROM age_details
GROUP BY date_reported
   , age_grp
ORDER BY date_reported
   , age_grp
)
SELECT date_reported
   , age_grp
   , death_cnt
   , SUM(death_cnt) OVER(PARTITION BY age_grp ORDER BY date_reported) AS cum_death_cnt
FROM cnt_by_age_grp
