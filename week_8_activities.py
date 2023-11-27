import statistics
# Week 8 Day 11
#--------------------------------------------------------------------
# ACTIVITY 1
#--------------------------------------------------------------------
# Create a function that calcuates a range of interger data in a list

# number_list = [4,5,6,6,8,12,15,17,17,17,19,21]
# # sequence of numbers

# def calculate_range(number_list):
# # function called calculate_range is defined and takes 1 parameter which is the list of numbers we want to calculate the range of
# # outcome is empty liost to store the min and max values.
# # .extend, when we want to add multiple things to list(adding the values of range1 and range2 to outcome list)- .append only adds 1 thing to list
# # return= we want to use the outcome- so retuning the outcome list containing min and max values.
#     outcome = []
#     for i in number_list:
#         range1 = min(number_list)
#         range2 = max(number_list)
#         outcome.extend([range1, range2])
#         return outcome
    
# result = calculate_range(number_list)

# # outcome = [range1(min), range2(max)]
# # calculate_range function is called with number_list - ([range1, range2] stored in variable result)
# range_result = result[1] - result[0]
# # # range calcuated by subtracting min value'result[0] from max result[1] from max value 'result[1]
# print(range_result)

number_list = [4,5,6,6,8,12,15,17,17,17,19,21]

def calculate_range(data):
    range1 = min(data)
    range2 = max(data)
    print(f"The range is - {range2 - range1:.2f}")


# calculate_range(number_list)
# --------------------------------------------------------------------
# Activity 2
# --------------------------------------------------------------------
# now create functions that calculate the Mean, Mode and Median

# MEAN
# number_list = [4,5,6,6,8,12,15,17,17,17,19,21]

def calculate_mean(data):
    mean_value = statistics.mean(data)
    print(f"This is the mean - {mean_value:.2f}")

# calculate_mean(number_list)

# def mean_value(data):
    #   return sum(data)/len(data):
    #   print(data)
    

# result = calculate_mean(number_list)

# print(result)
    
# # Median
# number_list = [4,5,6,6,8,12,15,17,17,17,19,21]

def calculate_median(data):
    median_value = statistics.median(data)
    print(f"This is the median - {median_value:.2f}")
    

# result = calculate_median(number_list)

# print(result)

# # MODE
# number_list = [4,5,6,6,8,12,15,17,17,17,19,21]

def calculate_mode(data):
    mode_value = statistics.mode(data)
    print(f"This is the mode - {mode_value:.2f}")
    

# result = calculate_mode(number_list)

# print(result)
# ---------------------------------------------
# # Activity 3
# ---------------------------------------------
# # megabytes_sales 
megabytes_sales = [256.85, 295.65, 248.25, 275.90, 273.35, 282.40, 257.20, 294.90, 263.90, 2316.50, 459.25, 567.85, 97.80, 72.50]
# # sunday figures- 97.80, 72.50
# use dictionary if need day data

calculate_mean(megabytes_sales)
calculate_median(megabytes_sales)
calculate_mode(megabytes_sales)
calculate_range(megabytes_sales)

# ORIGINAL RESULTS
# This is the mean - 425.88
# This is the median - 274.62
# This is the mode - 256.85
# The range is - 2244.00

# SUNDAY RESULTS
# This is the mean - 482.67
# This is the median - 279.15
# This is the mode - 256.85
# The range is - 2068.25

# Not much difference- shows us Sunday is the day we earn the least and doesn't have a huge impact on overall figures- do we need to be open on Sundays? 
# or what can we do better?
