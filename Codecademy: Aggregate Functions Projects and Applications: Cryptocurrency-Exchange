SELECT COUNT(money_in)
FROM transactions;

SELECT SUM(money_in)
FROM transactions;

SELECT COUNT(money_in)
FROM transactions;

SELECT COUNT(money_in)
FROM transactions
WHERE currency = "BIT";

SELECT MAX(money_in), MAX(money_out)
FROM transactions;
-- So money_out has the largest recorded transaction with a total of 15047.00 USD
SELECT 
  date, 
  avg(money_in), 
  avg(money_out)
FROM transactions
GROUP BY date;

SELECT 
  date, 
  ROUND(AVG(money_in), 2) AS 'average money out', 
  ROUND(AVG(money_out),2) AS 'average money in'
FROM transactions
GROUP BY date;
