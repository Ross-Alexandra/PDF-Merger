from PyPDF4 import PdfFileReader as preader, PdfFileWriter as pwriter

def merge_pdf(source, merge, writer=None):
    print(f"Merging {merge} into {source}.")

    if not writer:
        writer = pwriter()

    reader = preader(source)

    # Readers are not iterable, thus
    for page in range(reader.getNumPages()):
        writer.addPage(reader.getPage(page))

    reader = preader(merge)
    for page in range(reader.getNumPages()):
        writer.addPage(reader.getPage(page))

    return writer
