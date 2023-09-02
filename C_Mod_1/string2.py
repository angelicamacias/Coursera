#!user/bin/env python3
def replace_date(schedule, old_date, new_date):
    if schedule.endswith(old_date):
        p = len(old_date)
        new_schedule = schedule[:-p] #+ schedule[-p:].replace(old_date, new_date)
        print(new_schedule)

print(replace_date("Last year’s annual report will be released in March 2023", "2023", "2024"))