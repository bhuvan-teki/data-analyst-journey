
# 📅 Day 01: SQL Foundations & DBMS Theory
**Date:** April 26, 2026  
**Track:** Data Analyst Journey (SQL Phase)

## 📝 Executive Summary
Today, I officially pivoted my learning strategy to prioritize **Database Management Systems (DBMS)** and **SQL**. After a gap in consistency, I am rebuilding my foundation by mastering how data is structured, stored, and retrieved before returning to Python automation.

---

## 🏛️ Part 1: DBMS & Data Theory
To effectively query data, I first mastered the ecosystem where it resides.

### 1. The 3 V's of Data
I evaluated the core characteristics of data that drive organizational decision-making:
* **Volume:** The massive scale of data generated and stored.
* **Velocity:** The speed at which data is generated and processed in real-time.
* **Variety:** Managing structured (tables), unstructured (images), and semi-structured (JSON) data.

### 2. Database Architectures
I researched 9 types of databases, focusing on how their structures impact performance:
* **Relational (RDBMS):** Data stored in tables linked by unique identities (Primary Keys).
* **NoSQL:** A non-relational mechanism for flexible, high-availability data storage.
* **Hierarchical/Network:** Legacy tree-like or web-like structures for specific ranked or many-to-many data.

---

## ⚙️ Part 2: Technical Fundamentals (SQLite)
I am using **SQLite** for its lightweight, zero-configuration efficiency.

### 1. Data Types & Integrity
I applied strict type definitions to ensure "Data Integrity" in my local environment:
* **TEXT:** For string-based data like Names.
* **INTEGER:** For whole numbers like Age and Records.
* **REAL:** For precise decimals like Height and Weight.

---

## 💻 Part 3: Practical Implementation
I successfully implemented Data Definition (DDL) and Data Manipulation (DML) using an MMA dataset.

### 1. Table Creation
```sql
CREATE TABLE MMA (
  Name TEXT,
  age INTEGER,
  record INTEGER,
  height REAL,
  weight REAL
);
```

### 2. Data Entry
```sql
INSERT INTO MMA (Name, age, record, height, weight) 
VALUES ('Conor McGregor', 35, 22, 1.75, 70.3);
```

### 3. Data Retrieval & Filtering
I practiced extracting specific insights using the `SELECT` statement and `WHERE` clause logic.
```sql
SELECT name, record
FROM MMA
WHERE age < 25;
```

---

## 🚀 Reflection
This restart is about building a "Proof of Work" portfolio that demonstrates both technical skill and strategic thinking. By documenting the theory alongside the code, I am proving my value as a Data Analyst who understands the full data lifecycle.

---

### **Next Goals:**
* [ ] Master the rest of CRUD: `UPDATE` and `DELETE`.
* [ ] Explore SQL Constraints (`PRIMARY KEY`, `NOT NULL`, `UNIQUE`).
* [ ] Practice Aggregate functions (`COUNT`, `SUM`, `AVG`).
```
