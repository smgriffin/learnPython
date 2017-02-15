cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers  # Subtracs number of drivers from number of cars (100 - 30 = 70)
cars_driven = drivers  # Sets variable cars_driven equal to number of drivers
carpool_capacity = cars_driven * space_in_a_car  # Calculates total capacity by multiplying number of cars by their capacity
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."  # 100 cars available
print "There are only", drivers, "drivers available."  # 30 drivers available
print "There will be", cars_not_driven, "empty cars today."  # 70 cars not driven today
print "We can transport", carpool_capacity, "people today."  # 120 carpool capacity today
print "We have", passengers, "to carpool today."  # 90 passengers today
print "We need to put about", average_passengers_per_car, "in each car"  # About 3 passengers per car

#  In line 8 you attempted to call the variable car_pool_capacity which is a variable that does not exist.
#  the variable created on line 7 is actually carpool_capacity.  Furthermore the variable carpool_capacity
#  cannot acurately be used to calculate the average_passengers_per_car unless we knew already every car 
#  was going to be full.

#  1. It was not necessary to use a floating point variable for space_in_a_car because it is used
#     strictly to calculate in the carpool_capacity which is going to be a whole number.  If it 
#     was simply 4 then line 14 would print simply 120 as opposed to 120.0.
