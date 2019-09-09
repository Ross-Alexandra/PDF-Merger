import argparse

from parse_utils import get_range
from tools.merge import merge_pdf
from tools.slice import slice_pdf

def handle_merge(args):

        try:
            source = args.source[0]

            merge = args.merge[0]

            print(f"Attempting to merge {merge} into {source}.")

            if "source_range" in args and args.source_range is not None:
                source_range, log_str = get_merge_range(args.source_range[0], args.source_range[1])
                if log_str:
                    print(log_str + f" for {source}")
            else:
                source_range = None

            if "merge_range" in args and args.merge_range is not None:
                merge_range, log_str = get_merge_range(args.merge_range[0], args.merge_range[1])
                if log_str:
                    print(log_str + f" for {merge}")
            else:
                merge_range = None

        except Exception as e:
            print(f"Error reading arguments: {e}.\nPlease try again.\nArgs for this run: {args}")
            raise e

        return merge_pdf(source, merge, source_range, merge_range)

def handle_slice(args):

    try:
        source = args.source[0]
        slice_range = get_range(args.slice_range[0], args.slice_range[1])

    except Exception as e:
        print(f"Error reading arguments: {e}.\nPlease try again.\nArgs for this run: {args}")
        exit()

    if 'keep' in args and args.keep:
        print(f"Attempting to save only pages {args.slice_range[0]} to {args.slice_range[1]} from {source}")
        return slice_pdf(source, slice_range, True)
    else:
        print(f"Attempting to slice pages {args.slice_range[0]} to {args.slice_range[1]} from {source}")
        return slice_pdf(source, slice_range, False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command line utility for working with PDF files.")

    # Add parser to get output file name.
    parser.add_argument('-o', '--output_file', help="The name of the outputted pdf", type=str, nargs=1)

    # Each command will be faily unique, thus each should have its own parser.
    subparsers = parser.add_subparsers(help="Select a function to preform")

    # Setup the parser for merging pdfs.
    merge_parser = subparsers.add_parser("merge")
    merge_parser.add_argument('source', help="The pdf that will be stitched on to.", type=str, nargs=1)
    merge_parser.add_argument('-s', '--source_range', help='Range of pages to include in merged pdf. ex) -s 2 END', type=str, nargs=2)
    merge_parser.add_argument('merge', help="The pdf that will be stitched to [source].", type=str, nargs=1)
    merge_parser.add_argument('-m', '--merge_range', help='Range of pages to include in merged pdf.\nex) -m 2 END', type=str, nargs=2)

    # Setup the parser for slicing pdfs.
    slice_parser = subparsers.add_parser("slice")
    slice_parser.add_argument('source', help='The pdf that will be sliced.', type=str, nargs=1)
    slice_parser.add_argument('slice_range', help='The range of pages to slice out of the document. ex) 2 END', type=str, nargs=2)
    slice_parser.add_argument('-k', '--keep', help='If present the range will be kept instead of discarded.', action='store_true')

    # Paese the provided argumentsm and attempt to get the filename.
    args = parser.parse_args()
    output_filename = args.output_file[0] if args.output_file else "output.pdf"


    # If merge and source are in args
    # then they have selected to merge
    # pdfs.
    if "merge" in args and "source" in args:
        writer = handle_merge(args)

    elif "slice_range" in args:
        writer = handle_slice(args)

    else:
        raise Exception("You must select at least one sub-command.")

    # Finally take the pdf writer, and export it.
    with open(output_filename, 'wb') as out_file:
        writer.write(out_file)
