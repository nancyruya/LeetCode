Select (Case When mod(id, 2) = 1 AND id = counts Then id
             When mod(id, 2) = 1 AND id != counts Then id + 1
             Else id - 1
        End) As id, student
From seat, (Select count(*) as counts From seat) As counts
Order by id
