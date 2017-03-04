# Email Simulator

### Summary

This generates mock e-mails with real-world email signature formats.
The underlaying data like first name, last name, etc are randomized.
There are picked based on frequency tables (very much a physics MC sim technique).

To run:

    python email_gen.py

To get command-line help:

    python email_gen.py --help

There is a CFG file that stores the configuration.

There will be one .TXT file per mock e-mail.

The default location for the generated .TXT file is "./output"

### Design

Ultimately, this e-mail simulator is data-driven. There are CSV files that store
the atomic randomized data and their frequencies.

The distributions and variations are primarily controlled by the contents of these CSV files.



### Dependencies

I am using WinPython 3.5 (a Windows distribution aimed for engineers), so I cannot be absolute certain.

- Docopt. This is a nice command-line argument parser. It ties the UNIX-like help text to the parser.
- Jinja2. It works good enough in Py3.
- Remainder should be standard Python. But I might be using one or two things introduced in 3.4:
    - print .. naturally.
    - open .. a file.
    - ConfigParser
	- CSV




### TODO

- Currently a wasteful of the random numbers. We'll become more stingy with the generated bits.
- Some frequency tables are from real-world data. Others are simply stubbed up.
  Hopefully will be converting the latter to some thing more rest-world.
