from typing import Callable
from flask_login import login_required
from flask_wtf import FlaskForm
from server import blog, bcrypt, db
from server.storage.models import User, Post
from server.storage.sessions import UserSession
from server.view import users
from server.view.pages import PageFlash, PageRedirect, Request, PageRequest, PageUrlFor, AbortPage, InformPage
from server.view.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from server.view.image import UpdateImage
from server.view.templates import YFoxTemplate
from server.view.users import CurrentUser

_root: str = '/'
_home: str = '/home'
_about: str = '/about'
_register: str = '/register'
_account: str = '/account'
_login: str = '/login'
_logout: str = '/logout'
_new_post: str = '/post/new'
_post_id: str = '/post/<int:post_id>'
_update_post: str = _post_id + '/update'
_delete_post: str = _post_id + '/delete'
_GET: str = 'GET'
_POST: str = 'POST'
_forbidden: int = 403


@blog.route(_root)
@blog.route(_home)
def home() -> str:
    posts = Post.query.all()
    return YFoxTemplate('home.html').render(posts=posts)


@blog.route(_about)
def about() -> str:
    return YFoxTemplate('about.html').render(title='About')


@blog.route(_register, methods=[_GET, _POST])
def register() -> str:
    if CurrentUser().authenticated():
        return PageRedirect(PageUrlFor('home')).link()
    form: FlaskForm = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass: str = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user: User = User(username=form.username.data, email=form.email.data, password=hashed_pass)
        UserSession(db).add(user)
        InformPage(f'Your account has been created! You are now able to login with {user.username} username',
                   'success', 'login').perform()
    return YFoxTemplate('register.html').render(title='Register', form=form)


@blog.route(_login, methods=[_GET, _POST])
def login() -> str:
    if CurrentUser().authenticated():
        return PageRedirect(PageUrlFor('home')).link()
    form: FlaskForm = LoginForm()
    if form.validate_on_submit():
        user: User = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            CurrentUser().login(user, form)
            next_page: Request = PageRequest('next').get()
            return PageRedirect(PageUrlFor(next_page if next_page else 'home')).link()
        else:
            PageFlash('Login Unsuccessful. Please check email and password', 'danger').display()
    return YFoxTemplate('login.html').render(title='Login', form=form)


@blog.route(_logout)
def logout() -> str:
    CurrentUser().logout()
    return PageRedirect(PageUrlFor('home')).link()


@blog.route(_account, methods=[_GET, _POST])
@login_required
def account() -> str:
    form: FlaskForm = UpdateAccountForm()
    user: users.User = CurrentUser()
    if form.validate_on_submit():
        if form.picture.data:
            image = UpdateImage(form, blog)
            user.image_file = image.perform()
        user.username = form.username.data
        user.email = form.email.data
        UserSession(db).add(user)
        form.success()
    elif PageRequest().method() == _GET:
        form.username.data = user.username
        form.email.data = user.email
    image_file: Callable = PageUrlFor('static', filename=f'accounts/{user.image_file}')
    return YFoxTemplate('account.html').render(title='Account', image_file=image_file(), form=form)


@blog.route(_new_post, methods=[_GET, _POST])
@login_required
def new_post() -> str:
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=CurrentUser().get_user)
        UserSession(db).add(post)
        form.success()
    return YFoxTemplate('create_post.html').render(title='New Post', form=form, legend='New Post')


@blog.route(_post_id)
def post(post_id) -> str:
    post = Post.query.get_or_404(post_id)
    return YFoxTemplate('post.html').render(title=post.title, post=post)


@blog.route(_update_post, methods=[_GET, _POST])
@login_required
def update_post(post_id) -> str:
    post = Post.query.get_or_404(post_id)
    form = PostForm()
    if post.author != CurrentUser().get_user:
        AbortPage(_forbidden).perform()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        UserSession(db).add(post)
        InformPage('Your post has been updated!', 'success', 'post', post_id=post.id).perform()
    elif PageRequest().method() == _GET:
        form.title.data = post.title
        form.content.data = post.content
    return YFoxTemplate('create_post.html').render(title='Update Post', form=form, legend='Update Post')


@blog.route(_delete_post, methods=[_POST])
@login_required
def delete_post(post_id) -> str:
    post = Post.query.get_or_404(post_id)
    if post.author != CurrentUser().get_user:
        AbortPage(_forbidden).perform()
    UserSession(db).delete(post)
    return InformPage('Your post has been deleted!', 'success', 'home').perform()
