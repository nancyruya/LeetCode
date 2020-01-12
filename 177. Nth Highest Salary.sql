CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    set N=N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT distinct Salary From employee ORDER BY Salary desc limit N, 1
  );
END
