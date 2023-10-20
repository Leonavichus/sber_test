WITH sales_summary AS (
    SELECT e.id AS e_id,
        e.name AS e_name,
        COUNT(s.id) AS sales_c,
        RANK() OVER (
            ORDER BY COUNT(s.id) DESC
        ) AS sales_rank_c,
        SUM(s.price) AS sales_s,
        RANK() OVER (
            ORDER BY SUM(s.price) DESC
        ) AS sales_rank_s
    FROM employee e
        LEFT JOIN sales s ON e.id = s.employee_id
    GROUP BY e.id,
        e.name
)
SELECT e_id,
    e_name,
    sales_c,
    sales_rank_c,
    sales_s,
    sales_rank_s
FROM sales_summary;