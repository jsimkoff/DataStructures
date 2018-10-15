# python2

from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()

    def process(self, request):
        for i in request:
            if not self.finish_time:
                # print("first element, empty buffer")
                self.finish_time.append(request[0] + request[1])
                return Response(False, request[0]) # if buffer is empty, request will be processed immediately

            else:

                while self.finish_time[0] <= request[0]:
                    self.finish_time.popleft()
                    # print("popped finish_time = ")
                    if not self.finish_time:
                        break

                s = len(self.finish_time)
                if not s:
                    self.finish_time.append(request[0] + request[1])
                    # print("empty buffer, due to arrival time")
                    return Response(False, request[0]) # if buffer is empty, request will be processed immediately

                if s == self.size:
                    # print("full buffer at arrival time")
                    return Response(True, -1)   # if buffer is full when packet is received, drop packet

                else:
                    # print("buffer neither full nor empty, adding to buffer")
                    start_time = self.finish_time[s-1]
                    self.finish_time.append(self.finish_time[s-1] + request[1])
                    return Response(False, start_time)

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, raw_input().split())
    if buffer_size > 0:
        requests = []
        for _ in range(n_requests):
            arrived_at, time_to_process = map(int, raw_input().split()) # casts the input value to int

            requests.append(Request(arrived_at, time_to_process))   # a list of Requests (namedtuple defined at top)

        buffer = Buffer(buffer_size)
        responses = process_requests(requests, buffer)

        for response in responses:
            print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
