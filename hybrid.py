#!/usr/bin/env python3

from phenotypes import phenotypes
import sys

def mix_gene(g1, g2):
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

def mix_genes(g1, g2):
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

def main(species, g1, g2):
  for genes, prob in mix_genes(g1, g2):
    color = phenotypes[species][genes]
    print(genes, color, prob)

if __name__ == '__main__':
  main(sys.argv[1], sys.argv[2], sys.argv[3])
