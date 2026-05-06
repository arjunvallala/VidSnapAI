from flask import Flask, render_template, request
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create uploads folder if not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create", methods=["GET", "POST"])
def create():
    myid = str(uuid.uuid4())

    if request.method == "POST":
        uid = request.form.get("uuid")
        text = request.form.get("text")

        save_path = os.path.join(app.config['UPLOAD_FOLDER'], uid)

        # Create folder for this UUID
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        input_files =[]
        for key in request.files:
            file = request.files[key]
            input_files.append(file.filename)
            if file and file.filename != "":
                file_path = os.path.join(save_path, file.filename)
                file.save(file_path)
                with open(os.path.join(app.config['UPLOAD_FOLDER'], uid,"desc.txt"),"w") as f:
                    f.write(text)
        for fl in input_files :
            with open(os.path.join(app.config['UPLOAD_FOLDER'], uid,"input.txt"),"a") as f:
                f.write(f"file '{fl}'\nduration 2\n")
    return render_template("create.html", myid=myid)


@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    return render_template("gallery.html",reels = reels)

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)