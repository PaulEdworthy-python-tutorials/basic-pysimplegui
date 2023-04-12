import PySimpleGUI as sg

sg.theme('Default1')

layout = [
    [sg.Text('Text here')],
    [sg.Text('Enter text'), sg.InputText()],
    [sg.Button('OK'), sg.Button('Cancel')]
]

# text
window = sg.Window('Title here', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('You entered:', values[0])

window.close()