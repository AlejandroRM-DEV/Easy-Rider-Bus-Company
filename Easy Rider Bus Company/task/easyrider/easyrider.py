import json
import re


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


if __name__ == "__main__":
    data = input()
    buses = json.loads(data)
    check_errors(buses)
