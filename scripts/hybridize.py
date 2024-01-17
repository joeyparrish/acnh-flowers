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

def mix_gene(g1, g2):
  """Mix two single genes in ternary format (0, 1, 2).

  Yields a sequence of tuples (resulting gene and probability from 0-1)."""

  if g1 == '0':
    if g2 == '0':
      yield ('0', 1)
    elif g2 == '1':
      yield ('0', 0.5)
      yield ('1', 0.5)
    elif g2 == '2':
      yield ('1', 1)
  elif g1 == '1':
    if g2 == '0':
      yield ('0', 0.5)
      yield ('1', 0.5)
    elif g2 == '1':
      yield ('0', 0.25)
      yield ('1', 0.5)
      yield ('2', 0.25)
    elif g2 == '2':
      yield ('1', 0.5)
      yield ('2', 0.5)
  elif g1 == '2':
    if g2 == '0':
      yield ('1', 1)
    elif g2 == '1':
      yield ('1', 0.5)
      yield ('2', 0.5)
    elif g2 == '2':
      yield ('2', 1)

def hybridize(g1, g2):
  """Hybridize two gene sequences in ternary format (0, 1, 2) of any length.

  Returns a list of tuples (resulting sequence and probaility from 0-1)."""

  assert len(g1) == len(g2)

  mixes = [('', 1)]
  for i in range(len(g1)):
    options = list(mix_gene(g1[i], g2[i]))
    new_mixes = []

    for prefix, prefix_prob in mixes:
      for gene, gene_prob in options:
        new_mix = prefix + gene
        new_prob = prefix_prob * gene_prob
        new_mixes.append((new_mix, new_prob))

    mixes = new_mixes

  return mixes
