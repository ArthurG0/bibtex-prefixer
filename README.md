# bibtex-prefixer

Script to take a BibTeX file (.bib) as input, and produce, as output
a (.bib) file that is identical, except that the id is changed as follows:

* the id for each entry is prefixed with the supplied prefix
* Exception: if there is a field `acmid` in the entry, instead, the id is replaced with the acmid prefixed by the supplied prefix

# Dependencies

You need to do:

```
pip install bibtexparser
```

See: <https://bibtexparser.readthedocs.io/en/master/install.html#how-to-install>

# Use Case

Suppose you are doing a structured literature survey, and you have:

* `acm-raw.bib` One BibTeX file from the [ACM Digital Library](https://dl.acm.org)
* `ieee-raw.bib` One BibTeX from the [IEEE Xplore](https://ieeexplore.ieee.org/Xplore/home.jsp)

Each has its own ids, which may have collisions.

What this scripts allows you to do is

```
python bibtex_prefixer.py --prefix "acm-" --input acm-raw.bib --output acm-tagged.bib
```

This takes `acm-raw.bib` as input and produces `acm-tagged.bib` where
each id has `acm-` in front of the tag.

Similarly, one can do:

```
python bibtex_prefixer.py --prefix "ieee-" --input ieee-raw.bib --output ieee-tagged.bib
```
