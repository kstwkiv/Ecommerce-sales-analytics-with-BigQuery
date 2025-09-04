SELECT
  EXTRACT(YEAR FROM order_date) AS year,
  EXTRACT(MONTH FROM order_date) AS month,
  SUM(total_amount) AS monthly_revenue
FROM ecommerce_sales.fact_orders
GROUP BY year, month
ORDER BY year, month;
