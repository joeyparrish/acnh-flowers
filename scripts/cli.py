#!/usr/bin/env python3

# Joey's ACNH Flower Guide
# Copyright (C) 2024 Joey Parrish
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
