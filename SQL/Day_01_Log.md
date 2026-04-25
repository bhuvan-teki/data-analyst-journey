# 📅 Day 01: SQL Foundations & DBMS Theory
**Date:** April 26, 2026  
**Track:** Data Analyst Journey (SQL Phase)

## 📝 Executive Summary
Today, I officially restarted my Data Analyst journey with a "Data-First" strategy. After a 2-month gap, I realized that mastering **Database Management Systems (DBMS)** is the essential foundation before moving into complex Python automation. Today’s session covered the 3 V’s of data, the 9 types of database architectures, and core SQLite syntax.

---

## 🏛️ Part 1: DBMS & Data Theory
To understand how to query data, I first studied the environment where data lives.

### 1. The 3 V's of Data
I evaluated the characteristics that determine which database a company chooses:
* **Volume:** The massive scale of data being stored and processed.
* **Velocity:** The speed at which data is generated and analyzed in real-time.
* **Variety:** Managing structured (tables), semi-structured (JSON), and unstructured (images/text) data.

### 2. Database Models & Architectures
I researched 9 different database types to understand their specific use cases:
* **Relational (RDBMS):** Organized into tables linked by Primary and Foreign Keys (Current Focus).
* **Hierarchical:** A tree-like structure where each child has only one parent.
* **Network:** A web-like model allowing many-to-many relationships.
* **NoSQL:** Non-tabular structures ideal for unstructured data and horizontal scalability.
* **Cloud & Personal:** Specialized environments like AWS/GCP for scale, or SQLite for local development.

---

## ⚙️ Part 2: Technical Fundamentals (SQLite)
I have selected **SQLite** as my primary tool for this phase because it is a zero-configuration, lightweight RDBMS ideal for local data analysis.

### 1. Data Types & Integrity
I am focusing on assigning the correct data types to ensure "Data Integrity":
* **TEXT:** For string data (names, categories).
* **INTEGER:** For whole numbers (IDs, ages, wins).
* **REAL:** For floating-point decimals (height, weight, financial values).

### 2. Constraints (Security Rules)
* **PRIMARY KEY:** Ensures every record is unique and identifiable.
* **NOT NULL:** Prevents critical data from being left blank.
* **UNIQUE:** Stops duplicate entries in specific columns.

---

## 💻 Part 3: SQL Syntax Mastery (CRUD)
I practiced the four fundamental operations that power all modern data applications:

| Operation | SQL Command | Purpose |
| :--- | :--- | :--- |
| **CREATE** | `CREATE TABLE` | Building the structured "skeleton" of the data. |
| **INSERT** | `INSERT INTO` | Populating the table with "cargo" (values). |
| **READ** | `SELECT` | Retrieving and displaying data. |
| **FILTER** | `WHERE` | Slicing data based on specific conditions. |

---

## 🚀 Reflection
By documenting the "Why" behind my pivot and the "How" behind my code, I am building a transparent **Proof of Work** portfolio. Today wasn't just about learning syntax; it was about understanding the data ecosystem that I will eventually manage as a professional analyst.

---

### **Next Steps:**
* [ ] Create a practical `.sql` script implementing an `MMA_CONTENDERS` table.
* [ ] Practice complex `WHERE` clause filters (Relational Operators).
* [ ] Explore Aggregate functions (`COUNT`, `SUM`, `AVG`).
