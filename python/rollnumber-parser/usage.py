from roll_number_parser import (
    parse_roll_number,
    get_batch_display,
    get_programme_display
)

if __name__ == "__main__":
    sample_roll = "BL.EN.U4EAC24041"

    parsed = parse_roll_number(sample_roll)
    print(parsed)
    print(get_batch_display(sample_roll))
    print(get_programme_display(sample_roll))
