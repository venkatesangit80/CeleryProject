from task_producer.tasks import process_data_from_source_normal as process_data_from_source
from time import sleep
from datetime import datetime
from script_reader import read_script

print("Parellel Execution Started")
print("time " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
script_path_weather = "weatherretreiver.py"

script_code_weather = read_script(script_path_weather)

args = ()
weatheresult = process_data_from_source.delay(script_code_weather, "get_weather", "Bangalore")

# result = add.apply_async((4, 4), countdown=10)
# result = add.apply_async((4, 4), eta=datetime.now() + timedelta(seconds=10))
# result = add.apply_async((4, 4), expires=10)
# result = add.apply_async((4, 4), expires=10, countdown=10)
# result = add.apply_async((4, 4), expires=10, eta=datetime.now() + timedelta(seconds=10))
# result = add.apply_async((4, 4), expires=10, countdown=10, eta=datetime.now() + timedelta(seconds=10))

# print(result.ready())
# print(result.successful())
# print(result.state)

print("time " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("Sequential Execution Completed")
# Sequential Execution will take 1 minute for 3 adds, but parallel execution will take 40 seconds for 12 tasks with one worker and 20 seconds for 12 tasks with 2 workers.
# Total 41 seconds for parellel execution of 12 tasks using 1 worker and sequential execution of 3 tasks took 1 min.
# Now 2 workers  tasks got distributed and executed in 20 seconds.
# Tasks got distributed to 2 workers and executed in 20 seconds.
