import turtle
from turtle import Screen
import json
import time

#|------------------------------UI--------------------------------------|
screen = Screen()
screen.title("European Country Quiz")
image = "map.gif"
screen.addshape(image)
turtle.shape(image)
score = 0

#|------------------------------Mechanism----------------------------------|
eu_countries = [
    "Albania", "Andorra", "Austria", "Belarus", "Belgium",
    "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czech Republic",
    "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece",
    "Hungary", "Iceland", "Ireland", "Italy", "Kosovo", "Latvia", "Lithuania", "Luxembourg", "Malta", "Moldova",
    "Monaco",
    "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal",
    "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain",
    "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom"
]

with open("data.json", mode="r") as data_file:
    data = json.load(data_file)


#|------------------------------Timed Mode----------------------------------|
def start_timer(duration):
    """Start the timer for the quiz based on the selected difficulty."""
    start_time = time.time()
    end_time = start_time + duration
    return start_time, end_time


def check_time_remaining(end_time):
    """Check if the time is up."""
    current_time = time.time()
    return current_time < end_time


def update_timer_display(start_time, end_time):
    """Update the timer display on the screen."""
    remaining_time = int(end_time - time.time())
    minutes, seconds = divmod(remaining_time, 60)
    timer_turtle.clear()
    timer_turtle.write(f"Time Left: {minutes}:{seconds:02d}", align="center", font=("Arial", 14, "bold"))


#|------------------------------Game Setup----------------------------------|
unanswered_countries = [item for item in eu_countries]
answered_countries = []


def display_unanswered():
    """Display all unanswered countries in a different color."""
    for country in unanswered_countries:
        x_cord = data[country]["x"]
        y_cord = data[country]["y"]
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.color("red")  # Highlight in red
        t.goto(x_cord, y_cord)
        t.write(arg=country, font=("Arial", 10, "bold"))


#|------------------------------Difficulty Selection----------------------------------|
difficulty = screen.textinput(
    title="Select Difficulty",
    prompt="Choose a difficulty: Easy (15min), Medium (10min), Hard (7min)"
).lower()

if difficulty == "easy":
    time_limit = 15 * 60
elif difficulty == "medium":
    time_limit = 10 * 60
elif difficulty == "hard":
    time_limit = 7 * 60
else:
    screen.textinput(title="Invalid Choice", prompt="Please restart and choose Easy, Medium, or Hard.")
    screen.bye()

start_time, end_time = start_timer(time_limit)

#|------------------------------Timer Display----------------------------------|
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.goto(0, 250)
update_timer_display(start_time, end_time)

#|-----------------------------User Inputs------------------------------------|
while len(answered_countries) < 46:
    if not check_time_remaining(end_time):
        screen.textinput(title="Time's Up!", prompt="Time's up! Press OK to see unanswered countries.")
        display_unanswered()
        break

    update_timer_display(start_time, end_time)

    user_answer = screen.textinput(
        title=f"{score}/46 European Countries",
        prompt="What is another European country?"
    )

    if user_answer == "Exit":
        display_unanswered()
        screen.bye()
        break

    if user_answer:
        user_answer = user_answer.title()

    for country in data:
        if user_answer == country and user_answer not in answered_countries:
            x_cord = data[user_answer]["x"]
            y_cord = data[user_answer]["y"]
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            t.goto(x_cord, y_cord)
            t.write(arg=country, font=("Arial", 10, "normal"))
            answered_countries.append(country)
            unanswered_countries.remove(country)
            score += 1

screen.mainloop()
