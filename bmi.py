# __________________ basic settings __________________
import tkinter as tk
from tkinter import messagebox as mb
# __________________ calculate BMI __________________
def calcute_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        height = height / 100

        if height <= 0:
            mb.showerror("خطا", "قد باید بیشتر از صفر باشد")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            status = "کم‌وزن (Underweight)"
            color = "blue"

        elif 18.5 <= bmi < 25:
            status = "نرمال (Normal)"
            color = "green"

        elif 25 <= bmi < 30:
            status = "اضافه وزن (Overweight)"
            color = "yellow"

        elif 30 <= bmi < 35:
            status = "چاقی درجه 1 (Obese)"
            color = "orange"

        elif 35 <= bmi < 40:
            status = "چاقی درجه 2 (Obese)"
            color = "red"

        else:
            status = "چاقی درجه 3 (Obese)"
            color = "maroon"

        normal_min = height ** 2 * 18.5
        normal_max = height ** 2 * 25

        normal_height = f"{normal_min:.2f} تا {normal_max:.2f}"

        label_result.config(
            text=f"BMI: {bmi:.2f}\n"
                 f"وضعیت: {status}\n"
                 f"وزن ایده‌آل بااین قد: {normal_height} کیلوگرم",
            fg=color
        )

    except ValueError:
        mb.showerror("خطا", "لطفاً فقط عدد وارد کنید")
# __________________ window __________________
window = tk.Tk()
window.geometry("500x300")
window.config(bg="lime")
# __________________ system of program __________________
label_bmi = tk.Label(
    window,
    text="محاسبه شاخص توده بدنی",
    font=("Vazir", 12, "bold")
)
label_bmi.pack()

label_weight = tk.Label(
    window,
    text="وزن خود را وارد کنید (مثلاً: 70)",
    font=("Vazir", 12),bg="cyan"
)
label_weight.pack()

entry_weight = tk.Entry(window,bg="cyan",font=("Vazir", 12))
entry_weight.pack()

label_height = tk.Label(
    window,
    text="قد خود را وارد کنید (مثلاً: 170)",
    font=("Vazir", 12),bg="olive"
)
label_height.pack()

entry_height = tk.Entry(window,bg="olive",font=("Vazir", 12))
entry_height.pack()

label_result = tk.Label(
    window,
    text="",
    font=("Vazir", 12, "bold")
)
btn_calcute = tk.Button(
    window,
    text="محاسبه کردن",
    command=calcute_bmi
)
btn_calcute.pack()
label_result.pack()

# __________________ mainloop __________________

window.mainloop()
