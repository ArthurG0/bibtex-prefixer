#!/usr/bin/env python

import argparse
import bibtexparser

def modify_entry(entry):
    return entry

def perform_prefixing(args):


    contents = args.input.read()

    contents = contents.replace("month = jan","month = {January}")
    contents = contents.replace("month = feb","month = {February}")
    contents = contents.replace("month = mar","month = {March}")
    contents = contents.replace("month = apr","month = {April}")
    contents = contents.replace("month = may","month = {May}")
    contents = contents.replace("month = jun","month = {June}")
    contents = contents.replace("month = jul","month = {July}")
    contents = contents.replace("month = aug","month = {August}")
    contents = contents.replace("month = sep","month = {September}")
    contents = contents.replace("month = oct","month = {October}")
    contents = contents.replace("month = nov","month = {November}")
    contents = contents.replace("month = dec","month = {December}")
    
    bibtex_database = bibtexparser.loads(contents)

    for i in range(len(bibtex_database.entries)):
        bibtex_database.entries[i] = modify_entry(bibtex_database.entries[i])
    
    bibtexparser.dump(bibtex_database, args.output)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
    
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument("-p", "--prefix",                
                               help="prefix to add to each id", required=True)
    requiredNamed.add_argument("-i", "--input", type=argparse.FileType('r'),
                               help="input bibtex file", required=True)
    requiredNamed.add_argument("-o", "--output", type=argparse.FileType('w'),
                               help="output bibtex file",required=True)

    args = parser.parse_args()

    perform_prefixing(args)
