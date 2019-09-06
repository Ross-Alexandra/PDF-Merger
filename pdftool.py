import argparse
from tools.merge import merge_pdf

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command line utility for working with PDF files.")

    # Each command will be faily unique, thus each should have its own parser.
    subparsers = parser.add_subparsers(help="Select a function to preform")

    # Setup the parser for merging pdfs.
    merge_parser = subparsers.add_parser("merge")
    merge_parser.add_argument('source', help="The pdf that will be stitched on to", type=str, nargs=1)
    merge_parser.add_argument('merge', help="The pdf that will be stitched to [source]", type=str, nargs=1)
    merge_parser.add_argument('-o', '--output_file', help="The name of the outputted pdf", type=str, nargs=1)

    args = parser.parse_args()

    # If merge and source are in args
    # then they have selected to merge
    # pdfs.
    if "merge" and "source" in args:

        try:
            source = args.source[0]
            merge = args.merge[0]
            output_filename = args.output_file[0] if args.output_file[0] else "output.pdf"
        except Exception as e:
            print(f"Error reading arguments: {e}.\nPlease try again.")
            exit()

        writer = merge_pdf(source, merge)

        with open(output_filename, 'wb') as out_file:
            writer.write(out_file)
