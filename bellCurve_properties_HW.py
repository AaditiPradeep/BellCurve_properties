import statistics
import csv

with open("StudentsPerformance.csv") as csv_file:
    reader = csv.reader(csv_file)
    file_data = list(reader)

file_data.pop(0)

maths_score = []

for i in range(len(file_data)):
    number = file_data[i][5]
    maths_score.append(int(number))

mean = statistics.mean(maths_score)
print("The mean is: ", mean)

median = statistics.median(maths_score)
print("The medain is: " , median)

mode = statistics.mode(maths_score)
print("The mode is: " , mode)

std_dev = statistics.stdev(maths_score)
print("The standard deviation is: " , std_dev)

first_std_deviation_start , first_std_deviation_end = mean-std_dev, mean+std_dev
second_std_deviation_start , second_std_deviation_end = mean - (2*std_dev) , mean + (2*std_dev)
third_std_deviation_start , third_std_deviation_end = mean - (3*std_dev) , mean + (3*std_dev)

list_of_data_within_1_std_dev =[result for result in maths_score if result > first_std_deviation_start and result < first_std_deviation_end]
print("{}%of data lies between one std_dev".format(len(list_of_data_within_1_std_dev)*100.0/len(maths_score)))

list_of_data_within_2_std_dev =[result for result in maths_score if result > second_std_deviation_start and result < second_std_deviation_end]
print("{}%of data lies between two std_dev".format(len(list_of_data_within_2_std_dev)*100.0/len(maths_score)))

list_of_data_within_3_std_dev =[result for result in maths_score if result > third_std_deviation_start and result < third_std_deviation_end]
print("{}%of data lies between three std_dev".format(len(list_of_data_within_3_std_dev)*100.0/len(maths_score)))
