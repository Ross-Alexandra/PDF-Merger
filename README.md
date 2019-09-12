# PDF-Tools
A simple project to make working with pdfs easy.

### Currently supported applications
    - Merging PDFs.

### Planned support
    - Slicing PDFs.
    - Reordering PDFs.
    - Interactive working with PDFs.
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
```

Translated, this means that to use the tool your command must
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

### Slicing PDFs
Slicing PDFs uses the `slice` command of pdftools.

The automatically generated usage for this command
is:
``` commandline
usage: pdftool.py slice [-h] [-k] source slice_range slice_range

positional arguments:
  source       The pdf that will be sliced.
  slice_range  The range of pages to slice out of the document. ex) 2 END

optional arguments:
  -h, --help   show this help message and exit
  -k, --keep   If present the range will be kept instead of discarded.
```

Translated, this means that to use the tool your command must
first start with
``` commandline
python pdftool.py slice
```

Next, the path to the 'source' pdf must be given. This just means
that you should give the path to the pdf file that you want to slice.

Next, you must specify the range of pages to slice. This can be done
by simply giving either 2 numbers (the first number is the first page
to slice, the second number is the first page to exclude from slicing).
For example, slicing 1 3 will slice the first and second page. You can
also specify the end of the file by stating 'END'. For example, slicing
5 END will slice the fifth page and on.

Finally, you must decide whether you want to keep, or trash the slice.
By default, all pages outside of the slice will be kept. If you would
instead like to keep the pages within the range, add the `-k` switch.

Example usage:
``` commandline
python3 pdftool.py slice pdf.pdf 3 END -o mySlicedPDF.pdf
```
This command will slice the pages from 3 on from pdf.pdf and
and save the pdf without those pages to a pdf called mySlicedPDF.pdf.

``` commandline
python3 pdftool slice pdf.pdf 1 4 -k
```
This command will save the first second and third pages of
the pdf, and throw out all others. The resulting document
will be saved in output.pdf.
