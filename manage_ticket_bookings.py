def book_seat(booked, seat):
    if seat in booked:
        print("Seat already booked")
    else:
        booked.append(seat)

def cancel_seat(booked, seat):
    if seat in booked:
        booked.remove(seat)

def available_seats(total, booked):
    return [i for i in range(1, total + 1) if i not in booked]

total_seats = 10
booked_seats = [2, 5, 7]
book_seat(booked_seats, 3)
cancel_seat(booked_seats, 5)
print("Available seats:", available_seats(total_seats, booked_seats))
