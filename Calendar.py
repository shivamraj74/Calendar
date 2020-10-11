import PySimpleGUI as sg

sg.theme('DarKAmber')
layout = [[sg.CalendarButton('Click here to see the date',  target='-IN4-', format='%m-%d', default_date_m_d_y=(1,None,2020), )],
      [sg.Button('Date Popup'), sg.Exit()]]

window = sg.Window('AK calendar',layout,no_titlebar=False)

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Date Popup':
        sg.popup('You chose:', sg.popup_get_date())
window.close()
