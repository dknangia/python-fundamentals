current_movies = {'The Grinch': '11:00am',
                  'Rudoph':'1:00pm',
                  'Frosty the Snowman': '3:00pm',
                  'Christmas Vacation':'5:30pm'}

print("We are currently showing the following movies")
for movie in current_movies:
    print(movie)
    
user_input = input("What movie would you like the showtime for?\n")

showtime = current_movies.get(user_input)
if showtime == None:
    print("The requested move is not playing")
else:
    print(user_input ,"is showing at ", showtime)

