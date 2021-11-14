def on_button_pressed_a():
    global br, brojac
    br = randint(0, 2)
    list2[brojac] = br
    basic.show_number(br)
    brojac += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global br2
    index = 0
    while index <= brojac - 1:
        basic.show_number(list2[br2])
        br2 += 1
        basic.pause(100)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.pause(100)
        index += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

br2 = 0
brojac = 0
list2: List[number] = []
br = 0
br = 0
list2 = []
brojac = 0
br2 = 0