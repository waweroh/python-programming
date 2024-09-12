import main_func
import FreeSimpleGUI as sg

label = sg.Text('Type in a todo')
input_box = sg.InputText(tooltip='enter todo')
add_button = sg.Button('Add')


window = sg.Window('My-todo', layout=[[label], [input_box, add_button]])#list of gui instances ie input label and add button.
window.read()
window.close()