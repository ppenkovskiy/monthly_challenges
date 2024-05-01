Project "Monthly Challenges" preview:

...

Installing "Monthly Challenges" project on Linux:

git clone git@github.com:ppenkovskiy/monthly_challenges.git

cd monthly_challenges

sudo apt install python3.10-venv

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python3 manage.py migrate

python3 manage.py runserver