from tkinter import *  # asterisk mean that you import all the classes from tkinter package
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
REPS = 0
CHECKMARK_COUNT = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer) #Stoppping the timer
    canvas.itemconfig(timer_text, text="00:00")
    Timer_label.config(text="Timer")
    Checkmarks_label.config(text="")
    global REPS
    REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        time = LONG_BREAK_MIN
        Timer_label.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        time = SHORT_BREAK_MIN
        Timer_label.config(text="Break", fg=PINK)
    else:
        time = WORK_MIN
        Timer_label.config(text="Work", fg=GREEN)

    count_down(time * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60) #number of minutes
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    if count_min == 0 and count_sec == "00":
        start_timer()

        checkmark_1 = " ✔ "
        checkmark_2 = " ✔ ✔"
        checkmark_3 = " ✔ ✔ ✔"
        if REPS % 2 == 0:
            global CHECKMARK_COUNT
            CHECKMARK_COUNT += 1
            print(CHECKMARK_COUNT)
            if CHECKMARK_COUNT == 3:
                Checkmarks_label.config(text=checkmark_3)
            elif CHECKMARK_COUNT == 2:
                Checkmarks_label.config(text=checkmark_2)
            elif CHECKMARK_COUNT == 1:
                Checkmarks_label.config(text=checkmark_1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # choose the photo by wrtiing path to him
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 33, "bold"))
canvas.grid(column=1, row=1)



Timer_label = Label(text="Timer", font=(FONT_NAME, 37, "bold"), bg=YELLOW, fg=GREEN)
Timer_label.grid(column=1, row=0)

Checkmarks_label = Label(font=(FONT_NAME, 18, "bold"), bg=YELLOW, fg=GREEN)
Checkmarks_label.grid(column=1, row=3)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
