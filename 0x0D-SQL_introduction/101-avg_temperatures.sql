-- hbtn_0c_0 database this table dump
SELECT city, AVG(values) AS avg_temp FROM tempratures GROUP BY city ORDER BY avg_temp DESC;
