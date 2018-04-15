# Simple markdown server in Python

Simple markdown server written in Python.
It converts your markdown file to HTML and return response as text/html.
Forked from https://github.com/ohbarye/markdown-server .

## Core features

#### 1. Do one thing and do it well

  - This is a simple tool that only render html directly from your markdown files.
    - You can use any folder to store files.
    - You can use any sync methods.
    - You can use any edtiors.

#### 2. It is powerful

  - Github Flavored Markdown.
  - Full MathJax support.
  - [Todo] Awesome fuzzy search through your folders and files.
  - [Todo] Table-of-content support.

## How to start

#### 1.  Install requirements

Create virtualenv first

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

Install the requirements

```bash
$ pip install -r requirements.txt
```

#### 2. Start it

Run the main app script in foreground
```bash
$ source venv/bin/activate
$ python backend/app.py
```

#### 3. Checkout!

Open [http://localhost:5901/notes/sample.md](http://localhost:5901/notes/sample.md) in your browser and see the effect!

#### 4. Add more markdown files!

Link your makedown folder, so that we can see it!

```bash
$ ln -s /path/to/markdown_notes_dir notes/extra
```

Open [http://localhost:5901/notes](http://localhost:5901/notes) and see all your files!
