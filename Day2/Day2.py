def is_safe(report):
    increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def is_safe_with_dampener(report):
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if is_safe(new_report):
            return True
    return False

def count_safe_reports(filename):
    safe_count_part1 = 0
    safe_count_part2 = 0
    with open(filename, 'r') as file:
        for line in file:
            report = list(map(int, line.strip().split()))
            if is_safe(report):
                safe_count_part1 += 1
                safe_count_part2 += 1
            elif is_safe_with_dampener(report):
                safe_count_part2 += 1
    return safe_count_part1, safe_count_part2

# Main Execution
filename = "data.txt"
part1, part2 = count_safe_reports(filename)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
