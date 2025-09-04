SELECT
  p.category,
  SUM(f.total_amount) AS revenue
FROM ecommerce_sales.fact_orders f
JOIN ecommerce_sales.dim_products p
  ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;
