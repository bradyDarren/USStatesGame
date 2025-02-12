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
user_answer = screen.textinput(title=f'Guess the state: {correct}/50', prompt="Input any name of the 50 U.S. States:")

# # finds the coordinates of the mouse when it is clicked
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

user_answer = input('Input any name of the 50 U.S. States:')

# importing our csv file. 
states_data = pandas.read_csv('50_states.csv')

# seperate just the state column, and converting it into a list:
all_states = states_data['state']
states_list = all_states.to_list()

present = states_data[states_data['state'] == user_answer]
print(present.x.iloc[0])

screen.exitonclick()