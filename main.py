# Initialize 2D list to store seat data
seats = [
  [False,False,False,False,False,False,False,False],
  [False,False,False,False,False,False,False,False],
  [False,False,False,False,False,False,False,False],
  [False,False,False,False,False,False,False,False],
  [False,False,False,False,False,False,False,False]
]

def book_single_seat(row, col):
  if seats[row][col]:
    print('Sorry, seat', col, 'in row', row, 'is taken')
  else: # Seat is free!
    seats[row][col] = True
    print('Great! We reserved seat', col, 'in row', row, 'for you')

def book_backrow_seat():
  back_row = seats[-1]

  for i, taken in enumerate(back_row):
    if not(taken):
      back_row[i] = True
      print('Great! We reserved back row seat', i, 'for you')
      return

  print('Sorry, the entire back row is full')

def book_multiple_seats(row, num_seats):
  start = 0
  end = num_seats

  all_free = [False]*num_seats
  all_taken = [True]*num_seats

  while end <= len(seats[row]):
    if seats[row][start:end] == all_free:
      seats[row][start:end] = all_taken
      print('Great! We reserved seats', start, 'through', end-1, 'in row', row, 'for you!')
      return

    start += 1
    end += 1

  print('Sorry, we were unable to book', num_seats, 'tickets in row', row)

def print_menu():
  print('* * * 🎟  Ticket Purchase Center 🎟 * * * ')
  print('1️⃣: Book a single seat')
  print('2️⃣: Book a back row seat')
  print('3️⃣: Book multiple seats in a row') # Stretch
  print('4️⃣: Exit')

def main():
  print_menu()

  while True:
    choice = int(input('\nSelect an option (1-4): '))

    if choice == 1: # Book a single seat
      row = int(input('Enter a row number (0-4): '))
      col = int(input('Enter a seat number (0-7): '))
      book_single_seat(row, col)

    elif choice == 2: # Book any backrow seat
      book_backrow_seat()

    elif choice == 3: # Book multiple seats in the same row
      row = int(input('Enter a row number (0-4): '))
      num_seats = int(input('Enter a number of seats (1-8): '))
      book_multiple_seats(row, num_seats)

    elif choice == 4: # Exit
      break
    
    else:
      print('Please enter a valid option.')

  print('Thank you for coming! Enjoy the show. 👋\n')

main()