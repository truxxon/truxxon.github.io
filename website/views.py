import base64
from flask import Blueprint, render_template, request, flash, redirect, url_for, Response
from . forms import CommissionForm, PortfolioForm
from . models import Commission, Portfolio
# from .models import Artwork
from . import db


views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("home.html")

@views.route("/portfolio")
def portfolio():
    portfolio = Portfolio.query.all()  # ✅ Fetch all artwork from the database
    return render_template("portfolio.html", portfolio=portfolio)  # ✅ Pass the data to the template

@views.route("/image/<int:art_id>")
def serve_image(art_id):
    item = Portfolio.query.get_or_404(art_id)  # ✅ Get the image by ID

    if item.artwork:  # ✅ If artwork exists, serve it
        return Response(item.artwork, mimetype="image/jpeg")  # ✅ Adjust MIME type if needed

    return "No Image", 404  # ✅ Return 404 if no image is found

@views.route("/shop", methods=['GET', 'POST'])
def shop():
    form = CommissionForm()  # ✅ Create form instance

    if request.method == "POST" and form.validate_on_submit():
        new_commission = Commission(
            email=form.email.data,
            request=form.request.data,
            questions=form.questions.data,
            deadline=form.deadline.data
        )
        db.session.add(new_commission)
        db.session.commit()
        flash("Your request has been submitted!", "success")
        return redirect(url_for("views.shop"))  # Prevents resubmission

    return render_template("shop.html", form=form)  # ✅ Passes form to template

@views.route("/portfolio_add", methods=['GET', 'POST'])
def portfolio_add():
    form = PortfolioForm()  # ✅ Create form instance

    if request.method == "POST" and form.validate_on_submit():
        artwork_file = form.artwork.data  # ✅ Get the file

        if artwork_file:
            artwork_bytes = artwork_file.read()  # ✅ Convert FileStorage to bytes
        else:
            artwork_bytes = None  # ✅ Handle case where no image is uploaded

        new_portfolio = Portfolio(
            title =form.title.data,
            style =form.style.data,
            product_type =form.product_type.data,
            artwork = artwork_bytes 
        )
        db.session.add(new_portfolio)
        db.session.commit()
        return redirect(url_for("views.portfolio"))  # Prevents resubmission

    return render_template("portfolio_add.html", form=form)  # ✅ Passes form to template

@views.route("/about")
def about():
    return render_template("about.html")


# @views.route('/commission', methods=['GET', 'POST'])
# def commission_request():
#     form = CommissionForm()
#     if form.validate_on_submit():  # Checks if form is submitted & valid
#         new_commission = Commission(email=form.email.data, details=form.details.data)
#         db.session.add(new_commission)  # Add to database
#         db.session.commit()  # Save changes
#         flash("Your commission request has been submitted!", "success")
#         return redirect(url_for('views.commission_request'))  # Reload page after submission

#     return render_template("commission.html", form=form)
