# Задание 1
SELECT c.login, COUNT(o.id)
FROM "Couriers" as c 
LEFT JOIN "Orders" as o ON c.id = o."courierId" AND o."inDelivery" = true
GROUP BY c.login;

# Задание 2
SELECT o.track,
    CASE
        WHEN o.finished = true THEN 2
        WHEN o.cancelled = true THEN -1
        WHEN o."inDelivery" = true THEN 1
        ELSE 0
        END AS status
FROM "Orders";