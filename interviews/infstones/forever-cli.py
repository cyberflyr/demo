from redis import Redis
import click

channel = "forever"
redis_client = Redis()


@click.command()
@click.option("--count", default=1, help="Number of greetings.")
def hello(count):
    """Simple program that greets NAME for a total of COUNT times."""
    redis_client.publish(channel, count)


if __name__ == "__main__":
    hello()
