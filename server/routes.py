from flask_wtf import FlaskForm
from server.storage.sessions import UserSession
from server.view.flashes import PageFlash
from server.view.forms import RegistrationForm, LoginForm
from server.view.posts import BlogPost
from server.view.redirects import PageRedirect
from server.view.requests import NextPageRequest
from server.view.templates import YFoxTemplatePosts, YFoxTemplate
from server.view.urls import PageUrlFor
from server.storage.models import User, Post
from server import blog, bcrypt, db
from flask_login import login_required
from server.view.requests import Request
from server.view.users import OrdinaryUser


@blog.route('/')
@blog.route('/home')
def home() -> str:
    return YFoxTemplatePosts('home.html').render(BlogPost())


@blog.route('/about')
def about() -> str:
    return YFoxTemplate('about.html').render(title='About')


@blog.route('/register', methods=['GET', 'POST'])
def register() -> str:
    if OrdinaryUser().authenticated():
        return PageRedirect(PageUrlFor('home')).link()
    form: FlaskForm = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass: str = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user: User = User(username=form.username.data, email=form.email.data, password=hashed_pass)
        UserSession(db).add(user)
        PageFlash(f'Your account has been created!'
                  f' You are now able to login with {user.username} username', 'success').display()
        return PageRedirect(PageUrlFor('login')).link()
    return YFoxTemplate('register.html').render(title='Register', form=form)


@blog.route('/login', methods=['GET', 'POST'])
def login() -> str:
    if OrdinaryUser().authenticated():
        return PageRedirect(PageUrlFor('home')).link()
    form: FlaskForm = LoginForm()
    if form.validate_on_submit():
        user: User = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            OrdinaryUser().login(user, form)
            next_page: Request = NextPageRequest('next').get()
            return PageRedirect(PageUrlFor(next_page if next_page else 'home')).link()
        else:
            PageFlash('Login Unsuccessful. Please check email and password', 'danger').display()
    return YFoxTemplate('login.html').render(title='Login', form=form)


@blog.route('/logout')
def logout() -> str:
    OrdinaryUser().logout()
    return PageRedirect(PageUrlFor('home')).link()


@blog.route('/account')
@login_required
def account() -> str:
    return YFoxTemplate('account.html').render(title='account')
