SELECT
  p.product_name,
  SUM(f.total_amount) AS revenue
FROM ecommerce_sales.fact_orders f
JOIN ecommerce_sales.dim_products p
  ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 10;
