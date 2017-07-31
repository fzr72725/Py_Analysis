-- Ziru Fan
-- ziru.z.fan@gmail.com

select sp.Name
from Salesperson sp
join Orders o
on o.salesperson_id = sp.id
group by o.salesperson_id 
having count(*) > 1;