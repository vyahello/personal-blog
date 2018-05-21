from server.view.flashes import BlogFlash
from server.view.forms import RegistrationForm, LoginForm
from server.view.posts import BlogPost
from server.view.redirects import BlogRedirect
from server.view.templates import BlogTemplatePosts, BlogTemplate
from server.view.urls import BlogUrlFor
from server.storage.models import User, Post
from server import blog, bcrypt, db
from flask_login import login_user, current_user, logout_user, login_required
from flask import request


@blog.route('/')
@blog.route('/home')
def home():
    return BlogTemplatePosts('home.html').render(BlogPost())


@blog.route('/about')
def about():
    return BlogTemplate('about.html').render(title='About')


@blog.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return BlogRedirect(BlogUrlFor('home')).link()
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pass)
        db.create_all()
        db.session.add(user)
        db.session.commit()
        BlogFlash('Your account has been created!', 'success').display()
        return BlogRedirect(BlogUrlFor('login')).link()
    return BlogTemplate('register.html').render(title='Register', form=form)


@blog.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return BlogRedirect(BlogUrlFor('home')).link()
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return BlogRedirect(BlogUrlFor(next_page if next_page else 'home')).link()
        else:
            BlogFlash('Login Unsuccessful. Please check email and password', 'danger').display()
    return BlogTemplate('login.html').render(title='Login', form=form)


@blog.route('/logout')
def logout():
    logout_user()
    return BlogRedirect(BlogUrlFor('home')).link()


@blog.route('/account')
@login_required
def account():
    return BlogTemplate('account.html').render(title='account')
