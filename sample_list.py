''' 
Practicing code by using print(), range(), 
and other functions. The goal is to recall usage of method
or loops to get the solutions. Below is a sample list that will
be used for this exercise.
'''

sample_list = [
    469, 755, 244, 245, 758, 450, 
    302, 20, 712, 71, 456, 21, 398, 
    339, 882, 848, 179, 535, 940, 472
]

# 1. print("Elements and count of sample_list:")
sample_count = 0
for sample in sample_list:
    counter = sample_list.count(sample)
    sample_count += counter
    print(sample)
print(f" There are {sample_count} numbers.")

# 2. print("Even elements and their count:")
even_count = 0
for sample in sample_list:
    if sample%2 == 0:
        counter = sample_list.count(sample)
        even_count += counter
        print(sample)
print(f"There are {even_count} even numbers.")

# 3. print("Odd elements and their count:")
odd_count = 0
for sample in sample_list:
    if sample%2 == 1:
        counter = sample_list.count(sample)
        odd_count += counter
        print(sample)
print(f"There are {odd_count} odd numbers.")

# 4. print("Squares of elements of sample_list:")
for sample in sample_list:
    square_sample = pow(sample, 2)
    print(square_sample)

# 5. print("Sum of elements of sample_list:")
total = sum(sample_list)
print(f"The total of the sample list is {total}")

# 6. print("Smallest (min) element of sample_list:")
min_sample = min(sample_list)
print(f"The minimum sample is {min_sample}.")

# 7. print("Largest (max) element of sample_list:")
max_sample = max(sample_list)
print(f"The maximum sample number is {max_sample}.")