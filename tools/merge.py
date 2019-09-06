from PyPDF4 import PdfFileReader as preader, PdfFileWriter as pwriter


def merge_pdf(source, merge, source_range=None, merge_range=None, writer=None):
    """ merge_pdf - Takes two pdfs and merges their contents to a single pdf.

        Parameters:
            source(str):        Path to the source pdf.
            merge(str):         Path to the pdf to merge to source.
            source_range(range/int):
                    (int):      The start page to merge. Assume it should merge
                                to end of the source document.
                    (range):    The range of pages to include from source document.
            merge_range(range/int):
                    (int):      The start page to merge into source. Assume it should
                                merge to the end of the merge document.
                    (range):    The range of pages to include from the merge document.
            writer(PDFFileWriter):  Writer to add document to. This is incase other operations
                                    need to be done *before* this.
    """

    # Create the writer.
    if not writer:
        writer = pwriter()

    # Get the bytes for both documents.
    source_reader = preader(source)
    merge_reader = preader(merge)

    # Find range of pages to merge from source.
    if isinstance(source_range, int):

        # If the range is just an int, presume user wants
        # from source_range to end.
        source_range = range(source_range, source_reader.getNumPages())
    elif not source_range:
        source_range = range(source_reader.getNumPages())

    # Find range of pages to merge from merge.
    if isinstance(merge_range, int):

        # If the range is just an int, presume user wants
        # from merge_range to end.
        merge_range = range(merge_range, merge_reader.getNumPages())
    elif not merge_range:
        merge_range = range(merge_reader.getNumPages())

    # Add each page of source to the document.
    for page in source_range:
        writer.addPage(source_reader.getPage(page))

    # Add each page of merge to the document.
    for page in merge_range:
        writer.addPage(merge_reader.getPage(page))

    # Return the bytes of the PDF.
    return writer

def get_merge_range(begin, end):

    # If we are merging to the end,
    # then only include the start number
    # and let merge_pdf handle the rest.
    if end.lower() == "end":

        # Decrement each of their numbers as the pdf_merge method
        # expects page indices, but users expect page numbers.
        actual_range = int(begin) - 1
        log_str = f"Only looking at pages {begin} to END"

        return actual_range, log_str
    else:

        # Decrement each of their numbers as the pdf_merge method
        # expects page indices, but users expect page numbers.
        actual_range = range(int(begin) - 1, int(end) - 1)
        log_str = f"Only looking at pages {begin} to {end}"

        return actual_range, log_str

    return None, None

