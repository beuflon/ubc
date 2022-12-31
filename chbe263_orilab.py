# Random Errors and Gaussian Distribution (q3)

# Inputs: Data from lab
# Outputs: The average (x_bar)
def calculateXBar(lab_data):
    num_data = len(lab_data)
    sum = 0
    x_bar = 0

    for i in range(num_data):
        sum += lab_data[i]

    x_bar = (sum)/num_data 
    return round(x_bar, 4)

# Inputs: x_bar, lab_data:List[]
# Outputs: standard deviation (s)
def standardDeviationCalc(lab_data):
    x_bar = calculateXBar(lab_data)
    sum_squared = 0

    for i in range(len(lab_data)):
        sum_squared += (x_bar - lab_data[i])**2

    s_squared = sum_squared/(len(lab_data)-1)
    s = s_squared**0.5
    return s 

# Inputs: Student t-values table:List[], standard deviation (s)
# Outputs: uNceRtaintieS
def phys159ptsdfrfr(t_values, s, num_data):
    uncertainty = t_values*s/num_data**0.5
    return round(uncertainty, 4) 

# Calculate the accuracy (q1)

# Input: Lab data in mL, theoretical values of pipettes
# Output: accuracy
def systematicError(lab_data, theoValue): 
    x_bar = calculateXBar(lab_data)
    accuracy = abs(x_bar - theoValue) * 100
    return round(accuracy, 4)

# Calculate the relative standard deviation (q2)

# Inputs: standard deviation, mean volume (mL)
# Output: relative standard deviation (s_r)
def relativeStandardDev(s, x_bar, lab_data):
    s = standardDeviationCalc(lab_data)
    x_bar = calculateXBar(lab_data)
    s_r = (s/x_bar) * 100
    return s_r

# With data
theo_Value1 = 1.0000
theo_Value2 = 5.0000

weight_data1 = [1.0022, 0.9966, 0.9930, 0.9931, 0.9934]
weight_data2 = [1.0234, 1.0305, 1.0321, 1.0312, 1.0344]
weight_data3 = [4.9483, 4.9511, 4.9557, 4.9653, 4.9994]

temperature_constant = 0.9982

lab_data1 = [x/temperature_constant for x in weight_data1]
lab_data2 = [x/temperature_constant for x in weight_data2]
lab_data3 = [x/temperature_constant for x in weight_data3]

t_values90 = 2.13
t_values99 = 4.60
t_values95 = 2.78
num_data = len(lab_data1)

# Pipette accuracy
print("Question 1:")
print("1ml P1000:", systematicError(lab_data1, theo_Value1))
      
print("1ml P5000:", systematicError(lab_data2, theo_Value1))

print("5ml P5000:", systematicError(lab_data3, theo_Value2))
    
# Relative standard deviation
print("Question 2:")
print("1ml P1000:", relativeStandardDev(standardDeviationCalc(lab_data1), calculateXBar(lab_data1), lab_data1))
print("1ml P5000:", relativeStandardDev(standardDeviationCalc(lab_data2), calculateXBar(lab_data2), lab_data2))
print("5ml P5000:", relativeStandardDev(standardDeviationCalc(lab_data3), calculateXBar(lab_data3), lab_data3))

print("Question 3:")
# 95% confidence
print("95 percent confidence")
print("1ml P1000:", calculateXBar(lab_data1), "+/-", phys159ptsdfrfr(t_values95, standardDeviationCalc(lab_data1), num_data))
print(standardDeviationCalc(lab_data2))
print("1ml P5000:", calculateXBar(lab_data2), "+/-", phys159ptsdfrfr(t_values95, standardDeviationCalc(lab_data2), num_data))
print(standardDeviationCalc(lab_data3))
print("5ml P5000:", calculateXBar(lab_data3), "+/-", phys159ptsdfrfr(t_values95, standardDeviationCalc(lab_data3), num_data))

# 90% confidence
print("90 percent confidence")
print("1ml P1000:", calculateXBar(lab_data1), "+/-", phys159ptsdfrfr(t_values90, standardDeviationCalc(lab_data1), num_data))
print("1ml P5000:", calculateXBar(lab_data2), "+/-", phys159ptsdfrfr(t_values90, standardDeviationCalc(lab_data2), num_data))
print("5ml P5000:", calculateXBar(lab_data3), "+/-", phys159ptsdfrfr(t_values90, standardDeviationCalc(lab_data3), num_data))

# 99% confidence
print("99 percent confidence")
print("1ml P1000:", calculateXBar(lab_data1), "+/-", phys159ptsdfrfr(t_values99, standardDeviationCalc(lab_data1), num_data))
print("1ml P5000:", calculateXBar(lab_data2), "+/-", phys159ptsdfrfr(t_values99, standardDeviationCalc(lab_data2), num_data))
print("5ml P5000:", calculateXBar(lab_data3), "+/-", phys159ptsdfrfr(t_values99, standardDeviationCalc(lab_data3), num_data))