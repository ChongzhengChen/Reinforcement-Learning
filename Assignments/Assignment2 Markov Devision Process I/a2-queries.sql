.echo on
--Question 1
select distinct m.name,m.email
from members As m, cars As c1,cars as c2
where  m.email  = c1.owner
and    c1.owner = c2.owner
and    c1.cno != c2.cno
intersect
select distinct m.name, m.email
from   members as m,cars as c, rides as r
where  m.email = c.owner
and    c.cno = r.cno;

--Question 2
select distinct m.name,m.email
from members as m, cars as c, bookings as b
where m.email = c.owner
And   m.email = b.email
except
select distinct m.name,m.email
from members as m, cars as c, rides as r
where m.email = c.owner  
and c.cno = r.cno

--Question 3
select distinct b.email
from  bookings as b,rides as r, locations
where b.rno = r.rno
and src in (select lcode from locations where city = "Edmonton")
and dst in (select lcode from locations where city = "Calgary")
and r.rdate <= "2018-11-30" and r.rdate >= "2018-11-01";

--Question 4

select distinct r1.rid, r1.email, r1.pickup, r1.dropoff,r2.rno
from requests as r1, rides as r2,locations as l1
where r1.rdate = r2.rdate
and r2.price <= r1.amount
intersect
select distinct r1.rid, r1.email, r1.pickup, r1.dropoff,r2.rno
from requests as r1, rides as r2,locations as l1, locations as l2
where r1.pickup = l1.lcode
and   r2.src    = l2.lcode
and   l1.city   = l2.city
intersect
select distinct r1.rid, r1.email, r1.pickup, r1.dropoff,r2.rno
from requests as r1, rides as r2,locations as l1, locations as l2
where r1.dropoff = l1.lcode
and   r2.dst    = l2.lcode
and   l1.city   = l2.city;

--Question 5
select city, prov
from rides as r, locations as l
where r.dst = l.lcode 
group by city,prov
order by count(city) desc
limit 3;

--Question 6
select city,prov,num_src, num_dst, num_lcode
from locations
left outer join 

select count(src) as num_src
from locations as l, rides as r
where r.src = l.lcode

left outer join

select count(dst) as num_dst
from locations as l, rides as r
where r.dst = l.lcode

left outer join

select count(lcode) as num_lcode
from enroute as e, locations as l 
where e.lcode = l.lcode
group by city using(city);

--Question 7
select r.rno
from rides as r, locations as l1, locations as l2, bookings as b
where l1.city = "Edmonton"
and   l1.lcode = r.src
and   l2.city = "Calgary"
and   l2.lcode = r.dst
and   b.seats <> r.seats
and   strftime('%Y-%m',rdate) = '2018-10'
order by r.price 
limit 1;



--Question 8







--Question 9
create view ride_info(rno,booked,available,rdate,price,src,dst)
As select r.rno,count(b.seats),count(r.seats-b.seats),r.rdate,price,r.src,r.dst 
from rides as r, bookings as b
where c.owner = r.driver



--Question 10

