Update salary
Set sex = (Case when sex = 'm'
          Then 'f'
          when sex = 'f'
          Then 'm'
          end)
