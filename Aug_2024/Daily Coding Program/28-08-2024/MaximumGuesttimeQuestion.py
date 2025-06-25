# """There was a party.there was a log register in which entry and exit time of all the guests was logged.
# you have to tell the time at which there was maximum guest in the party.
# input will be the entry and exit time of all the n guests.share the approach to solve this

def find_max_guests(entry_times,exit_times):
    events = []
    for entry in entry_times:
        events.append((entry,"entry"))
    for exit in exit_times:
        events.append((exit,"exit"))

    events.sort(key=lambda x: (x[0],x[1] == 'entry'))

    max_guests = 0
    current_guests = 0
    time_of_max_guest = 0

    for time, event_type in events:
        if event_type == 'entry':
            current_guests += 1
            if current_guests > max_guests:
                max_guests = current_guests
                time_of_max_guest = time
            else:
                current_guests -= 1

    return time_of_max_guest, max_guests


entry_times = [1,10,8,11,5]
exit_times = [4,6,12,9,7]

time, max_guest = find_max_guests(entry_times,exit_times)
print(f"The maximum number of guest was {max_guest} at the time {time}.")