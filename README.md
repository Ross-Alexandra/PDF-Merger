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
usage: pdftool.py merge [-h] [-s SOURCE_RANGE SOURCE_RANGE]
                        [-m MERGE_RANGE MERGE_RANGE] [-o OUTPUT_FILE]
                        source merge

positional arguments:
  source                The pdf that will be stitched on to
  merge                 The pdf that will be stitched to [source]

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE_RANGE SOURCE_RANGE, --source_range SOURCE_RANGE SOURCE_RANGE
                        Range of pages to include in merged pdf. ex) -s 2 END
  -m MERGE_RANGE MERGE_RANGE, --merge_range MERGE_RANGE MERGE_RANGE
                        Range of pages to include in merged pdf. ex) -m 2 END
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

Example usage combining with page ranges:
``` commandline
python3 pdftool.py merge pdf1.pdf pdf2.pdf -s 1 3 -m 5 END
```
This command will merge pages 1, 2, 3 from pdf1.pdf and pages 5 and on
from pdf2.pdf into a combined pdf called output.pdf
