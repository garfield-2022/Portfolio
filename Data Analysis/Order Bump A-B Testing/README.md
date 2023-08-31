This project was from the course Product Case Interview Pro by Data Interview Pro (Emma Ding).

An e-commerce startup wants to know if order bump could increase the revenue in product sales by getting customers to add more items to their cart before they check out. To test if this is a good idea, an A/B test is run. Customers are split into both control (c) and treatment (t) variants. In the treatment variant, customers are nudged to add more items to their cart by the order bump whereas in the control variant, customers check out whatever they add to the cart without being prompted to add more. 

The success metric is selected to be average revenue per customer, for that it tracks the goal of the prodcut and company, can be more easily measured within the experiment duration, than, say churn and retention, and has a variance lower than total revenues. 

The experiment data are stored in 3 separate CSV files:
  1. Transaction data before the experiment: transactions_pre.csv,
      a. customer_id (data type: integer): unique identifier of each customer,
      b. transaction_date (data type: datetime): the date on which the transaction happened,
      c. amount_usd (data type: float): the US dollar amount paid by the customer in the transaction,
  2. Transaction data after the experiment: transactions_post.csv (same structure as the pre-test data),
  3. Metadata on experiment assignments: assignment.csv,
      a. customer_id (data type: integer): unique identifier of each customer,
      b. variant (data type: string): whether the customer was assigned to the experiment or the control variant.

I adopted most of their solutions. I did a test. Keeping outliers will not change conclusions but reduces the variance of the metric.     

Compared to control, the treatment improved significantly more in terms of average revenue per customer. So a launch decision is suggested.
