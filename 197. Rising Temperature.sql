Select tb1.id
From Weather as tb1
Inner Join Weather as tb2
On tb1.Temperature > tb2.Temperature AND DATEDIFF(tb1.RecordDate, tb2.RecordDate) = 1
Where tb1.RecordDate > tb2.RecordDate
