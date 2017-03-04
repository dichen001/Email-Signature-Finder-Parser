# Setup on OSX

Install brew

Install python3 using brew

    brew install python3

You may need to do this:

    sudo chown -R $(whoami):admin /usr/local

    brew link python3

Install virtualenv

in EmailSim directory

    virtualenv -p python3 venv

    source venv/bin/activate

Now invoking "python" should point to "python3"

    python -v

    pip install docopt
    pip install jinja2

    python email_gen.py

You may see an error

    FileNotFoundError: [Errno 2] No such file or directory: 'output/daniel_mcgowan_20160319_102519.txt'

Create "output" folder (this should be part of python script, to create if missing)

    mkdir output

You should have a successful run now!

Let us now freeze the dependency requirements, and set it up so that someone else can get this going quickly.

    pip freeze > requirements.txt

To get the dependencies configured on another machine, run

    pip install -r requirements.txt
