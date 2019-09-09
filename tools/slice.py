from PyPDF4 import PdfFileReader as preader, PdfFileWriter as pwriter


def slice_pdf(source, slice_range, keep, writer=None):
    """ slice_pdf(str, range/int, boolean, PdfFileWriter) - Slices a pdf and returns the writer for it.

        Arguments:
            source(str):    The path to the pdf to slice.
            slice_range(int/range):
                    (int):  The first page to slice. All pages following will also be sliced.
                    (range):    The range of pages to slice.
            keep(boolean):  If true, only the slice will be kept. If false, the slice will be removed.
            writer(PdfFileWriter):  A file writer so that operations can be preformed on the pdf before this.
    """

    writer = pwriter()
    source_reader = preader(source)

    is_range = isinstance(slice_range, range)

    for page in range(source_reader.getNumPages()):
        if keep:

            # Only keep pages contained in the range.
            if is_range:
                if page in slice_range:
                    writer.addPage(source_reader.getPage(page))

            # Otherwise it's an int and only pages greater than
            # or equal to that have been kept.
            else:
                if page >= slice_range:
                    writer.addPage(source_reader.getPage(page))

        else:

            # Get rid of pages in this range.
            if is_range:
                if page not in slice_range:
                    writer.addPage(source_reader.getPage(page))

            # Get rid of pages before the specified page.
            else:
                if page < slice_range:
                    writer.addPage(source_reader.getPage(page))

    return writer
