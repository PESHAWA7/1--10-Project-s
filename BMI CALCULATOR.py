height = input("inter your height, please: ")
weight = input("inter your weight, please: ")

weight_as_int = int(weight)
height_as_float = float(height)
# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
BMI = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(BMI)
print(bmi_as_int)
# PEMDAS: stands for Parentheses, Exponents, Multiplication and Division (same level), and Addition and Subtraction
# (same level). By following these steps, you can simplify and accurately solve mathematical expressions, ensuring
# a correct final answer.
