from flask import render_template, flash, url_for, redirect
from server.forms import RegistrationForm, LoginForm
from server.posts import BlogPost
from server.servers import Server, WebServer

_blog: Server = WebServer()
_blog.config()


@_blog.route('/')
@_blog.route('/home')
def home():
    return render_template('home.html', posts=BlogPost().data())


@_blog.route('/about')
def about():
    return render_template('about.html', title='About')


@_blog.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@_blog.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    _blog.run()
