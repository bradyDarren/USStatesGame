import turtle
import pandas 

screen = turtle.Screen()
# sets title at the top of our window.
screen.title('U.S. States Game')

# added image as a shape within our Turtle class.
blank_states = 'blank_states_img.gif'
screen.addshape(blank_states)

turtle.shape(blank_states)
correct = 0 

# # finds the coordinates of the mouse when it is clicked
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# importing our csv file. 
states_data = pandas.read_csv('50_states.csv')

# seperate just the state column, and converting it into a list:
all_states = states_data['state']
states_list = all_states.to_list()

guessed_states = []

while correct != 50:
    user_answer = screen.textinput(title=f'Guess the state: {correct}/50', prompt="Input any name of the 50 U.S. States:").title().strip()

    if user_answer == 'Exit':
        missed_states = []
        # missed_states = [state for state in states_list if state not in guessed_states]
        for state in states_list: 
            if state not in guessed_states:
                missed_states.append(state)
        data = pandas.DataFrame(missed_states)
        data.to_csv('missed_states.csv')
        break

    if user_answer in states_list and user_answer not in guessed_states: 
        pen = turtle.Turtle()
        pen.hideturtle() 
        pen.penup()
        state_data = states_data[states_data['state']== user_answer]
        pen.goto(int(state_data['x']), int(state_data['y']))
        pen.pendown()
        pen.color('black')
        pen.write(user_answer)
        correct += 1
        guessed_states.append(user_answer)
    


