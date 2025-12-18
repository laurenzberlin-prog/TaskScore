from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    """Startseite mit kurzer Erklärung und Navigation."""
    return render_template("home.html")


@app.route("/tasks")
def show_tasks():
    """
    Übersicht über Aufgaben.
    Im aktuellen Prototyp sind hier noch keine echten Daten angebunden.
    """
    aufgaben = []  # wird später aus Datenbank oder Formular befüllt
    return render_template("tasks.html", tasks=aufgaben)


@app.route("/plan")
def weekly_plan():
    """
    Wochenübersicht für die Punkteplanung.
    Aktuell nur Struktur – Logik folgt in einer späteren Iteration.
    """
    wochenpunkte = {}  # z.B. {"Montag": 30, ...} – kommt später
    return render_template("plan.html", weekly_points=wochenpunkte)


@app.route("/progress")
def progress():
    """
    Zeigt den aktuellen Fortschritt.
    Derzeit sind nur Platzhalterwerte hinterlegt.
    """
    total_points = 0
    done_points = 0
    return render_template(
        "progress.html",
        total_points=total_points,
        done_points=done_points,
    )


if __name__ == "__main__":
    app.run(debug=True)
