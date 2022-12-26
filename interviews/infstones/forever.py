import json
import multiprocessing
import time
import os
from redis import Redis

redis_client = Redis()
send_channel = "monitor"
recv_channel = "forever"


def sub_forever():
    cur_pid = os.getpid()
    while True:
        print("sub pid:", cur_pid)
        time.sleep(1)


def forever():
    """Simple program that greets NAME for a total of COUNT times."""
    pubsub = redis_client.pubsub()
    pubsub.subscribe([recv_channel])
    while True:
        for msg in pubsub.listen():
            if msg.get("type") == "message":
                count = int(msg.get("data"))
                print(msg)
                sub_proc = multiprocessing.Process(target=sub_forever, args=(count,))
                sub_proc.start()
                redis_client.publish(send_channel, json.dumps([sub_proc.pid, count]))


if __name__ == "__main__":
    forever()
