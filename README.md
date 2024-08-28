# Pet Treat Shop - Pricing Calculator

Welcome to the **Pet Treat Shop** Pricing Calculator! This project showcases my Python skills and unique coding style through the development of a simple yet flexible pricing calculator for a pet treat shop.

## Project Overview

The Pet Treat Shop offers three types of treats: **biscuits**, **chewies**, and **vitamins**. The prices vary based on the bucket size and the day of the week. Additionally, the shop offers various discounts that can be combined, making the pricing calculation a bit more complex.

|      Bucket     |     Biscuits    |     Chewies     |     Vitamins    |
|-----------------|-----------------|-----------------|-----------------|
|      Normal     |     R2.00/pc    |     R4.10/pc    |     R2.50/pc    |
|      Large      |     R3.75/pc    |     R4.50/pc    |     R4.15/pc    |

## Features

- **Weekend Pricing**: Automatic 15% price increase on weekends.
- **Multiple Discounts**: 
  - 5% discount for more than 7 vitamins in a Normal bucket.
  - 10% discount for 10 or more chewies in a Large bucket.
  - 20% discount for purchasing more than 20 treats in total.
- **Combined Discounts**: Discounts are made in the above-described order and can be combined!
- **Default Bucket Fill**: The price for filling a bucket is always R2.

## Project Summary
Write a program that calculates the price of a bucket.

## Input Data
The input is read from the console and contains exactly 5 lines:
- **Line 1**: the number of purchased biscuits **Int: 0-200**
- **Line 2**: the number of purchased chewies **Int: 0-200**
- **Line 3**: the number of purchased vitamins **Int: 0-200**
- **Line 4**: the bucket size **String: 'Normal'/'Large'**
- **Line 5**: if day is on a weekend **String: Y = Yes / N = No**

## Output Data
Print requirements: 
- 1 number – the price of treats
- format up to the second digit after the decimal point

## Sample Input and Output
### Weekend
|      Input     |     Output    |                  Comments                   |
|----------------|---------------|---------------------------------------------|
|        2       |               |                                             |
|        4       |               |                                             |
|        8       |     46.14     |  Price: 2*2.00 + 4*4.10 + 8*2.50 = R40.40   |
|     Normal     |               |                                             |
|        Y       |               |                                             |

- **Weekend**: 40.40 + 15% = R46.46
- **5% Discount**: for more than 7 vitamins for a normal bucket: 44.14
- **No Discount**: if the treats are in total 20 or less
- **Filling The Bucket**: 44.14 + 2 = R46.14

### Not A Weekend
|      Input     |     Output    |                  Comments                   |
|----------------|---------------|---------------------------------------------|
|        3       |               |                                             |
|        10      |               |                                             |
|        9       |     69.39     |  Price: 3*3.75 + 10*4.50 + 9*4.15 = R93.60  |
|      Large     |               |                                             |
|        N       |               |                                             |

- **Not A Weekend**: no increase in price
- **10% Discount**: for more than 10 chewies for a large bucket: 84.24
- **20% Discount**: treats are in total over 20 = 67.392
- **Filling The Bucket**: 67.392 + 2 = R69.392

### Extra test case
|      Input     |     Output    |
|----------------|---------------|
|        10      |               |
|        10      |               |
|        10      |     91.28     |
|      Large     |               |
|        N       |               |

## Conclusion

This project is a simple demonstration of my ability to handle complex pricing logic, including conditional price increases, discounts, and user input. The clean, well-structured code reflects my attention to detail and commitment to writing maintainable, efficient Python code.
