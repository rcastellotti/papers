import markdown
import os
from jinja2 import Environment, FileSystemLoader
import yaml
import shutil


def getMetadata(slug, file):
    with open(file) as f:
        heading = f.read().split("---")[1]
        out = yaml.load(heading, Loader=yaml.FullLoader)
        out["slug"] = slug[:-3]
        return out


env = Environment(loader=FileSystemLoader("templates"))

m = markdown.Markdown(
    extensions=["fenced_code", "codehilite", "meta", "footnotes", "toc", "tables"]
)


dir = "build/p"
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)

papers_dir = "papers"


def index():
    papers = []
    for slug in os.listdir(papers_dir):
        paper=os.path.join(papers_dir, slug)
        if os.path.isfile(paper):
            meta = getMetadata(slug, paper)
            papers.append(meta)
    t = env.get_template("index.html.jinja2")
    index_page = t.render(papers=papers)
    with open("build/index.html", "w") as output_file:
        output_file.write(index_page)
    print(f"[+] generated: /index.html")


def papers():
    t = env.get_template("post.html.jinja2")
    for p in os.listdir(papers_dir):
        p = os.path.join(papers_dir, p)
        if os.path.isfile(p):
            with open(p, "r") as file:
                post = file.read()
                posto = m.convert(post)
            index_page = t.render(post=posto, meta=m.Meta)
            os.makedirs("build/p", exist_ok=True)
            slug = m.Meta["slug"][0]
            print(f"[+] generated: /p/{slug}.html")

            with open(f"build/p/{slug}.html", "w") as output_file:
                output_file.write(index_page)


index()
papers()
