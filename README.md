# [papers.rcastellotti.dev](https://papers.rcastellotti.dev)

## run locally
`watchexec -r -e py,jinja2,md,css -- make` (`brew install watchexec` or GFY [^1])

## process to convert a paper from pdf to this beauty
+ go paragraph by paragraph (typeset correctly `\textit` and similar and math)
+ go over the refs
+ bib to footnotes (\[(\d+)\] -> [^$1])
+ extract images `pdfimages -all input.pdf images/prefix`, (`brew install poppler` [^1]), if it does not work just use inkscape
+ pass with grammarly (`aspell` if you feel FrEe LiKe In FrEeDoM) to check if typos were introduced

[^1]: OF COURSE it means Go FigureItOut Yourself, [BUT MAYBE](https://www.urbandictionary.com/define.php?term=GFY)
