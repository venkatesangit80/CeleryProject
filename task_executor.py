from task_producer import add, subtract, multiply, divide
from time import sleep
from datetime import datetime

print("Parellel Execution Started")
print("time " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
result = add.delay(4, 4)
result2 = add.delay(3, 4)
result3 = add.delay(2, 4)
result4 = subtract.delay(6, 4)
result5 = subtract.delay(5, 4)
result6 = subtract.delay(4, 4)
result7 = multiply.delay(4, 4)
result8 = multiply.delay(3, 4)
result9 = multiply.delay(2, 4)
result10 = divide.delay(8, 4)
result11 = divide.delay(6, 4)
result12 = divide.delay(4, 4)

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
