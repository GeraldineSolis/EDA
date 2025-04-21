class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.size = 0


    def is_full(self):
        return self.size == self.capacity


    def is_empty(self):
        return self.size == 0


    def enqueue(self, item):
        if self.is_full():
            print("Queue is full!  Car can't enter")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1


    def dequeue(self):
        if self.is_empty():
            return None
        value = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value
queue = CircularQueue(4)
total_time = 15
time = 0
car_id = 1
cars_arrived = 0
cars_passed = 0
traffic_light = "RED"


print("TRAFFIC SIMULATION 🚦")


while time <= total_time:
    # Change traffic light
    if time in [3, 8, 12]:
        traffic_light = "RED"
        print(f"Time {time}: 🔴 Traffic light turns RED")
    elif time in [5, 10, 14]:
        traffic_light = "GREEN"
        print(f"Time {time}: 🟢 Traffic light turns GREEN")


    # Cars arrive at certain times
    if time in [2, 4, 6, 10] and car_id <= 4:
        print(f"Time {time}: 🚗 Car #{car_id} arrives")
        queue.enqueue(car_id)
        car_id += 1
        cars_arrived += 1


    # When green, let a car pass
    if traffic_light == "GREEN" and not queue.is_empty():
        car = queue.dequeue()
        print(f"Time {time}:  Car #{car} passes")
        cars_passed += 1


    time += 1


# Final results
print("\n--- RESULTS --- 🎉")
print(f"Cars arrived: {cars_arrived}")
print(f"Cars passed: {cars_passed}")
