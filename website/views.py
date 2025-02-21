from flask import Blueprint, render_template, request, flash, redirect, url_for
from . forms import CommissionForm
from . models import Commission
from . import db


views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("home.html")

@views.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")



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
