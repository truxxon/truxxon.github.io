import base64
from flask import Blueprint, render_template, request, flash, redirect, url_for, Response, session
from . forms import CommissionForm, PortfolioForm
from . models import Commission, Portfolio
from . import db
from markupsafe import escape
from os import getenv

PASSWORD = getenv("GAIYA_PROTECTED_PASSWORD")  # Change this to your desired password

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("home.html")

@views.route("/portfolio")
def portfolio():
    portfolio = Portfolio.query.all()  # Fetch all artwork from the database
    return render_template("portfolio.html", portfolio=portfolio)  # Pass the data to the template

@views.route("/image/<int:art_id>")
def serve_image(art_id):
    item = Portfolio.query.get_or_404(art_id)  # Get the image by IDA
    if item.artwork:  #  If artwork exists, serve it
        return Response(item.artwork, mimetype="image/jpeg")  
    return "No Image", 404  # Return 404 if no image is found

@views.route("/commission", methods=['GET', 'POST'])
def commission():
    form = CommissionForm()  # Create form instance
    if request.method == "POST" and form.validate_on_submit():
        new_commission = Commission(
            email=escape(form.email.data),
            request=escape(form.request.data),
            questions=escape(form.questions.data),
            deadline=form.deadline.data)
        db.session.add(new_commission)
        db.session.commit()
        return render_template("request_success.html")  # Prevents resubmission
    return render_template("commission.html", form=form)  # Passes form to template

@views.route("/logout")
def logout():
    session.pop("authenticated", None)  # Remove authentication
    return redirect(url_for("views.login"))

@views.route("/login", methods=["GET", "POST"])
def login():
    next_page = request.args.get("next")  
    if request.method == "POST":
        if request.form["password"] == PASSWORD:
            session["authenticated"] = True  # Store in session
            # return redirect(url_for("views.view_requests"))
            return redirect(next_page or url_for("views.home"))
        else:
            return render_template("login_failed.html")
    return render_template("login.html")

@views.route("/view_requests")
def view_requests():
    if not session.get("authenticated"):
        return redirect(url_for("views.login", next=(url_for("views.view_requests"))))  # Redirect if not logged in
    commission = Commission.query.all() 
    return render_template("view_requests.html", commission=commission)

@views.route("/portfolio_add", methods=['GET', 'POST'])
def portfolio_add():
    if not session.get("authenticated"):
        return redirect(url_for("views.login", next=(url_for("views.portfolio_add"))))  # Redirect if not logged in
    form = PortfolioForm()  # Create form instance
    if request.method == "POST" and form.validate_on_submit():
        artwork_file = form.artwork.data  # Get the file
        if artwork_file:
            artwork_bytes = artwork_file.read()  # Convert FileStorage to bytes
        else:
            artwork_bytes = None  # Handle case where no image is uploaded
        new_portfolio = Portfolio(
            title =escape(form.title.data),
            product_type =form.product_type.data,
            artwork = artwork_bytes )
        db.session.add(new_portfolio)
        db.session.commit()
        return redirect(url_for("views.portfolio"))  # Prevents resubmission
    return render_template("portfolio_add.html", form=form)  # Passes form to template

@views.route("/about")
def about():
    return render_template("about.html")

