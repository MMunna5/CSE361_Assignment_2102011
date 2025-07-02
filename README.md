# CSE361_Assignment_2102011

```markdown
# CipherShift-Invert Cryptographic Algorithm

## 📚 Course Information

- **Course Title:** Mathematical Analysis for Computer Science  
- **Course Code:** CSE 361  
- **Assignment:** Individual Task

## 🔐 Algorithm Overview

### Algorithm Name
**CipherShift-Invert**

### 🔧 Encryption Process

1. Map each letter to a number from 0–25 (A=0, B=1, ..., Z=25).
2. Add the key and take modulo 26.
3. Convert the result to 5-bit binary.
4. Apply bitwise NOT (invert each bit).
5. Convert the inverted binary back to decimal and take modulo 26.
6. Convert the result to the corresponding letter.

### 🔓 Decryption Process

1. Map each ciphertext letter to its index (0–25).
2. Convert the index to 5-bit binary.
3. Apply bitwise NOT (invert each bit).
4. Convert the binary to decimal.
5. Subtract the key and take modulo 26.
6. Convert the result to the original letter.

## 🧪 Test Case & Experimental Results

- **Plaintext:** `HELLO`  
- **Key:** `3`  
- **Ciphertext:** `VYRRO`  
- **Decrypted:** `HELLO`

✅ **Verification:** The algorithm successfully retrieves the original plaintext.

## 🧠 Pseudocode

> *See "Algorithm Overview" above for step-by-step encryption and decryption logic.*

## 🔄 Flowchart Description

### Encryption:


Input letter → Map to 0–25 → Add key (mod 26) → Convert to binary → Apply NOT → Convert to decimal (mod 26) → Output letter



### Decryption:


Input letter → Map to 0–25 → Convert to binary → Apply NOT → Convert to decimal → Subtract key (mod 26) → Output letter



## 💻 Source Code

> *Python implementation available in the accompanying file.*

## 📤 Submission Information

- **Submitted By:**  Md. Moniruzzaman Munna 
- **Submitted To:** Pankaj Bhowmik  
- **Department:** Computer Science and Engineering  
- **University:** Hajee Mohammad Danesh Science and Technology University, Dinajpur-5200  
- **Date:** July 02, 2025, 10:39 AM (GMT +06)

## 📊 Presentation Notes

Prepared to demonstrate:
- Algorithm Design
- Test Case Execution
- Source Code Explanation
```

