from server.view.flashes import BlogFlash
from server.view.forms import RegistrationForm, LoginForm
from server.view.posts import BlogPost
from server.view.redirects import BlogRedirect
from server.view.templates import BlogTemplatePosts, BlogTemplate
from server.view.urls import BlogUrlFor
from server.servers import Server, WebServer

_blog: Server = WebServer()
_blog.config()


@_blog.route('/')
@_blog.route('/home')
def home():
    return BlogTemplatePosts('home.html').render(BlogPost())


@_blog.route('/about')
def about():
    return BlogTemplate('about.html').render(title='About')


@_blog.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        BlogFlash(f'Account created for {form.username.data}!', 'success').display()
        return BlogRedirect(BlogUrlFor('home')).link()
    return BlogTemplate('register.html').render(title='Register', form=form)


@_blog.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            BlogFlash('You have been logged in!', 'success').display()
            return BlogRedirect(BlogUrlFor('home')).link()
        else:
            BlogFlash('Login Unsuccessful. Please check username and password', 'danger').display()
    return BlogTemplate('login.html').render(title='Login', form=form)


if __name__ == '__main__':
    _blog.run()
