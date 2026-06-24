from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/certificates")
def certificates():
    return render_template("certificates.html")

@app.route("/roadmaps")
def roadmaps():
    return render_template("roadmaps.html")

@app.route("/jobs")
def jobs():
    return render_template("jobs.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/career")
def career():
    return render_template("career.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

if __name__ == "__main__":
    app.run(debug=True)