# python2
from heapq import heappush, heappop, heapify
import itertools

class JobQueue:

    def read_data(self):
        self.num_workers, m = map(int, raw_input().split())
        self.jobs = list(map(int, raw_input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print("%0.f %0.f" % (self.assigned_workers[i], self.start_times[i]))


    def assign_jobs_pq(self):
        # plan: use a min heap to store the available threads - priority is next
        # available time
        # counter = itertools.count()
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)

        pq = []
        for i in range(self.num_workers):
            heappush(pq, (0, i))

        heapify(pq)

        for j in range(0, len(self.jobs)):
            worker = heappop(pq)
            self.assigned_workers[j], self.start_times[j] = worker[1], worker[0]
            heappush(pq, (worker[0]+self.jobs[j], worker[1] ))


    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        # do this for each of the m jobs
        for i in range(len(self.jobs)):
            # first job goes to worker 0
            next_worker = 0

            # scan through the remaining (n-1) workers
            for j in range(self.num_workers):

                # if any of them has a "next free time" before the current candidate,
                # update the next_worker to be that worker instead
                if next_free_time[j] < next_free_time[next_worker]:
                    next_worker = j

            # once the most readily available worker has been found, assign them to
            # the current job, i
            self.assigned_workers[i] = next_worker
            # and set the start time to be the time that worker became free
            self.start_times[i] = next_free_time[next_worker]
            # update that worker's next_free time to reflect the time it takes to
            # complete job i
            next_free_time[next_worker] += self.jobs[i]

    def solve(self):
        self.read_data()
        self.assign_jobs_pq()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
