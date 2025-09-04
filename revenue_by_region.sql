SELECT
  region,
  SUM(total_amount) AS revenue
FROM ecommerce_sales.fact_orders
GROUP BY region
ORDER BY revenue DESC;
