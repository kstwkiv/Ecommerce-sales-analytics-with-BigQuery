SELECT
  EXTRACT(YEAR FROM order_date) AS year,
  EXTRACT(MONTH FROM order_date) AS month,
  SUM(total_amount) / COUNT(DISTINCT order_id) AS avg_order_value
FROM ecommerce_sales.fact_orders
GROUP BY year, month
ORDER BY year, month;
