# Customer Churn Analysis Report

## High Risk Profile - Values that Indicate HIGH Churn

---

## Dataset Overview

- **Total Customers**: 10,000
- **Churned Customers**: 2,037 (20.37%)
- **Non-Churned Customers**: 7,963 (79.63%)
- **Model Threshold for HIGH Risk**: Churn Probability ≥ 70%

---

## Key Findings: What Triggers HIGH Churn Risk?

### 1. **AGE (Most Important Factor)**

- **Churned Customers**: Mean Age = 44.84 years | Median = 45 years
- **Non-Churned Customers**: Mean Age = 37.41 years | Median = 36 years
- **Insight**: Customers aged **40-60** are significantly more likely to churn
- **HIGH RISK RANGE**: Age ≥ 40 (especially 45+)

### 2. **ACTIVE MEMBER STATUS (Critical Factor)**

- **Churned Customers**: Only 36.08% are active members
- **Non-Churned Customers**: 55.46% are active members
- **Insight**: Inactive members are **1.5x more likely to churn**
- **HIGH RISK**: `IsActiveMember = 0` (NOT an active member)

### 3. **GEOGRAPHY (Significant Factor)**

| Country | Churn Rate | Risk Level     |
| ------- | ---------- | -------------- |
| Germany | 32.44%     | ⚠️ **HIGHEST** |
| Spain   | 16.67%     | Low            |
| France  | 16.15%     | Low            |

- **HIGH RISK**: Country = **Germany**

### 4. **GENDER (Noticeable Factor)**

| Gender | Churn Rate | Risk Level    |
| ------ | ---------- | ------------- |
| Female | 25.07%     | ⚠️ **HIGHER** |
| Male   | 16.46%     | Lower         |

- **HIGH RISK**: Gender = **Female**

### 5. **CREDIT SCORE (Minor Factor)**

- **Churned Customers**: Mean = 645.35
- **Non-Churned Customers**: Mean = 651.85
- **Insight**: Slightly lower scores associated with churn
- **Note**: Not a strong indicator individually

### 6. **BALANCE (Moderate Factor)**

- **Churned Customers**: Mean Balance = $91,108.54
- **Non-Churned Customers**: Mean Balance = $72,745.30
- **Insight**: Surprisingly, higher balances correlate with churn
- **HIGH RISK**: Balance between $50,000 - $150,000

### 7. **NUMBER OF PRODUCTS (Weak Factor)**

- **Churned Customers**: Mean = 1.48 products
- **Non-Churned Customers**: Mean = 1.54 products
- **Insight**: Minimal difference - not a strong predictor

### 8. **TENURE (Weak Factor)**

- **Churned Customers**: Mean = 4.93 years
- **Non-Churned Customers**: Mean = 5.03 years
- **Insight**: Similar tenure - not a strong differentiator

---

## 🔴 HIGH CHURN RISK PROFILE (Probability ≥ 70%)

**The ideal values to submit that will likely result in HIGH CHURN prediction:**

```
✓ Credit Score:      450 - 550 (Low)
✓ Age:               45 - 60 (Older customer)
✓ Tenure:            0 - 5 years (Any recent tenure)
✓ Balance:           80,000 - 150,000 (Higher balance)
✓ Products:          1 - 2 products (Few products)
✓ Gender:            Female (Higher churn rate)
✓ Country:           Germany (32.44% churn rate)
✓ Active Member:     NO (0) *** CRITICAL ***
✓ Credit Card:       1 (Irrelevant)
```

---

## 📊 Test Cases for HIGH Churn Prediction

### **Test Case 1: Classic High Risk Profile**

```
Credit Score:    500
Age:            50
Tenure:         2
Balance:        100000
Products:       1
Gender:         Female
Country:        Germany
Active Member:  NO (0)
Credit Card:    Yes (1)
Salary:         50000

Expected Output: HIGH RISK (75-95% probability)
```

### **Test Case 2: Inactive Older Customer**

```
Credit Score:    520
Age:            55
Tenure:         3
Balance:        90000
Products:       1
Gender:         Female
Country:        Germany
Active Member:  NO (0)
Credit Card:    Yes (1)
Salary:         75000

Expected Output: HIGH RISK (85-95% probability)
```

### **Test Case 3: Lower Balance, Inactive**

```
Credit Score:    480
Age:            48
Tenure:         4
Balance:        75000
Products:       2
Gender:         Female
Country:        Germany
Active Member:  NO (0)
Credit Card:    Yes (1)
Salary:         60000

Expected Output: HIGH RISK (70-90% probability)
```

### **Test Case 4: Different Country but Still High Risk**

```
Credit Score:    510
Age:            52
Tenure:         1
Balance:        120000
Products:       1
Gender:         Female
Country:        Spain
Active Member:  NO (0)
Credit Card:    Yes (1)
Salary:         80000

Expected Output: HIGH RISK (70-80% probability)
```

---

## ⚠️ Critical Factors Summary

| Factor               | Importance    | HIGH RISK Value |
| -------------------- | ------------- | --------------- |
| Active Member Status | **HIGHEST**   | 0 (NOT Active)  |
| Age                  | **VERY HIGH** | 45+ years       |
| Geography            | **HIGH**      | Germany         |
| Gender               | **MODERATE**  | Female          |
| Balance              | **MODERATE**  | $50K-$150K      |
| Credit Score         | **LOW**       | 450-550         |
| Tenure               | **LOW**       | Any value OK    |
| Products             | **LOW**       | 1-2 products    |

---

## 💡 Key Insights for Business

1. **Inactive members are the biggest churn risk** - Focus retention efforts here
2. **Older customers (45+) need special attention** - May need personalized services
3. **Germany has 2x churn rate** - Market-specific issues?
4. **Female customers show higher churn** - Gender-specific factors to investigate
5. **High balance doesn't mean loyalty** - High-value customers may leave
6. **Number of products doesn't deter churn** - Need better engagement strategies

---

## How to Use This Analysis

1. **Use the test cases above** to verify the model works correctly
2. **Fill in the form with values from any test case** to get HIGH risk prediction
3. **Adjust values slightly** to see probability changes
4. **Compare with LOW risk profile** to understand the model's logic
