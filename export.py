import csv
import sys


def export_csv(tasks, out=sys.stdout):
    writer = csv.DictWriter(out, fieldnames=["title", "done"], extrasaction="ignore")
    writer.writeheader()
    for task in tasks:
        writer.writerow({"title": task.get("title", ""), "done": task.get("done", False)})
