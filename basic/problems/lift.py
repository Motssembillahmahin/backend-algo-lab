def main():
    t = int(input())
    fixed_distance = (
        19  # door open(3) + enter(5) + door close(3) + door open(3) + exit(5)
    )
    for case_num in range(1, t + 1):
        pos, left_pos = map(int, input().split())
        lift_travel_time_to_user = abs(pos - left_pos) * 4
        lift_travel_time_to_ground = pos * 4
        total_time = (
            lift_travel_time_to_user + lift_travel_time_to_ground + fixed_distance
        )
        print(f"Case {case_num}: {total_time}")


main()
