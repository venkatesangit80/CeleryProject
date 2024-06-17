from task_producer import add, subtract, multiply, divide, process_data_from_source
from time import sleep
from datetime import datetime
from script_reader import read_script

print("Parellel Execution Started")
print("time " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
script_path_add = "add.py"
script_path_subtract = "subtract.py"
script_path_multiply = "multiply.py"
script_path_divide = "divide.py"

script_code_add = read_script(script_path_add)
script_code_subtract = read_script(script_path_subtract)
script_code_multiply = read_script(script_path_multiply)
script_code_divide = read_script(script_path_divide)

result = process_data_from_source.delay(script_code_add, "add", 4, 4)
result2 = process_data_from_source.delay(script_code_add, "add", 3, 4)
result3 = process_data_from_source.delay(script_code_add, "add", 2, 4)
result4 = process_data_from_source.delay(script_code_subtract, "subtract", 6, 4)
result5 = process_data_from_source.delay(script_code_subtract, "subtract", 5, 4)
result6 = process_data_from_source.delay(script_code_subtract, "subtract", 4, 4)
result7 = process_data_from_source.delay(script_code_multiply, "multiply", 4, 4)
result8 = process_data_from_source.delay(script_code_multiply, "multiply", 3, 4)
result9 = process_data_from_source.delay(script_code_multiply, "multiply", 2, 4)
result10 = process_data_from_source.delay(script_code_divide, "divide", 8, 4)
result11 = process_data_from_source.delay(script_code_divide, "divide", 6, 4)
result12 = process_data_from_source.delay(script_code_divide, "divide", 4, 4)

# result = add.apply_async((4, 4), countdown=10)
# result = add.apply_async((4, 4), eta=datetime.now() + timedelta(seconds=10))
# result = add.apply_async((4, 4), expires=10)
# result = add.apply_async((4, 4), expires=10, countdown=10)
# result = add.apply_async((4, 4), expires=10, eta=datetime.now() + timedelta(seconds=10))
# result = add.apply_async((4, 4), expires=10, countdown=10, eta=datetime.now() + timedelta(seconds=10))

# print(result.ready())
# print(result.successful())
# print(result.state)

while not result.ready():
    sleep(1)

if result.successful():
    print(result.get())

while not result2.ready():
    sleep(1)

if result2.successful():
    print(result2.get())

while not result3.ready():
    sleep(1)

if result3.successful():
    print(result3.get())

while not result4.ready():
    sleep(1)

if result4.successful():
    print(result4.get())

while not result5.ready():
    sleep(1)

if result5.successful():
    print(result5.get())

while not result5.ready():
    sleep(1)

if result6.successful():
    print(result6.get())

while not result6.ready():
    sleep(1)

if result7.successful():
    print(result7.get())

while not result8.ready():
    sleep(1)

if result8.successful():
    print(result8.get())

while not result9.ready():
    sleep(1)

if result9.successful():
    print(result9.get())

while not result10.ready():
    sleep(1)

if result10.successful():
    print(result10.get())

while not result11.ready():
    sleep(1)

if result11.successful():
    print(result11.get())

while not result12.ready():
    sleep(1)

if result12.successful():
    print(result12.get())

print("time " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("Parellel Execution Completed")
print("Sequential Execution Started")
print("time " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

result3 = add(4, 4)
print(result3)
result4 = add(3, 4)
print(result4)
result5 = add(2, 4)
print(result5)

print("time " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("Sequential Execution Completed")
# Sequential Execution will take 1 minute for 3 adds, but parallel execution will take 40 seconds for 12 tasks with one worker and 20 seconds for 12 tasks with 2 workers.
# Total 41 seconds for parellel execution of 12 tasks using 1 worker and sequential execution of 3 tasks took 1 min.
# Now 2 workers  tasks got distributed and executed in 20 seconds.
# Tasks got distributed to 2 workers and executed in 20 seconds.
