Select tb2.Name as Department, tb1.Name as Employee, tb1.Salary as Salary
From Employee as tb1
Left Join Department as tb2
On tb1.DepartmentId = tb2.Id
Where (tb2.Id, tb1.Salary) In (Select DepartmentId, max(Salary)
                               From Employee
                               Group by DepartmentId);
