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
> **🔍 Explanation:**
> Since `16n` is always an even number, `(-1)^(16n) = 1`.
> Substituting this into the equation: `(-1)^n + 1 = 0` ➔ `(-1)^n = -1`.
> This condition is satisfied only when `n` is an odd number. Therefore, `n` can be any odd natural number.

---

### 📝 Question 2: When 89122 is divided by 4, what is the remainder?
* **Options:**
  * A) 1
  * B) 2
  * C) 3
  * D) 5

> **✅ Answer:** 2
>
> **🔍 Explanation:**
> According to the divisibility rule for 4, we only need to check the last two digits.
> The last two digits are `22`. 
> `22 ÷ 4 = 5` with a remainder of `2`. 
> Therefore, 89122 gives a remainder of 2 when divided by 4.

---

### 📝 Question 3: Find `C` and `D` if `C409530D` is divisible by 12 and 10. (C and D are single-digit numbers, C ≠ 0, and C should be the least possible number).
* **Options:**
  * A) 3, 0
  * B) 4, 0
  * C) 5, 0
  * D) 6, 0

> **✅ Answer:** 3, 0
>
> **🔍 Explanation:**
> * **Divisibility by 10:** The last digit must be 0. So, `D = 0`. The number becomes `C4095300`.
> * **Divisibility by 12:** The number must be divisible by both 3 and 4.
>   * *Check 4:* The last two digits are `00`, which is divisible by 4.
>   * *Check 3:* The sum of the digits must be a multiple of 3.
>     Sum = `C + 4 + 0 + 9 + 5 + 3 + 0 + 0 = C + 21`
> Let's test the options for the least value of C:
> * `C = 3` ➔ 3 + 21 = 24 (Divisible by 3)
> * `C = 4` ➔ 4 + 21 = 25 (Not divisible)
> 
> The least valid value is `C = 3`. Therefore, C = 3, D = 0.

---

### 📝 Question 4: A proper fraction value will be:
* **Options:**
  * A) Is equal to 0
  * B) Greater than 1
  * C) Lies between 0 to 1
  * D) Can't be determined

> **✅ Answer:** Lies between 0 to 1
>
> **🔍 Explanation:**
> By definition, a proper fraction is one where the numerator is strictly less than the denominator (e.g., `2/5 = 0.4`). Because the numerator is smaller, the overall value will always be greater than 0 but strictly less than 1.

---

### 📝 Question 5: A person got twice as many sums wrong as he got right. If he attempted 48 sums in all, how many did he solve correctly?
* **Options:**
  * A) 12
  * B) 24
  * C) 16
  * D) 21

> **✅ Answer:** 16
>
> **🔍 Explanation:**
> Let the number of correct answers = `x`.
> The number of wrong answers = `2x`.
> Total attempted = 48.
> `x + 2x = 48`
> `3x = 48` ➔ `x = 16`. 
> He solved 16 sums correctly.

---

### 📝 Question 6: How many prime numbers are less than 40?
* **Options:**
  * A) 10
  * B) 11
  * C) 12
  * D) 13

> **✅ Answer:** 12
>
> **🔍 Explanation:**
> The prime numbers less than 40 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37.
> Counting them up gives a total of 12 prime numbers.

---

### 📝 Question 7: Calculate `i^14`.
* **Options:**
  * A) 1
  * B) 0
  * C) -1
  * D) None

> **✅ Answer:** -1
>
> **🔍 Explanation:**
> The powers of `i` repeat in cycles of 4:
> `i^1 = i`, `i^2 = -1`, `i^3 = -i`, `i^4 = 1`.
> Divide the power by 4 to find the position in the cycle: `14 ÷ 4 = 3` with a remainder of `2`.
> Therefore, `i^14 = i^2`. Since `i^2 = -1`, the answer is -1.

---

### 📝 Question 8: Identify a non-prime number among the following.
* **Options:**
  * A) 19
  * B) 29
  * C) 121
  * D) 151

> **✅ Answer:** 121
>
> **🔍 Explanation:**
> A prime number has only two factors: 1 and itself. 
> 121 can be factored as `11 × 11`. Because it has factors other than 1 and itself, 121 is a composite (non-prime) number.

---

### 📝 Question 9: The number of employees in SoftSolutions is less than 300 and a prime number. What is the possible ratio of male to female employees?
* **Options:**
  * A) 61 : 58
  * B) 45 : 40
  * C) 100 : 99
  * D) 73 : 50

> **✅ Answer:** 100 : 99
>
> **🔍 Explanation:**
> The total number of employees is the sum of the ratio components. We need to find the sum that results in a prime number less than 300.
> * A) 61 + 58 = 119 (`7 × 17` - Not prime)
> * B) 45 + 40 = 85 (`5 × 17` - Not prime)
> * C) 100 + 99 = 199 (**Prime number**)
> * D) 73 + 50 = 123 (`3 × 41` - Not prime)
> 
> Therefore, 100:99 is the only possible ratio.

---

### 📝 Question 10: If 72 exactly divides `42573x`, what is the smallest value for `x`?
* **Options:**
  * A) 6
  * B) 7
  * C) 8
  * D) 2

> **✅ Answer:** 6
>
> **🔍 Explanation:**
> For a number to be divisible by 72, it must be divisible by both 8 and 9 (since `8 × 9 = 72` and they are co-prime).
> * **Divisibility by 8:** The last three digits (`73x`) must be divisible by 8. Let's test the options: `736 ÷ 8 = 92` (Divides exactly). `x = 6` works.
> * **Divisibility by 9:** The sum of all digits must be divisible by 9. 
>   `4 + 2 + 5 + 7 + 3 + 6 = 27`, which is divisible by 9.
> Therefore, `x = 6`.

---

### 📝 Question 11: When 4560 is divided by 8, what is the remainder?
* **Options:**
  * A) 0
  * B) 1
  * C) 2
  * D) 3

> **✅ Answer:** 0
>
> **🔍 Explanation:**
> According to the divisibility rule for 8, check the last three digits (`560`).
> `560 ÷ 8 = 70` with a remainder of 0. 
> Therefore, 4560 is perfectly divisible by 8, leaving a remainder of 0.

---

### 📝 Question 12: Which of the following is divisible by 4?
* **Options:**
  * A) 4646652
  * B) 47554
  * C) 466654
  * D) 499774

> **✅ Answer:** 4646652
>
> **🔍 Explanation:**
> A number is divisible by 4 if its last two digits are divisible by 4.
> * A) Ends in `52` ➔ `52 ÷ 4 = 13` (**Divisible**)
> * B) Ends in `54` ➔ Not divisible by 4
> * C) Ends in `54` ➔ Not divisible by 4
> * D) Ends in `74` ➔ Not divisible by 4

---

### 📝 Question 13: Which number is divisible by 3?
* **Options:**
  * A) 1235
  * B) 1237
  * C) 1239
  * D) 1241

> **✅ Answer:** 1239
>
> **🔍 Explanation:**
> A number is divisible by 3 if the sum of its digits is a multiple of 3.
> * 1235: `1+2+3+5 = 11` (No)
> * 1237: `1+2+3+7 = 13` (No)
> * 1239: `1+2+3+9 = 15` (**Yes**, 15 is divisible by 3)
> * 1241: `1+2+4+1 = 8` (No)

---

### 📝 Question 14: What is the rational form of 3.66666666...?
* **Options:**
  * A) 2/3
  * B) 11/3
  * C) 2/7
  * D) 1/9

> **✅ Answer:** 11/3
>
> **🔍 Explanation:**
> Let `x = 3.6666...`
> We know that the repeating decimal `0.6666... = 2/3`.
> Therefore, `3.6666... = 3 + 2/3 = 9/3 + 2/3 = 11/3`.

---

### 📝 Question 15: What is the smallest value that can replace `*` in `197*5462` to make it divisible by 9?
* **Options:**
  * A) 9
  * B) 2
  * C) 4
  * D) 1

> **✅ Answer:** 2
>
> **🔍 Explanation:**
> For divisibility by 9, the sum of all digits must be a multiple of 9.
> Sum of known digits: `1 + 9 + 7 + 5 + 4 + 6 + 2 = 34`.
> We need `34 + *` to be a multiple of 9. The nearest multiple of 9 after 34 is 36.
> `34 + * = 36` ➔ `* = 2`.

---

### 📝 Question 16: What is the commonly used form of a complex number?
* **Options:**
  * A) u + iv
  * B) v - u
  * C) u + v
  * D) i(u + v)

> **✅ Answer:** u + iv
>
> **🔍 Explanation:**
> A complex number is traditionally written in the standard form of `a + ib`, where `a` represents the real part and `b` represents the imaginary part. Using `u` and `v` as variables, this maps directly to the format `u + iv`.

---

### 📝 Question 17: A number divisible by 60 is also divisible by which number?
* **Options:**
  * A) 7
  * B) 11
  * C) 12
  * D) 13

> **✅ Answer:** 12
>
> **🔍 Explanation:**
> Finding the prime factors of 60: `60 = 2 × 2 × 3 × 5`.
> Finding the prime factors of 12: `12 = 2 × 2 × 3`.
> Since all the prime factors of 12 are contained within the prime factors of 60, 12 is a factor of 60. Thus, any number divisible by 60 must also be perfectly divisible by 12.

---

### 📝 Question 18: Which of the following numbers remains prime even after inversion?
* **Options:**
  * A) 31
  * B) 41
  * C) 51
  * D) None

> **✅ Answer:** 31
>
> **🔍 Explanation:**
> Let's test the inversion (reversing the digits) of the given options:
> * A) 31 reversed is 13. Both 31 and 13 are prime numbers. (**Valid**)
> * B) 41 reversed is 14. 14 is an even number, not prime.
> * C) 51 is not a prime number to begin with (`3 × 17 = 51`).

---

### 📝 Question 19: The difference between 3 times and 7 times of a number is 36. What is that number?
* **Options:**
  * A) 9
  * B) 10
  * C) 8
  * D) 6

> **✅ Answer:** 9
>
> **🔍 Explanation:**
> Let the unknown number be `x`.
> Set up the algebraic equation: `7x - 3x = 36`
> `4x = 36` ➔ `x = 36 / 4 = 9`.

---

### 📝 Question 20: The difference between the local value and the face value of 7 in the numeral 25974264 is:
* **Options:**
  * A) 5149
  * B) 69993
  * C) 64851
  * D) None of these

> **✅ Answer:** 69993
>
> **🔍 Explanation:**
> In the number `25974264`, the digit 7 is in the ten-thousands place.
> * Local Value (Place Value) = `70,000`
> * Face Value = `7` (The actual value of the digit itself)
> 
> Difference = `70,000 - 7 = 69993`.

---

### 📝 Question 21: Smallest whole number for `x` if `8x04752` is divisible by 11?
* **Options:**
  * A) 2
  * B) 4
  * C) 6
  * D) 8

> **✅ Answer:** 8
>
> **🔍 Explanation:**
> For divisibility by 11, the difference between the sum of alternate digits must be 0 or a multiple of 11.
> * Sum of digits at odd places (from left): `8 + 0 + 7 + 2 = 17`
> * Sum of digits at even places (from left): `x + 4 + 5 = x + 9`
> 
> Difference: `17 - (x + 9) = 8 - x`.
> For this difference to be 0 (or a multiple of 11), `8 - x = 0`, which means `x = 8`.

---

### 📝 Question 22: Which of the following numbers is divisible by 30?
* **Options:**
  * A) 9030
  * B) 9040
  * C) 9050
  * D) 9065

> **✅ Answer:** 9030
>
> **🔍 Explanation:**
> `30 = 2 × 3 × 5`. Therefore, the number must be divisible by 2, 3, and 5.
> * It must end in 0 (satisfying 2 and 5). This eliminates D.
> * The sum of the digits must be divisible by 3.
> Let's test the remaining options:
> * 9030: Sum `9 + 0 + 3 + 0 = 12` (**Divisible by 3**)
> * 9040: Sum `9 + 4 = 13` (Not divisible by 3)
> * 9050: Sum `9 + 5 = 14` (Not divisible by 3)

---

### 📝 Question 23: Replace `*` with the smallest number so that `817*67` is divisible by 11.
* **Options:**
  * A) 2
  * B) 3
  * C) 1
  * D) 5

> **✅ Answer:** 2
>
> **🔍 Explanation:**
> Applying the divisibility rule for 11:
> * Sum of odd place digits: `8 + 7 + 6 = 21`
> * Sum of even place digits: `1 + * + 7 = 8 + *`
> 
> Difference = `21 - (8 + *) = 13 - *`.
> We need this difference to be 0 or a multiple of 11 (like 11, 22). 
> Let's set it to 11 to find the smallest digit: `13 - * = 11` ➔ `* = 2`.

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
