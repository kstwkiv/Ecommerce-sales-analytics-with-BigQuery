SELECT
  c.name AS customer_name,
  SUM(f.total_amount) AS lifetime_value
FROM ecommerce_sales.fact_orders f
JOIN ecommerce_sales.dim_customers c
  ON f.customer_id = c.customer_id
GROUP BY c.name
ORDER BY lifetime_value DESC
LIMIT 20;
