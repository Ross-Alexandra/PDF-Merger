# PDF-Tools
A simple project to make working with pdfs easy.

### Currently supported applications
    - Merging PDFs.

### Planned support
There are currently no plans to expand functionality. However, this
is due to other projects rather than lack of interest. If you have
a feature you want added to this tool, open an issue.

## Usage
As this tool is meant to have many functions, each function's
usage will be broken down in this section.

In general, the unpackaged version of this project will require
Python3 and the dependancies outlined in `requirements.txt`.

To install these requirements, first install `pip3` then
run from the root directory:
``` commanline
pip install -r requirements.txt
```

### Merging PDFs
Merging PDFs uses the `merge` command of pdftools.

The automatically generated usage for this command
is:
``` commandline
usage: pdftool.py merge [-h] [-o OUTPUT_FILE] source merge

positional arguments:
  source                The pdf that will be stitched on to
  merge                 The pdf that will be stitched to [source]

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        The name of the outputted pdf
```

Translated, this means that to use the tools your command must
first start with
``` commandline
python pdftool.py merge
```

Next, the path to the 'source' and 'merge' pdfs must be added.
The 'source' pdf is the pdf that will appear first in the merged
doc. The 'merge' pdf is the pdf that will be appeneded to source.

Finally, if you want to output to a file other that 'output.pdf'
specify the `-o` or `--output_file` switch, and provide a file name.

Example usage:
``` commandline
python3 pdftool.py merge pdf1.pdf pdf2.pdf -o myCombinedPDF.pdf
```
