Select tb2.Name as Department, tb1.Name as Employee, tb1.Salary as Salary
From Employee as tb1
Inner Join Department as tb2
On tb1.DepartmentId = tb2.Id
Where (Select count(DISTINCT Salary)
       From Employee as tb3
       Where tb3.DepartmentId = tb1.DepartmentId and tb3.Salary > tb1.Salary) < 3;
