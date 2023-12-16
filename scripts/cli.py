#!/usr/bin/env python3

import argparse
import sys

from hybridize import hybridize
from phenotypes import phenotypes

def main():
  parser = argparse.ArgumentParser(
      description='Compute flower hybrids for "Animal Crossing: New Horizons"')
  parser.add_argument('--species', '-s',
      choices=phenotypes.keys(),
      required=True)
  parser.add_argument('--genes1', '-g1',
      required=True)
  parser.add_argument('--genes2', '-g2',
      required=True)
  args = parser.parse_args()

  for genes, prob in hybridize(args.genes1, args.genes2):
    color = phenotypes[args.species][genes]
    print(genes, color, prob)

if __name__ == '__main__':
  main()
