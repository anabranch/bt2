import ray


# ray.init()
# import anyscale 
# anyscale.connect()

@ray.remote
class BillsService:
    def __init__(self):
        pass

@ray.remote
def some_function():
    import time
    time.sleep(2)
    return 2


print(sum(ray.get([some_function.remote() for x in range(500)])))