from tkinter import *


def move_start(event):
    widget = event.widget
    if widget == canvas or widget == playground:  # this thing allows to move ONLY player
        return 0
    else:
        widget.start_x = event.x
        widget.start_y = event.y


def move_player(event):
    try:
        widget = event.widget
        x = widget.winfo_x() - widget.start_x + event.x
        y = widget.winfo_y() - widget.start_y + event.y
        widget.place(x=x, y=y)

        if x < 0 or y < 0 or x + 20 > 491 or y + 20 > 491:  # can't go over the playground
            print('GAME OVER!')
            quit()

        for i in dangers:
            if (x + 20 >= i[0] and x <= i[2]) and (y + 20 >= i[1] and y <= i[3]):  # can't touch black rectangles
                print('GAME OVER!')
                quit()
            else:
                continue

    except AttributeError:
        print("You can click only at objects!")


if __name__ == '__main__':
    window = Tk()
    
    window.geometry('512x512')
    
    playground = Frame(window, bd=10, relief=RAISED, height=512, width=512)
    playground.pack()
    
    canvas = Canvas(playground, height=512, width=512)
    
    player = Label(playground, bg='red', width=2, height=1)
    player.place(x=0, y=0)
    
    dangers = [(50, 0, 70, 256), (120, 256, 140, 512), (190, 0, 210, 256), (260, 256, 280, 512),
               (330, 0, 350, 256), (400, 256, 420, 512)]
    
    canvas.create_rectangle(dangers[0], fill='#000000')
    canvas.create_rectangle(dangers[1], fill='#000000')
    canvas.create_rectangle(dangers[2], fill='#000000')
    canvas.create_rectangle(dangers[3], fill='#000000')
    canvas.create_rectangle(dangers[4], fill='#000000')
    canvas.create_rectangle(dangers[5], fill='#000000')
    
    window.bind('<Button-1>', move_start)
    window.bind('<B1-Motion>', move_player)
    
    canvas.pack()
    
    window.mainloop()
