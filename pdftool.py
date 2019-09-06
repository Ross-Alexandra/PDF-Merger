import argparse
from tools.merge import merge_pdf, get_merge_range

def handle_merge(args):

        try:
            source = args.source[0]
            merge = args.merge[0]

            print(f"Attempting to merge {merge} into {source}.")

            if "source_range" in args:
                source_range, log_str = get_merge_range(args.source_range[0], args.source_range[1])
                if log_str:
                    print(log_str + f" for {source}")

            if "merge_range" in args:
                merge_range, log_str = get_merge_range(args.merge_range[0], args.merge_range[1])
                if log_str:
                    print(log_str + f" for {merge}")

        except Exception as e:
            print(f"Error reading arguments: {e}.\nPlease try again.\nArgs for this run: {args}")
            exit()

        return merge_pdf(source, merge, source_range, merge_range)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command line utility for working with PDF files.")

    # Each command will be faily unique, thus each should have its own parser.
    subparsers = parser.add_subparsers(help="Select a function to preform")

    # Setup the parser for merging pdfs.
    merge_parser = subparsers.add_parser("merge")
    merge_parser.add_argument('source', help="The pdf that will be stitched on to", type=str, nargs=1)
    merge_parser.add_argument('-s', '--source_range', help='Range of pages to include in merged pdf. ex) -s 2 END', type=str, nargs=2)
    merge_parser.add_argument('merge', help="The pdf that will be stitched to [source]", type=str, nargs=1)
    merge_parser.add_argument('-m', '--merge_range', help='Range of pages to include in merged pdf.\nex) -m 2 END', type=str, nargs=2)
    merge_parser.add_argument('-o', '--output_file', help="The name of the outputted pdf", type=str, nargs=1)

    args = parser.parse_args()
    output_filename = args.output_file[0] if args.output_file[0] else "output.pdf"


    # If merge and source are in args
    # then they have selected to merge
    # pdfs.
    if "merge" and "source" in args:
        writer = handle_merge(args)

    else:
        raise Exception("You must select at least one sub-command.")

    # Finally take the pdf writer, and export it.
    with open(output_filename, 'wb') as out_file:
        writer.write(out_file)
