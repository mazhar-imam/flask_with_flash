from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'bba42afa18c7a6c09f45b20e0eefecaa'


posts = [

    {
        'author':  'Corey Schafer',
        'title': 'Bog Post 1',
        'content': 'First post content',
        'date_posted': 'april 20, 2018'
    },
    {

        'author':  'jane Doe',
        'title': 'Bog Post 2',
        'content': 'Second post content',
        'date_posted': 'april 21, 2018'
    }

]




@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account crated for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()

    return render_template('login.html', title='Login', form=form)