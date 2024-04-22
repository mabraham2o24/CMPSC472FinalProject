# directory: cd "C:\Users\mabra\OneDrive\Desktop\472 Final Project"
# run sql: sqlite3 users.db
# show the table: SELECT * FROM users;
#logins:
"""
1|mabraham24|Andrew09
2|anil1234|Andrew#09
3|vini1234|Andrew#2009
4|andrew54|Andrew22
5|treasure21|Purplepancakes
6|batman2|Superman
7|ron123|Andrew
8|rini98|Ron01
9|eagles17|superbowl
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set your own secret key

# Create a SQLite database
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''
          CREATE TABLE IF NOT EXISTS users (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT NOT NULL,
              password TEXT NOT NULL
          )
          ''')
conn.commit()
conn.close()

# Hardcoded good news articles for different categories
good_news_articles = {
    'Recovery Stories': [
        {'title': 'Tylers Story', 'content': 'Click Read More to Access The Article or Click Generate for Another Article', 'source': 'Family for Addiction Recovery', 'url': 'https://www.farcanada.org/tylers-story/', 'author': 'Tyler'},        
        {'title': 'Finding Hope Again After Losing Everything to Addiction', 'content': 'Click Read More to Access The Article or Click Generate for Another Article', 'source': 'Addiction Hope', 'url': 'https://www.addictionhope.com/recovery/inspirational-stories/finding-hope-again-after-losing-everything-to-addiction/', 'author': 'Andrea Blume'},        
        {'title': 'Living Recovery: True Stories of Addiction Recovery', 'content': 'Click Read More to Access The Article or Click Generate for Another Article', 'source': 'Recovery Centers of America', 'url': 'https://recoverycentersofamerica.com/blogs/living-recovery-true-stories-of-addiction-recovery/', 'author': 'Recovery Centers of America'},        
        {'title': 'Andreas Story', 'content': 'Click Read More to Access The Article or Click Generate for Another Article', 'source': 'Family for Addiction Recovery', 'url': 'https://www.farcanada.org/family-support/stories-of-recovery/', 'author': 'Andrea'},        
        {'title': 'Overcoming Alcohol Addiction: 4 Inspiring Stories of Triump and Transformation', 'content': 'Click Read More to Access The Article or Click Generate for Another Article', 'source': 'Aquila Recovery', 'url': 'https://www.aquilarecovery.com/blog/overcoming-alcohol-addiction-4-inspiring-stories-of-triumph-and-transformation/', 'author': 'Aquila Recovery Clinic'},        

        # Add more articles for the 'animals' category
    ],
    'Impact of Addiction': [
        {'title': 'People Who Have Been Impacted By Family Substance', 'content': 'Click Read More to Access The Article or Click Generate for Another Article', 'source': 'Change Grow Live', 'url': 'https://www.changegrowlive.org/advice-info/family-substance-use-stories', 'Author': 'No Author'},
        {'title': 'How Drug Addiction Affects the Entire Family', 'content': 'Click Read More to Access The Article or Click Generate for Another Article', 'source': 'Peace Valley Recovery', 'url': 'https://www.peacevalleyrecovery.com/blog/how-drug-addiction-affects-the-entire-family/', 'Author': 'Elliot Redwine'},
        {'title': 'Stories of Survival: Families Affected By Addiction Share Advice', 'content': 'Click Read More to Access The Article or Click Generate for Another Article', 'source': 'The Guardian', 'url': 'https://www.theguardian.com/social-care-network/2016/feb/23/drug-alcohol-misuse-addiction-families-advice', 'Author': 'Nicola Slawson'},
        {'title': 'Everything Changed: Reuniting Families Fractured by Opioids', 'content': 'Click Read More to Access The Article or Click Generate for Another Article', 'source': 'Cornell Chronicle', 'url': 'https://news.cornell.edu/stories/2022/11/everything-changed-reuniting-families-fractured-opioids', 'Author': 'Susan Kelley'},
        {'title': 'Family Addiction: How Does Addiction Affect Families?', 'content': 'Click Read More to Access The Article or Click Generate for Another Article', 'source': 'American Addiction Centers', 'url': 'https://americanaddictioncenters.org/rehab-guide/guide-for-families-i', 'Author': 'Editorial Staff'},

        # Add more articles for the 'nature' category
    ],
    'Statistics': [
        {'title': 'Drug, Subtance Abuse and Addiction Statistics 2024', 'content': 'Click Read More to Access The Article or Click Generate for Another Article', 'source': 'USA Today', 'url': 'https://www.usatoday.com/money/blueprint/health-insurance/addiction-statistics/', 'Author': 'Timothy Moore, Jennifer Lobb, and Heidi Gollub'},
        {'title': 'NIDA IC Fact Sheet 2024', 'content': 'Click Read More to Access The Article or Click Generate for Another Article', 'source': 'National Institute on Drug Abuse', 'url': 'https://nida.nih.gov/about-nida/legislative-activities/budget-information/fiscal-year-2024-budget-information-congressional-justification-national-institute-drug-abuse/ic-fact-sheet-2024 ', 'Author': 'No Author'},
        {'title': 'Drug, Substance Abuse, and Addiction Statisitcs for 2024', 'content': 'Click Read More to Access The Article or Click Generate for Another Article', 'source': 'Victory Recovery Partners', 'url': 'https://www.victoryrp.com/blog/drug-substance-abuse-and-addiction-statistics-for-2024', 'Author': 'Victory Recovery Partners'},
        {'title': 'Drug Addiction Statistics 2024', 'content': 'Click Read More to Access The Article or Click Generate for Another Article', 'source': 'Tech Report', 'url': 'https://techreport.com/statistics/drug-addiction-statistics/', 'Author': 'Jeff Beckman'},
        {'title': 'Drug Overdose Deaths in The United States 2002-2022', 'content': 'Click Read More to Access The Article or Click Generate for Another Article', 'source': 'Centers for Disease Control and Prevention', 'url': 'https://www.cdc.gov/nchs/products/databriefs/db491.htm', 'Author': 'Merianne R. Spencer'},

        # Add more articles for the 'inspiring' category
    ],
    
}

def get_random_good_news(category):
    # Randomly select an article from the specified category
    return random.choice(good_news_articles.get(category, []))

# Update the calculate_overall_mood function in app.py

def calculate_overall_score(answers):
    # Calculate the overall mood based on answers
    total_score = sum(answers)
    num_questions = len(answers)
    average_score = total_score / num_questions

    #Categorize overall mood based on average score and assign emojis
    if average_score <= 2:
        survey_category = "Seek Professional Help"
    elif 2 < average_score <= 3:
        survey_category = "Reach Out To A Friend Or Family Member"
    elif 3 < average_score <= 4:
        survey_category = "You Are Doing Good!"
    elif 4 < average_score <= 5:
        survey_category = "You Are Doing Amazing!"

    return survey_category
  
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def categorize_results(score):
    if score < 10:
        return "Please Seek Professional Help"
    elif 10 <= score < 20:
        return "Reach Out To A Friend Or Family Member"
    elif 20 <= score < 30:
        return "You Are Doing Good!"
    elif 30 <= score < 40:
        return "You Are Doing Amazing!"
    

def get_advice(category):
    if category == "Please Seek Professional Help":
        return "Please reach out and get profession help. You are struggling right now and the sooner you reach out for help the better. You got this!"
    elif category == "Reach Out To A Friend Or Family Member":
        return "Take it one day at a time. Addiction is a serious matter and it takes a lot of strength to beat it. Reach out to your loved one and use them as your support system."
    elif category == "You Are Doing Good!":
        return "Right now you are not doing too bad or too good. It can be hard at times but with your strength you can get overcome it. "
    elif category == "You Are Doing Amazing!":
        return "Keep doing what you're doing! You are such a strong individual and there is nothing that can take you down. "

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = c.fetchone()

    conn.close()

    if user:
        return render_template('menu.html', username=username)
    else:
        flash('Incorrect username or password', 'error')
        return redirect(url_for('home'))

@app.route('/register')
def register():
    return render_template('register.html')


# Modified /stressometer route to handle form submissions
@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        # Extracting scores from the form
        scores = [int(request.form[f'q{i}']) for i in range(1, 10)]

        # Sorting the scores using quicksort
        sorted_scores = quicksort(scores)

        # Summing the top 5 scores
        total_score = sum(sorted_scores[-5:])

        # Calculating mood category and emoji
        survey_category = calculate_overall_score(scores)

        # Categorizing the overall mood
        survey_category = categorize_results(total_score)

        # Getting advice based on the mood category
        advice = get_advice(survey_category)

        return render_template('survey_result.html', survey_category=survey_category, advice=advice)

    return render_template('survey.html')


@app.route('/journaling', methods=['GET', 'POST'])
def journaling():
    if request.method == 'POST':
        # Get the journal content and username from the form
        journal_content = request.form['journal_content']
        username = request.form['username']

        # Save the journal entry to a database or file
        # For demonstration purposes, I'll assume you have a database table named 'journal_entries'
        # with columns 'username' and 'content'
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('INSERT INTO journal_entries (username, content) VALUES (?, ?)', (username, journal_content))
        conn.commit()
        conn.close()

    # Fetch all journal entries for the current user
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT username, content FROM journal_entries WHERE username=?', (username,))
    entries = c.fetchall()
    conn.close()

    # Pass the entries to the template for rendering
    return render_template('journaling.html', entries=entries, username=username)





@app.route('/good-news', methods=['GET', 'POST'])
def good_news():
    if request.method == 'POST':
        category = request.form.get('category', 'Recovery Stories')  # Default to 'recovery stories' if no category is selected
        random_article = get_random_good_news(category)
        return render_template('good_news.html', articles=[random_article])

    # If it's a GET request, show an article from the default category
    default_category = 'Recovery Stories'
    random_article = get_random_good_news(default_category)
    return render_template('good_news.html', articles=[random_article])

@app.route('/resources')
def resources():
    # Render the resources.html template
    return render_template('resources.html')

@app.route('/statistics')
def statistics():
    # You can pass any necessary data to the template here
    return render_template('statistics.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()

    conn.close()

    flash(f'Account created for {username}', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
