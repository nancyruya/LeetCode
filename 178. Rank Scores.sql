Select tb1.Score AS Score, (Select count(distinct tb2.Score)
                            From Scores AS tb2
                            WHERE tb2.Score > tb1.Score) + 1 AS Rank
From Scores As tb1
Order by tb1.Score DESC;
