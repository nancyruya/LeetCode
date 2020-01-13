Select id, movie, description, rating From cinema Where (id % 2 = 1) and description != 'boring' order by rating DESC
