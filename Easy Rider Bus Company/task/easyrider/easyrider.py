import json
import re


def check_errors(buses):
    time_pattern = r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$'

    bus_id = 0
    stop_id = 0
    stop_name = 0
    next_stop = 0
    stop_type = 0
    a_time = 0

    for bus in buses:
        if not isinstance(bus["bus_id"], int):
            bus_id += 1

        if not isinstance(bus["stop_id"], int):
            stop_id += 1

        if not isinstance(bus["stop_name"], str) or len(bus["stop_name"]) <= 0:
            stop_name += 1

        if not isinstance(bus["next_stop"], int):
            next_stop += 1

        if isinstance(bus["stop_type"], str):
            if len(bus["stop_type"]) >= 1 and bus["stop_type"] not in ["S", "O", "F"]:
                stop_type += 1
        else:
            stop_type += 1

        if not isinstance(bus["a_time"], str) or not re.match(time_pattern, bus["a_time"]):
            a_time += 1

    total = bus_id+stop_id+stop_name+next_stop+stop_type+a_time
    print(f"Type and required field validation: {total} errors")
    print(f"bus_id: {bus_id}")
    print(f"stop_id: {stop_id}")
    print(f"stop_name: {stop_name}")
    print(f"next_stop: {next_stop}")
    print(f"stop_type: {stop_type}")
    print(f"a_time: {a_time}")


if __name__ == "__main__":
    data = input()
    buses = json.loads(data)
    check_errors(buses)
