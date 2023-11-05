import markdown
import os
from jinja2 import Environment, FileSystemLoader
import yaml
import shutil


def getMetadata(slug, file):
    with open(file) as f:
        heading = f.read().split("---")[1]
        out = yaml.load(heading, Loader=yaml.FullLoader)
        return out

env = Environment(loader=FileSystemLoader("templates"))

m = markdown.Markdown(
    extensions=["fenced_code", "admonition", "codehilite", "meta", "footnotes", "toc", "tables"]
)

dir = "build/p"
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)
papers_dir = "papers"

def index():
    papers = []
    todo=[
        "implement math mode",
        "add the tables to dynamo",
        "go paragraph by paragraph (typeset correctly `\\textit` and similar and math)",
        "go over the refs",
        "bib to footnotes (`\[(\d+)\]` -> `[^$1]`)",
        "extract images `pdfimages -all input.pdf images/prefix`, (install `poppler-utils`, `brew install poppler`) if it does not work just use inkscape",
        "pass with grammarly to check if typos were introduced"
    ]
    for slug in os.listdir(papers_dir):
        paper=os.path.join(papers_dir, slug)
        if os.path.isfile(paper):
            meta = getMetadata(slug, paper)
            papers.append(meta)
    t = env.get_template("index.html.jinja2")
    todo=[markdown.markdown(t) for t in todo]
    index_page = t.render(papers=papers,todo=todo)
    with open("build/index.html", "w") as output_file:
        output_file.write(index_page)
    print(f"[+] generated: /index.html")

def papers():
    t = env.get_template("post.html.jinja2")
    for p in os.listdir(papers_dir):
        p = os.path.join(papers_dir, p)
        if os.path.isfile(p):
            with open(p, "r") as file:
                m.reset()
                paper = m.convert(file.read())
            index_page = t.render(paper=paper, meta=m.Meta)
            os.makedirs("build/p", exist_ok=True)
            slug = m.Meta["slug"][0]
            print(f"[+] generated: /p/{slug}.html")

            with open(f"build/p/{slug}.html", "w") as output_file:
                output_file.write(index_page)

index()
papers()