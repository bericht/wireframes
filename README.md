# bericht_wireframes

templates & static files with a small flask/django app to serve them.
Should be replaced with a real django app soonish.

Install it (preferably to a [virtualenv][virtualenv]) with:

    pip install -r requirements.txt

...and run it with:

    python3 run.py

You should then be able to see the frontpage at [http://localhost:5000](http://localhost:5000) and to play around with the templates. Each template gets the content of data.json as its context.

![frontpage](/bericht/bericht_wireframes/raw/master/frontpage.png)
![fronpage mobile](/bericht/bericht_wireframes/raw/master/frontpage-mobile.png)

[virtualenv]: http://docs.python-guide.org/en/latest/dev/virtualenvs/