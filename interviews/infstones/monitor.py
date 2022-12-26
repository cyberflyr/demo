import json
import multiprocessing
import os

from redis import Redis


redis_client = Redis()
channel = "monitor"
subprocess_pool = {}


def check_then_rerise_proc():
    for pid in subprocess_pool.keys():
        cmd = f"ps aux | grep {pid} | grep -v grep"
        res = os.popen(cmd)
        output_str = res.read()
        if not output_str:
            redis_client.publish("forever", subprocess_pool[pid])
            del subprocess_pool[pid]


if __name__ == "__main__":
    pubsub = redis_client.pubsub()
    pubsub.subscribe([channel])
    while True:
        for msg in pubsub.listen():
            if msg.get("type") == "message":
                data = msg.get("data")
                pid, arg = json.loads(data)
                subprocess_pool[pid] = arg
                print(subprocess_pool)
                multiprocessing.Process(target=check_then_rerise_proc)
