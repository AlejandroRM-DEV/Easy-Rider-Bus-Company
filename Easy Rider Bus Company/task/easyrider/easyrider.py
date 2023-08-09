import json
import re
from collections import Counter
from datetime import datetime


def check_errors(buses):
    time_pattern = r'([01][0-9]|2[0-3]):[0-5][0-9]$'
    stop_name_pattern = r'([A-Z][a-z ]+)+(Road|Avenue|Boulevard|Street)$'

    stop_name = 0
    stop_type = 0
    a_time = 0

    for bus in buses:
        if (not isinstance(bus["stop_name"], str) or len(bus["stop_name"]) <= 0 or
                re.match(stop_name_pattern, bus["stop_name"]) is None):
            stop_name += 1

        if isinstance(bus["stop_type"], str):
            if len(bus["stop_type"]) >= 1 and bus["stop_type"] not in ["S", "O", "F"]:
                stop_type += 1
        else:
            stop_type += 1

        if not isinstance(bus["a_time"], str) or not re.match(time_pattern, bus["a_time"]):
            a_time += 1

    total = stop_name+stop_type+a_time
    print(f"Type and required field validation: {total} errors")
    print(f"stop_name: {stop_name}")
    print(f"stop_type: {stop_type}")
    print(f"a_time: {a_time}")


def count_stops(buses):
    counts = {}
    for bus in buses:
        if bus["bus_id"] in counts:
            counts[bus["bus_id"]] += 1
        else:
            counts[bus["bus_id"]] = 1

    print(counts)


def check_stops_types(buses):
    bus_stops = {}
    stop_names = []
    starting_stops = set()
    final_stops = set()
    wrong_on_demand_stops = set()

    for stop in buses:
        bus_id = stop["bus_id"]
        stop_name = stop["stop_name"]
        stop_type = stop["stop_type"]

        if bus_id not in bus_stops:
            bus_stops[bus_id] = []

        bus_stops[bus_id].append((stop_name, stop_type))

    for bus_id, stops in bus_stops.items():
        stop_types = [stop_type for _, stop_type in stops]

        if "S" not in stop_types or "F" not in stop_types:
            print(f"There is no start or end stop for the line: {bus_id}")
            exit()

        starting_stops.add([stop_name for stop_name, stop_type in stops if stop_type == "S"][0])
        final_stops.add([stop_name for stop_name, stop_type in stops if stop_type == "F"][0])
        stop_names.append([stop_name for stop_name, _ in stops])

    counters = [Counter(arr) for arr in stop_names]
    element_counts = Counter()
    for counter in counters:
        element_counts.update(counter)

    transfer_stops = [element for element, count in element_counts.items() if count >= 2]

    print("Start stops:", len(starting_stops), sorted(starting_stops))
    print("Transfer stops:", len(transfer_stops), sorted(transfer_stops))
    print("Finish stops:", len(final_stops), sorted(final_stops))

    for stop in buses:
        stop_name = stop["stop_name"]
        stop_type = stop["stop_type"]
        if (stop_type == "O" and
                (stop_name in starting_stops or stop_name in transfer_stops or stop_name in final_stops)):
            wrong_on_demand_stops.add(stop_name)

    if len(wrong_on_demand_stops):
        print(sorted(wrong_on_demand_stops))
    else:
        print("OK")

def check_stops_times(buses):
    last_bus_id = None
    last_time = None
    errors = []
    for bus in buses:
        if last_bus_id == bus["bus_id"]:
            time_format = "%H:%M"
            datetime1 = datetime.strptime(last_time, time_format)
            datetime2 = datetime.strptime(bus["a_time"], time_format)
            if datetime1 >= datetime2:
                errors.append((bus["bus_id"], bus["stop_name"]))

            last_time = bus["a_time"]
        else:
            last_bus_id = bus["bus_id"]
            last_time = bus["a_time"]

    if len(errors) == 0:
        print("OK")
    else:
        for bus_id, stop_name in errors:
            print(f"bus_id line {bus_id}: wrong time on station {stop_name}")


if __name__ == "__main__":
    data = input()
    buses = json.loads(data)
    check_stops_types(buses)
