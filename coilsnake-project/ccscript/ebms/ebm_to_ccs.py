#!/usr/bin/env python3
# Script to convert .ebm to .ebm.ccs
from os import write
import sys
import struct
from typing import List

BYTES_PER_LINE = 32

USAGE = (
    '=== ebm_to_ccs ===',
    'Usage: python3 ebm_to_ccs.py abc.ebm',
    '  -> converts abc.ebm to abc.ccs which will have the raw data',
    '     from abc.ebm wrapped in a command called "ebm_data"',
)
def usage():
    for l in USAGE:
        print( l )

def ebm_to_ccs( ebm_filename: str ) -> int:
    '''Convert an EBM file to a .ccs'''
    
    # Read in all the .EBM data
    with open( ebm_filename, 'rb' ) as fin:
        ebm_data = fin.read()
    ebm_len, ebm_addr = struct.unpack_from( '<HH', ebm_data, 0 )
    assert ebm_len == len( ebm_data ) - 4, ( 'EBM file has invalid length, '
        'expected {:#04X} but file says {:#04X}'.format( len(ebm_data) - 4, ebm_len ))
    
    # Calculate output filename
    ccs_filename = ebm_filename.replace( '.ebm', '' ) + '.ccs'

    # Write output file
    with open( ccs_filename, 'w' ) as fout:
        print( 'command ebm_data {', file=fout )
        write_ptr = 0
        while write_ptr < len( ebm_data ):
            next_ptr = write_ptr + BYTES_PER_LINE
            if next_ptr > len( ebm_data ):
                next_ptr = len( ebm_data )
            chunk = ebm_data[ write_ptr : next_ptr ]
            write_ptr = next_ptr
            chunk_str = ''.join('{:02X}'.format(x) for x in chunk)
            print( '   "[', chunk_str, ']"', file=fout, sep='' )
        print( '}', file=fout )

    return 0

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2 or args[1] == '-h' or args[1] == '--help':
        usage()
        sys.exit( 0 )
    sys.exit( ebm_to_ccs( args[1] ) )
