import argparse

def cli_parser():
    description = "Compute compute something useful based on input and argurments."

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('-o', '--output-filepath',
                        help='Path to a file to output '
                             'feature vector to. Otherwise the feature '
                             'vector is printed to standard out. '
                             'Output is saved in numpy binary format '
                             '(.npy suffix recommended).')
    parser.add_argument('-v', '--verbose',
                        action='store_true', default=False,
                        help='Print additional debugging messages. All '
                             'logging goes to standard error.')
    parser.add_argument('-c', '--config',
                        help='Configuration file')


    parser.add_argument("input_file",
                        help="Input Data file")

    return parser


def main():
    parser = cli_parser()
    args = parser.parse_args()

    # Do something useful with the arguments

if __name__ == "__main__":
    main()
