## FocusTime

This is mainly a pomodoro app. There are 3 modes :
 - Pomodoro : you start with a work session that last for 25
 minutes followed by a 5-minute time break. Repeat that.
 - Todo : A simple todo list. 
 - Tracker : track the number of pomodoro sessions you have each day on a graph

Dependencies for this projects : `pyqt6`,`pyqtgraph` and `playsound`
(Note that I used `playsound` because I'm experiencing a bug with QtMultimedia)
The data is saved in `data.json`

Here is a screenshot of the app:

![screenshot of the app](https://media.discordapp.net/attachments/906215316730814557/954781501835341885/unknown.png?width=748&height=481 "Screenshot of the app")

This is version 1.0.0. 
Upcoming features:
 - Tags for to-do
 - Assign a session with a task, track the number of time spend on that task