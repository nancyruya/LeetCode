Select id,
sum(Case when month = 'Jan' then revenue else null end) as Jan_Revenue,
sum(Case when month = 'Feb' then revenue else null end) as Feb_Revenue,
sum(Case when month = 'Mar' then revenue else null end) as Mar_Revenue,
sum(Case when month = 'Apr' then revenue else null end) as Apr_Revenue,
sum(Case when month = 'May' then revenue else null end) as May_Revenue,
sum(Case when month = 'Jun' then revenue else null end) as Jun_Revenue,
sum(Case when month = 'Jul' then revenue else null end) as Jul_Revenue,
sum(Case when month = 'Aug' then revenue else null end) as Aug_Revenue,
sum(Case when month = 'Sep' then revenue else null end) as Sep_Revenue,
sum(Case when month = 'Oct' then revenue else null end) as Oct_Revenue,
sum(Case when month = 'Nov' then revenue else null end) as Nov_Revenue,
sum(Case when month = 'Dec' then revenue else null end) as Dec_Revenue
From Department
Group by id
Order by id
