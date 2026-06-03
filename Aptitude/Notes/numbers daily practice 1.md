# Quantitative Aptitude - Daily Practice Set 1: Number Systems

This document contains a structured log of my daily problem-solving practice, focusing on Number Systems, Divisibility Rules, Prime Numbers, and Algebraic logic.

---

### 📝 Question 1: Find `n` if `(-1)^n + (-1)^(16n) = 0`
* **Options:**
  * A) Any odd natural number
  * B) Any even natural number
  * C) Any integer
  * D) None of these

> **✅ Answer:** Any odd natural number
>
> **🧮 Step-by-Step Calculation:**
> **Step 1:** Analyze the second term, `(-1)^(16n)`.
> * Since `n` is a natural number, `16n` will always result in an **even** number.
> * Any negative base raised to an even power becomes positive: `(-1)^(even) = 1`.
> 
> **Step 2:** Substitute this back into the original equation.
> * `(-1)^n + 1 = 0`
> * `(-1)^n = -1`
> 
> **Step 3:** Determine `n`.
> * A negative base raised to a power results in a negative number *only* if the power is **odd**.
> * Therefore, `n` must be an odd natural number.

---

### 📝 Question 2: When 89122 is divided by 4, what is the remainder?
* **Options:**
  * A) 1
  * B) 2
  * C) 3
  * D) 5

> **✅ Answer:** 2
>
> **🧮 Step-by-Step Calculation:**
> **Step 1:** Apply the divisibility rule for 4 (only the last two digits matter).
> * Target digits = `22`.
> 
> **Step 2:** Perform the division.
> * `22 ÷ 4 = 5` with a remainder of `2`.
> 
> **Conclusion:** The entire number 89122 will leave a remainder of 2 when divided by 4.

---

### 📝 Question 3: Find `C` and `D` if `C409530D` is divisible by 12 and 10. (C and D are single-digit numbers, C ≠ 0, and C should be the least possible number).
* **Options:**
  * A) 3, 0
  * B) 4, 0
  * C) 5, 0
  * D) 6, 0

> **✅ Answer:** 3, 0
>
> **🧮 Step-by-Step Calculation:**
> **Step 1:** Apply the divisibility rule for 10.
> * A number is divisible by 10 only if its last digit is 0. 
> * Therefore, **`D = 0`**. The number is now `C4095300`.
> 
> **Step 2:** Apply the divisibility rule for 12 (must be divisible by both 3 and 4).
> * **Check 4:** The last two digits are `00`. Zero is divisible by 4, so this condition is met.
> * **Check 3:** The sum of all digits must be a multiple of 3.
>   * `Sum = C + 4 + 0 + 9 + 5 + 3 + 0 + 0 = C + 21`
> 
> **Step 3:** Test options to find the *least* valid value for `C`.
> * If `C = 3` ➔ `3 + 21 = 24` (24 is divisible by 3) ✅
> * If `C = 4` ➔ `4 + 21 = 25` (Not divisible by 3) ❌
> 
> **Conclusion:** The least valid value is `C = 3`, making the pair `3, 0`.

---

### 📝 Question 4: A proper fraction value will be:
* **Options:**
  * A) Is equal to 0
  * B) Greater than 1
  * C) Lies between 0 to 1
  * D) Can't be determined

> **✅ Answer:** Lies between 0 to 1
>
> **🧮 Logic:**
> * **Definition:** A proper fraction is a fraction where the Numerator is strictly less than the Denominator (`N < D`).
> * **Calculation:** Because you are dividing a smaller number by a larger number (e.g., `2 ÷ 5 = 0.4`), the quotient will always be greater than 0 but less than 1.

---

### 📝 Question 5: A person got twice as many sums wrong as he got right. If he attempted 48 sums in all, how many did he solve correctly?
* **Options:**
  * A) 12
  * B) 24
  * C) 16
  * D) 21

> **✅ Answer:** 16
>
> **🧮 Step-by-Step Calculation:**
> **Step 1:** Define variables.
> * Let the number of correct sums = `x`
> * Let the number of wrong sums = `2x` (twice as many)
> 
> **Step 2:** Set up the equation based on total attempts.
> * `Correct + Wrong = Total Attempted`
> * `x + 2x = 48`
> 
> **Step 3:** Solve for `x`.
> * `3x = 48`
> * `x = 48 / 3`
> * **`x = 16`**

---

### 📝 Question 6: How many prime numbers are less than 40?
* **Options:**
  * A) 10
  * B) 11
  * C) 12
  * D) 13

> **✅ Answer:** 12
>
> **🧮 Step-by-Step Calculation:**
> **Step 1:** List all prime numbers (numbers divisible only by 1 and themselves) up to 40.
> * Range: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37.
> 
> **Step 2:** Count the sequence.
> * Total count = 12 prime numbers.

---

### 📝 Question 7: Calculate `i^14`.
* **Options:**
  * A) 1
  * B) 0
  * C) -1
  * D) None

> **✅ Answer:** -1
>
> **🧮 Step-by-Step Calculation:**
> **Step 1:** Identify the cyclical nature of imaginary numbers (`i`).
> * `i^1 = i`
> * `i^2 = -1`
> * `i^3 = -i`
> * `i^4 = 1` (The cycle repeats every 4 powers).
> 
> **Step 2:** Divide the given power by 4 to find the remainder.
> * `14 ÷ 4 = 3` with a **remainder of 2**.
> 
> **Step 3:** Map the remainder to the cycle.
> * `i^14` is equivalent to `i^2`.
> * Since `i^2 = -1`, the answer is -1.

---

### 📝 Question 8: Identify a non-prime number among the following.
* **Options:**
  * A) 19
  * B) 29
  * C) 121
  * D) 151

> **✅ Answer:** 121
>
> **🧮 Step-by-Step Calculation:**
> * **Test A (19):** Divisible only by 1, 19 (Prime)
> * **Test B (29):** Divisible only by 1, 29 (Prime)
> * **Test C (121):** `11 × 11 = 121`. Because it has factors other than 1 and itself, it is a composite (non-prime) number.

---

### 📝 Question 9: The number of employees in SoftSolutions is less than 300 and a prime number. What is the possible ratio of male to female employees?
* **Options:**
  * A) 61 : 58
  * B) 45 : 40
  * C) 100 : 99
  * D) 73 : 50

> **✅ Answer:** 100 : 99
>
> **🧮 Step-by-Step Calculation:**
> **Logic:** The total number of employees is the sum of the ratio units. We must find the sum that results in a prime number.
> * Option A: `61 + 58 = 119` ➔ Divisible by 7 (`7 × 17`) ❌
> * Option B: `45 + 40 = 85` ➔ Divisible by 5 (`5 × 17`) ❌
> * Option C: `100 + 99 = 199` ➔ Only divisible by 1 and 199 (**Prime**) ✅
> * Option D: `73 + 50 = 123` ➔ Divisible by 3 (`3 × 41`) ❌

---

### 📝 Question 10: If 72 exactly divides `42573x`, what is the smallest value for `x`?
* **Options:**
  * A) 6
  * B) 7
  * C) 8
  * D) 2

> **✅ Answer:** 6
>
> **🧮 Step-by-Step Calculation:**
> **Step 1:** Break down 72 into co-prime factors.
> * `72 = 8 × 9`. The number must pass divisibility rules for both 8 and 9.
> 
> **Step 2:** Test for 8 (Last three digits `73x` must be divisible by 8).
> * Let's test the options for `x`:
>   * If `x = 6` ➔ `736 ÷ 8 = 92` (Exact division) ✅
> 
> **Step 3:** Verify with the rule for 9 (Sum of digits must be a multiple of 9).
> * Insert `x = 6`: `425736`
> * `Sum = 4 + 2 + 5 + 7 + 3 + 6 = 27`.
> * `27 ÷ 9 = 3` (Exact division) ✅

---

### 📝 Question 11: When 4560 is divided by 8, what is the remainder?
* **Options:**
  * A) 0
  * B) 1
  * C) 2
  * D) 3

> **✅ Answer:** 0
>
> **🧮 Step-by-Step Calculation:**
> **Step 1:** Apply the divisibility rule for 8 (check the last 3 digits).
> * Target digits = `560`
> 
> **Step 2:** Divide by 8.
> * `560 ÷ 8 = 70` exactly, with a remainder of `0`.

---

### 📝 Question 12: Which of the following is divisible by 4?
* **Options:**
  * A) 4646652
  * B) 47554
  * C) 466654
  * D) 499774

> **✅ Answer:** 4646652
>
> **🧮 Step-by-Step Calculation:**
> **Logic:** Apply the divisibility rule for 4 (check the last 2 digits of each option).
> * A) `...52` ➔ `52 ÷ 4 = 13` (Divisible) ✅
> * B) `...54` ➔ `54 ÷ 4 = 13.5` (Not Divisible) ❌
> * C) `...54` ➔ `54 ÷ 4 = 13.5` (Not Divisible) ❌
> * D) `...74` ➔ `74 ÷ 4 = 18.5` (Not Divisible) ❌

---

### 📝 Question 13: Which number is divisible by 3?
* **Options:**
  * A) 1235
  * B) 1237
  * C) 1239
  * D) 1241

> **✅ Answer:** 1239
>
> **🧮 Step-by-Step Calculation:**
> **Logic:** Apply the divisibility rule for 3 (Sum of digits must be a multiple of 3).
> * A) 1235 ➔ `1 + 2 + 3 + 5 = 11` (Not Divisible)
> * B) 1237 ➔ `1 + 2 + 3 + 7 = 13` (Not Divisible)
> * C) 1239 ➔ `1 + 2 + 3 + 9 = 15` ➔ `15 ÷ 3 = 5` (**Divisible**) ✅
> * D) 1241 ➔ `1 + 2 + 4 + 1 = 8` (Not Divisible)

---

### 📝 Question 14: What is the rational form of 3.66666666...?
* **Options:**
  * A) 2/3
  * B) 11/3
  * C) 2/7
  * D) 1/9

> **✅ Answer:** 11/3
>
> **🧮 Step-by-Step Calculation:**
> **Step 1:** Separate the whole number from the repeating decimal.
> * `3.6666... = 3 + 0.6666...`
> 
> **Step 2:** Convert the repeating decimal to a fraction.
> * Standard repeating rule: `0.666... = 6/9 = 2/3`.
> 
> **Step 3:** Add the whole number and the fraction.
> * `3 + 2/3`
> * Convert to common denominator: `9/3 + 2/3 = 11/3`.

---

### 📝 Question 15: What is the smallest value that can replace `*` in `197*5462` to make it divisible by 9?
* **Options:**
  * A) 9
  * B) 2
  * C) 4
  * D) 1

> **✅ Answer:** 2
>
> **🧮 Step-by-Step Calculation:**
> **Step 1:** Apply the divisibility rule for 9 (sum of digits).
> * `Sum = 1 + 9 + 7 + * + 5 + 4 + 6 + 2`
> * `Sum = 34 + *`
> 
> **Step 2:** Find the nearest multiple of 9 that is greater than or equal to 34.
> * Multiples of 9: 9, 18, 27, **36**, 45.
> 
> **Step 3:** Solve for `*`.
> * `34 + * = 36`
> * `* = 36 - 34 = 2`

---

### 📝 Question 16: What is the commonly used form of a complex number?
* **Options:**
  * A) u + iv
  * B) v - u
  * C) u + v
  * D) i(u + v)

> **✅ Answer:** u + iv
>
> **🧮 Logic:**
> * A complex number consists of a real part and an imaginary part.
> * The standard algebraic notation is `a + ib` (where `a` is real and `b` is imaginary).
> * Substituting variables `a` and `b` with `u` and `v`, the correct formatting is **`u + iv`**.

---

### 📝 Question 17: A number divisible by 60 is also divisible by which number?
* **Options:**
  * A) 7
  * B) 11
  * C) 12
  * D) 13

> **✅ Answer:** 12
>
> **🧮 Step-by-Step Calculation:**
> **Logic:** If `X` is divisible by `Y`, then `X` is also divisible by all the *factors* of `Y`.
> * Let's find the factors of 60: 1, 2, 3, 4, 5, 6, 10, **12**, 15, 20, 30, 60.
> * Looking at the options (7, 11, 12, 13), only **12** is a valid factor of 60.

---

### 📝 Question 18: Which of the following numbers remains prime even after inversion?
* **Options:**
  * A) 31
  * B) 41
  * C) 51
  * D) None

> **✅ Answer:** 31
>
> **🧮 Step-by-Step Calculation:**
> **Logic:** Invert (reverse the digits) of each option and test for primality.
> * Option A: `31` reversed is `13`. (Both 31 and 13 are prime). ✅
> * Option B: `41` reversed is `14`. (14 is even, divisible by 2). ❌
> * Option C: `51`. (Not prime to begin with, `17 × 3 = 51`). ❌

---

### 📝 Question 19: The difference between 3 times and 7 times of a number is 36. What is that number?
* **Options:**
  * A) 9
  * B) 10
  * C) 8
  * D) 6

> **✅ Answer:** 9
>
> **🧮 Step-by-Step Calculation:**
> **Step 1:** Translate the word problem into an algebraic equation. Let the number be `x`.
> * `7x - 3x = 36`
> 
> **Step 2:** Solve for `x`.
> * `4x = 36`
> * `x = 36 / 4`
> * **`x = 9`**

---

### 📝 Question 20: The difference between the local value and the face value of 7 in the numeral 25974264 is:
* **Options:**
  * A) 5149
  * B) 69993
  * C) 64851
  * D) None of these

> **✅ Answer:** 69993
>
> **🧮 Step-by-Step Calculation:**
> **Step 1:** Identify the Local Value (Place Value).
> * In `25974264`, the `7` is in the ten-thousands place.
> * Local Value = `70,000`.
> 
> **Step 2:** Identify the Face Value.
> * The face value of a digit is just the digit itself.
> * Face Value = `7`.
> 
> **Step 3:** Calculate the difference.
> * `70,000 - 7 = 69,993`.

---

### 📝 Question 21: Smallest whole number for `x` if `8x04752` is divisible by 11?
* **Options:**
  * A) 2
  * B) 4
  * C) 6
  * D) 8

> **✅ Answer:** 8
>
> **🧮 Step-by-Step Calculation:**
> **Step 1:** Apply the divisibility rule for 11. Find the sum of digits in odd and even places.
> * Odd places (1st, 3rd, 5th, 7th): `8 + 0 + 7 + 2 = 17`.
> * Even places (2nd, 4th, 6th): `x + 4 + 5 = x + 9`.
> 
> **Step 2:** Subtract the smaller sum from the larger sum.
> * `Difference = 17 - (x + 9) = 8 - x`.
> 
> **Step 3:** For divisibility by 11, the difference must be `0` or a multiple of `11`.
> * Set to 0: `8 - x = 0` ➔ `x = 8`.

---

### 📝 Question 22: Which of the following numbers is divisible by 30?
* **Options:**
  * A) 9030
  * B) 9040
  * C) 9050
  * D) 9065

> **✅ Answer:** 9030
>
> **🧮 Step-by-Step Calculation:**
> **Step 1:** Break 30 into co-prime factors (`30 = 3 × 10`). The number must be divisible by 3 and 10.
> **Step 2:** Check for divisibility by 10 (must end in 0).
> * Eliminates D (9065). Remaining: A, B, C.
> 
> **Step 3:** Check for divisibility by 3 (sum of digits).
> * A) 9030 ➔ `9+0+3+0 = 12` (Divisible by 3) ✅
> * B) 9040 ➔ `9+0+4+0 = 13` (Not Divisible) ❌
> * C) 9050 ➔ `9+0+5+0 = 14` (Not Divisible) ❌

---

### 📝 Question 23: Replace `*` with the smallest number so that `817*67` is divisible by 11.
* **Options:**
  * A) 2
  * B) 3
  * C) 1
  * D) 5

> **✅ Answer:** 2
>
> **🧮 Step-by-Step Calculation:**
> **Step 1:** Apply the divisibility rule for 11.
> * Sum of odd places: `8 + 7 + 6 = 21`
> * Sum of even places: `1 + * + 7 = 8 + *`
> 
> **Step 2:** Find the difference.
> * `Difference = 21 - (8 + *) = 13 - *`
> 
> **Step 3:** Set the difference to a multiple of 11 (like 0, 11, 22).
> * Since `*` must be a positive single digit, `13 - *` cannot be 0 (as `*` would be 13).
> * Set difference to 11: `13 - * = 11` ➔ `* = 2`.

---

## 🎯 Purpose

These notes are part of my **Data Analyst Journey** repository where I document my learning progress, aptitude preparation, and problem-solving practice.

## 👨‍💻 Repository Owner

**Bhuvan Teki**

* **GitHub:** https://github.com/bhuvan-teki/
* **LinkedIn:** https://www.linkedin.com/in/bhuvanteki/

## 🚀 Goal

Become skilled in:
- Quantitative Aptitude
- Logical Reasoning
- Data Analytics
- Problem Solving

through consistent practice, continuous learning, and logical application.
