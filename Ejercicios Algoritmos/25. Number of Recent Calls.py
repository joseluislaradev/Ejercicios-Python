# You have a system that receives requests over time.

# Every time a new request arrives at time t, you need to know how many requests happened during the last 3000 milliseconds, including the current request.

# More precisely, after receiving a request at time t, count all requests whose time is in:

# [t - 3000, t]

# Example:

# ping(1)

# Window:

# [-2999, 1]

# Requests:

# 1

# Return:

# 1

# Then:

# ping(100)

# Window:

# [-2900, 100]

# Requests still inside:

# 1, 100

# Return:

# 2

# Then:

# ping(3001)

# Window:

# [1, 3001]

# Requests:

# 1, 100, 3001

# Return:

# 3

# Then:

# ping(3002)

# Window:

# [2, 3002]

# Now request 1 is too old:

# 100, 3001, 3002

# Return:

# 3
# Guarantees
# t is always positive.
# Every new t is strictly greater than the previous one.
# You don't need to validate the input.
# The object must remember previous calls between executions of ping().


from collections import deque


class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        self.requests.append(t)
        
        while self.requests and self.requests[0] < t - 3000:
                self.requests.popleft()
        
        return len(self.requests)
    
    
# counter = RecentCounter()

# print(counter.ping(1))
# # 1

# print(counter.ping(100))
# # 2

# print(counter.ping(3001))
# # 3

# print(counter.ping(3002))
# # 3



counter = RecentCounter()

print(counter.ping(1000))
# 1

print(counter.ping(2000))
# 2

print(counter.ping(4000))
# 3

print(counter.ping(7001))
# 1