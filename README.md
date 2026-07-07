# smart-alarm
The Smart Alarm Clock is a desktop application developed using Python, Tkinter, and Pygame. Unlike a traditional digital clock, this application allows users to schedule multiple alarms, receive an audible notification when an alarm is triggered, snooze alarms for five minutes, and maintain a history of previously activated alarms.
# ⏰ Smart Alarm Clock

A Smart Alarm Clock developed in Python using Tkinter and Pygame. The application allows users to set multiple alarms, snooze alarms, stop alarms, and monitor upcoming alarms through a simple and attractive graphical interface.

---

## Features

- Real-time digital clock
- Displays current date
- Set multiple alarms
- Alarm history tracking
- Snooze alarm for 5 minutes
- Stop alarm functionality
- Audio notification using MP3
- User-friendly graphical interface
- Multithreaded alarm monitoring
- Lightweight desktop application

---

## Technologies Used

- Python 3.x
- Tkinter
- Pygame
- Threading
- Datetime
- Time

---

## Project Structure

```
Smart Alarm Clock/
│
├── alarm_clock.py
├── alarm.mp3
├── requirements.txt
├── README.md
└── screenshots/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/kamal1913jeet/smart-alarm
```

Move into the project folder

```bash
cd Smart-Alarm-Clock
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python alarm_clock.py
```

---

## How It Works

1. Launch the application.
2. The current time and date are displayed automatically.
3. Select Hour, Minute, and Second.
4. Click **Set Alarm**.
5. The alarm is added to the Upcoming Alarm list.
6. When the current system time matches the alarm time:
   - Alarm sound starts.
   - Status changes to **WAKE UP!**
   - Alarm is added to History.
7. Click **Stop Alarm** to stop the sound.
8. Click **Snooze** to postpone the alarm by five minutes.

---

## Libraries Used

| Library | Purpose |
|----------|----------|
| tkinter | GUI Development |
| pygame | Alarm Sound |
| datetime | Date & Time Handling |
| threading | Background Alarm Monitoring |
| time | Real-Time Clock |

---

## Future Improvements

- Custom alarm tones
- Dark and Light themes
- Alarm repetition (Daily/Weekly)
- Delete alarm option
- Volume control
- Notifications
- Calendar integration
- Voice commands
- Reminder notes
- Stopwatch and Timer

---

## Learning Outcomes

This project helped in understanding:

- Python GUI Development
- Event-Driven Programming
- Multithreading
- Audio Playback
- Time Manipulation
- Desktop Application Development
- Exception Handling

---

## Author

**Kamaljeet Kaur**

Python Developer | Data Analytics Enthusiast

---

## License

This project is developed for educational and learning purposes.
