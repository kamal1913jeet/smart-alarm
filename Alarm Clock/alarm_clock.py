import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import threading
import time
import pygame

# ==========================
# INITIALIZATION
# ==========================

pygame.mixer.init()

root = tk.Tk()
root.title("Smart Alarm Clock")
root.geometry("700x550")
root.configure(bg="#1E1E2F")
root.resizable(False, False)

alarms = []
alarm_running = False

# ==========================
# CLOCK UPDATE
# ==========================
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("")

    return os.path.join(base_path, relative_path)
def update_clock():
    current_time = time.strftime("%I:%M:%S %p")
    current_date = time.strftime("%d %B %Y")

    clock_label.config(text=current_time)
    date_label.config(text=current_date)

    root.after(1000, update_clock)

# ==========================
# SET ALARM
# ==========================

def add_alarm():

    alarm_time = (
        f"{hour_var.get()}:"
        f"{minute_var.get()}:"
        f"{second_var.get()}"
    )

    alarms.append(alarm_time)

    alarm_listbox.insert(tk.END, alarm_time)

    status_label.config(
        text=f"Alarm Added : {alarm_time}",
        fg="lightgreen"
    )

# ==========================
# STOP ALARM
# ==========================

def stop_alarm():

    pygame.mixer.music.stop()

    status_label.config(
        text="Alarm Stopped",
        fg="orange"
    )

# ==========================
# SNOOZE ALARM
# ==========================

def snooze_alarm():

    future_time = (
        datetime.datetime.now()
        + datetime.timedelta(minutes=5)
    )

    new_alarm = future_time.strftime("%H:%M:%S")

    alarms.append(new_alarm)

    alarm_listbox.insert(
        tk.END,
        f"Snooze -> {new_alarm}"
    )

    pygame.mixer.music.stop()

    status_label.config(
        text=f"Snoozed Until {new_alarm}",
        fg="cyan"
    )

# ==========================
# ALARM CHECKER
# ==========================

def alarm_checker():

    global alarm_running

    while True:

        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        for alarm in alarms:

            if current_time == alarm:

                if not alarm_running:

                    alarm_running = True

                    status_label.config(
                        text="WAKE UP!",
                        fg="red"
                    )

                    try:
                        pygame.mixer.music.load(resource_path("alarm.mp3"))
                        pygame.mixer.music.play(-1)

                    except:
                        messagebox.showerror(
                            "Error",
                            "alarm.mp3 not found"
                        )

                    history_listbox.insert(
                        tk.END,
                        f"Triggered : {alarm}"
                    )

        time.sleep(1)

# ==========================
# START THREAD
# ==========================

threading.Thread(
    target=alarm_checker,
    daemon=True
).start()

# ==========================
# HEADER
# ==========================

title_label = tk.Label(
    root,
    text="SMART ALARM CLOCK",
    font=("Segoe UI", 24, "bold"),
    bg="#1E1E2F",
    fg="#00FF99"
)

title_label.pack(pady=10)

clock_label = tk.Label(
    root,
    font=("Segoe UI", 34, "bold"),
    bg="#1E1E2F",
    fg="white"
)

clock_label.pack()

date_label = tk.Label(
    root,
    font=("Segoe UI", 14),
    bg="#1E1E2F",
    fg="lightgray"
)

date_label.pack(pady=5)

# ==========================
# TIME FRAME
# ==========================

time_frame = tk.Frame(
    root,
    bg="#1E1E2F"
)

time_frame.pack(pady=20)

hours = [f"{i:02}" for i in range(24)]
minutes = [f"{i:02}" for i in range(60)]
seconds = [f"{i:02}" for i in range(60)]

hour_var = tk.StringVar(value="00")
minute_var = tk.StringVar(value="00")
second_var = tk.StringVar(value="00")

ttk.Combobox(
    time_frame,
    textvariable=hour_var,
    values=hours,
    width=5
).grid(row=0, column=0, padx=10)

ttk.Combobox(
    time_frame,
    textvariable=minute_var,
    values=minutes,
    width=5
).grid(row=0, column=1, padx=10)

ttk.Combobox(
    time_frame,
    textvariable=second_var,
    values=seconds,
    width=5
).grid(row=0, column=2, padx=10)

# ==========================
# BUTTONS
# ==========================

button_frame = tk.Frame(
    root,
    bg="#1E1E2F"
)

button_frame.pack()

tk.Button(
    button_frame,
    text="Set Alarm",
    command=add_alarm,
    bg="#00AA55",
    fg="white",
    width=12
).grid(row=0, column=0, padx=10)

tk.Button(
    button_frame,
    text="Stop Alarm",
    command=stop_alarm,
    bg="#CC3333",
    fg="white",
    width=12
).grid(row=0, column=1, padx=10)

tk.Button(
    button_frame,
    text="Snooze 5 Min",
    command=snooze_alarm,
    bg="#3366FF",
    fg="white",
    width=12
).grid(row=0, column=2, padx=10)

# ==========================
# STATUS
# ==========================

status_label = tk.Label(
    root,
    text="No Alarm Set",
    font=("Segoe UI", 12, "bold"),
    bg="#1E1E2F",
    fg="yellow"
)

status_label.pack(pady=10)

# ==========================
# LISTS
# ==========================

list_frame = tk.Frame(
    root,
    bg="#1E1E2F"
)

list_frame.pack(pady=10)

alarm_frame = tk.Frame(list_frame)
alarm_frame.grid(row=0, column=0, padx=20)

tk.Label(
    alarm_frame,
    text="Upcoming Alarms",
    font=("Segoe UI", 12, "bold")
).pack()

alarm_listbox = tk.Listbox(
    alarm_frame,
    width=25,
    height=8
)

alarm_listbox.pack()

history_frame = tk.Frame(list_frame)
history_frame.grid(row=0, column=1, padx=20)

tk.Label(
    history_frame,
    text="Alarm History",
    font=("Segoe UI", 12, "bold")
).pack()

history_listbox = tk.Listbox(
    history_frame,
    width=25,
    height=8
)

history_listbox.pack()

# ==========================
# START CLOCK
# ==========================

update_clock()

root.mainloop()