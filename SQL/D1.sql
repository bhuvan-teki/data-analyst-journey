-- =====================================
-- Day 1 - Types of DBMS
-- =====================================

-- Hierarchical DBMS
GET /employees/123/projects/456

-- Network DBMS
FIND owner OF project 456

-- Relational DBMS (RDBMS)
SELECT * FROM employees
WHERE salary > 50000;

-- NoSQL DBMS (MongoDB)
db.inventory.find({ status: "A" })

-- Object Oriented DBMS (ODBMS)
SELECT e.name
FROM employees e
WHERE e.age > 30;

-- Graph Database
g.V().has('name', 'Alice').out('knows').values('name')

-- Document Database
db.collection.find({ field: "value" })