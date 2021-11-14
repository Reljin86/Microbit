input.onButtonPressed(Button.A, function () {
    br = randint(0, 2)
    list[brojac] = br
    basic.showNumber(br)
    brojac += 1
})
input.onButtonPressed(Button.B, function () {
    for (let index = 0; index <= brojac - 1; index++) {
        basic.showNumber(list[br2])
        br2 += 1
        basic.pause(100)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.pause(100)
    }
})
let br2 = 0
let brojac = 0
let list: number[] = []
let br = 0
br = 0
list = []
brojac = 0
br2 = 0
