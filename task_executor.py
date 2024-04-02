from tasks import add
from time import sleep

result = add.delay(4, 4)
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
    print("Waiting...")
    sleep(1)
if result.successful():
    print(result.get())