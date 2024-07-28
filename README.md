# Job-Search Tools

Hey, I started this project the tedious parts about the academic job search that I automate during my preparation.

This is an on-going library that I will keep improving and adding funcionality into.
If you are missing something, feel free to open a PR.


## Functionality

### Co-authors

I thought it may be useful to count the number of co-authors, although I didn't end up using it.

```sh
python job_search/co_authors/count.py --author_id AUTHOR_ID
```

Notes:

* Update the [config.json](config.json) file with the `s2` api key which you can request [here](https://www.semanticscholar.org/product/api).
* Retrieve the author id from semantic scholar by looking up the researcher you're interested in and copying the number id after their name in the url.


### Latex

For my research statement, I wanted a short, clean reference page, so this script (written by ChatGPT) cleans a bib file.

```sh
python job_search/latex/simplify.py --input_file data/sample.bib --output_file data/simplified.bib
```

Notes:

* I included a [sample file](data/sample.bib) with a few of my papers for testing the sciprt. Make sure to use the path to your papers bib file when actually running it.
* I used ChatGPT for creating this script. You can check it out [here](https://chatgpt.com/share/2ec25c41-1f48-4884-800e-c71cc2787aa3).
* The script works for my papers (I think most of them), but I only covered conferences I published at (or that some model automatically completed when working on the script). Check out the [config.json](config.json) file to add additional conference mapping.