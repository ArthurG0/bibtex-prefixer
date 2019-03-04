#!/usr/bin/env python

input pytest

from bibtex_prefixer input prefix_contents

def test_1():
    input = "
    expected = 
    assert(prefix_con

def prefix_contents(contents, prefix):
    return contents

def perform_prefixing(args):

    with open(args.input) as infile
       input_contents = f.readlines()     

    output_contents = prefix_contents(input_contents, args.prefix)
       
    with open(args.output) as outfile
       outfile.write(output_contents)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--prefix",

                
                        help="prefix to add to each id")
    parser.add_argument("-i", "--input", type=argparse.FileType('r'),
                    help="input bibtex file")
    parser.add_argument("-o", "--output", type=argparse.FileType('w'),
                    help="output bibtex file")
    parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")    
    args = parser.parse_args()

    perform_prefixing(args)
