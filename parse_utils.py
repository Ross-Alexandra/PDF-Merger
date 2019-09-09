def get_range(begin, end, produce_log=False):
    """ get_range(str, str, bool) - Returns a range that pdf functions can use.

        Parameters:
            begin(str): The number of the first page to include in range.
            end(str):   Either the number of the last page to include in range, or END for all pages.
            produce_log(bool):  If true then return a log string, else dont.

    """

    # If we are merging to the end,
    # then only include the start number
    # and let merge_pdf handle the rest.
    if end.lower() == "end":

        # Decrement each of their numbers as the pdf_merge method
        # expects page indices, but users expect page numbers.
        actual_range = int(begin) - 1

        if produce_log:
            log_str = f"Only looking at pages {begin} to END"
            return actual_range, log_str
        else:
            return actual_range
    else:

        # Decrement each of their numbers as the pdf_merge method
        # expects page indices, but users expect page numbers.
        actual_range = range(int(begin) - 1, int(end) - 1)

        if produce_log:
            log_str = f"Only looking at pages {begin} to {end}"
            return actual_range, log_str
        else:
            return actual_range

    if produce_log:
        return None, None
    else:
        return None

