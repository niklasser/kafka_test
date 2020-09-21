import argparse
import kafka
parser = argparse.ArgumentParser()

parser.add_argument("--host", help="Change cluster host (default is localhost:9092")
group = parser.add_mutually_exclusive_group()
group.add_argument("-list", help="Lists topics",action="store_true")
group.add_argument("-add", help="Adds topic. Takes <name> <partitions> <replication factor>", nargs=3)
group.add_argument("-delete", help="Deletes topic. Takes <Topic name>")
args = parser.parse_args()

host = 'localhost:19092'
if args.host:
    host = args.host

if args.list:
    # To consume latest messages and auto-commit offsets
    consumer = kafka.KafkaConsumer(bootstrap_servers=[host])
    topics = consumer.topics()
    for topic in topics:
        print(topic)
elif args.add:
    admin = kafka.KafkaAdminClient(bootstrap_servers=[host])
    topics=[]
    topics.append(kafka.admin.NewTopic(name=args.add[0], num_partitions=int(args.add[1]), replication_factor=int(args.add[2])))
    res = admin.create_topics(new_topics=topics)
    print(res)
elif args.delete:
    admin = kafka.KafkaAdminClient(bootstrap_servers=[host])
    topics=[]
    topics.append(args.delete)
    res = admin.delete_topics(topics)
    print(res)
