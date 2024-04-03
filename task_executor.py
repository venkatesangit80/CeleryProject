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