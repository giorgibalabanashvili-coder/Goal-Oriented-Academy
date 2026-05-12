def meeting(s):
    guests = s.upper().split(';')
    formatted_guests = []
    for guest in guests:
        first, last = guest.split(':')
        formatted_guests.append((last, first))
    formatted_guests.sort()
    result = "".join(f"({last}, {first})" for last, first in formatted_guests)
    return result