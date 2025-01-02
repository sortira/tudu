from flask import Flask, request, redirect, render_template, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import firebase_admin
from firebase_admin import credentials, firestore
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(24)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

class User(UserMixin):
    def __init__(self, id, password=None):
        self.id = id
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    user_doc = db.collection("users").document(user_id).get()
    if user_doc.exists:
        user_data = user_doc.to_dict()
        user = User(user_id, user_data.get("password"))
        user.username = user_data.get("username")
        return user
    return None

# Routes
@app.route("/")
def home():
    if current_user.is_authenticated:
        user_tasks_doc = db.collection("todos").document(current_user.id).get()
        tasks = user_tasks_doc.to_dict().get("tasks", []) if user_tasks_doc.exists else []
        return render_template("home.html", tasks=tasks, user=current_user)
    return render_template("home.html", user=current_user)

@app.route("/add_todo", methods=["POST"])
@login_required
def add_todo():
    task = request.form.get("todo", "").strip()
    if not task:
        flash("Task cannot be empty.", "danger")
        return redirect(url_for("home"))

    # Add task to Firestore
    user_doc = db.collection("todos").document(current_user.id)
    user_doc.set({"tasks": firestore.ArrayUnion([task])}, merge=True)
    flash("Task added successfully.", "success")
    return redirect(url_for("home"))

@app.route("/delete_todo/<int:task_id>", methods=["POST"])
@login_required
def delete_todo(task_id):
    user_doc = db.collection("todos").document(current_user.id)
    user_tasks = user_doc.get().to_dict().get("tasks", [])
    
    # Validate task index
    if 0 <= task_id < len(user_tasks):
        task_to_remove = user_tasks[task_id]
        # Remove task from Firestore
        user_doc.set({"tasks": firestore.ArrayRemove([task_to_remove])}, merge=True)
        flash("Task deleted successfully.", "success")
    else:
        flash("Invalid task ID.", "danger")
    
    return redirect(url_for("home"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        user_doc = db.collection("users").document(email).get()
        if user_doc.exists:
            user_data = user_doc.to_dict()
            if user_data.get("password") == password:
                user = User(email, password)
                login_user(user, remember=True)
                flash("Logged in successfully.", "success")
                return redirect(url_for("home"))
            else:
                flash("Invalid password.", "danger")
        else:
            flash("User not found.", "danger")
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        username = request.form["username"]
        user_doc = db.collection("users").document(email).get()
        if user_doc.exists:
            flash("User already exists.", "warning")
        else:
            db.collection("users").document(email).set({"password": password, "username": username})
            flash("Account created successfully. Please log in.", "success")
            return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.", "success")
    return redirect(url_for("home"))

# Protected Route Example
@app.route("/dashboard")
@login_required
def dashboard():
    return f"Welcome to your dashboard, {current_user.id}!"

if __name__ == "__main__":
    app.run(debug=True)
