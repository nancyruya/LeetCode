Select distinct(tb1.Num) As ConsecutiveNums
From Logs as tb1, Logs as tb2, Logs as tb3
Where tb1.Id + 1 = tb2.Id And tb2.Id + 1 = tb3.Id And tb1.Num = tb2.Num And tb2.Num = tb3.Num;
