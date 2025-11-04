import pyautogui as p
import time
import datetime
import sys
from icecream import ic

def parse_end_time(time_str: str):
    """
    Parses a time string (HH:MM) and returns the corresponding datetime object for today.
    If the time has already passed today, it assumes the next day.

    Returns None if the input is empty (run indefinitely).
    """
    if not time_str:
        return None  # Run indefinitely if no input is given

    try:
        now = datetime.datetime.now()
        end_time = datetime.datetime.strptime(time_str, "%H:%M").replace(year=now.year, month=now.month, day=now.day)

        # If the time has already passed today, assume it's for the next day
        if end_time < now:
            end_time += datetime.timedelta(days=1)

        return end_time
    except ValueError:
        ic("Invalid time format. Please enter time as HH:MM.")
        sys.exit(1)  # Exit with error

def run_script(end_time=None):
    """
    Runs the script until the specified end time (datetime object).
    If no end time is provided, it runs indefinitely.

    The script presses 'junja', moves the mouse slightly, and logs activity.
    """
    start_time = datetime.datetime.now()
    p.FAILSAFE = False  # Prevent script interruption due to PyAutoGUI failsafe

    ic(f"Script started at {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    if end_time:
        ic(f"Will run until {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        ic("Running indefinitely until manually stopped (CTRL+C).")

    step = 0
    while True:
        if end_time and datetime.datetime.now() >= end_time:
            ic("Reached the specified end time. Stopping script.")
            break

        p.press('junja')
        p.moveRel(0, 1)
        time.sleep(5)
        p.moveRel(0, -1)
        p.press('junja')

        now = datetime.datetime.now()
        ic(f"Step {step} at {now.strftime('%Y-%m-%d %H:%M:%S')}")

        step += 1
        time.sleep(120)  # Wait for 2 minutes before next action

    ic("Script execution finished.")

if __name__ == "__main__":
    # Check if a time was provided as a command-line argument
    end_time = None
    if len(sys.argv) > 1:
        end_time = parse_end_time(sys.argv)
    else:
        user_input = input("Enter end time (HH:MM) or press Enter to run indefinitely: ").strip()
        end_time = parse_end_time(user_input)

    run_script(end_time)
