#!/usr/bin/env python

import jinja2
import markupsafe

from hybridize import hybridize
from phenotypes import phenotypes, seeds, colors, flower_by_number

class GroupedResults(object):
  def __init__(self):
    self.genes = []
    self.probability = 0
    self.outcome = 'unknown'

  def __repr__(self):
    return repr(self.__dict__)


def load_tab_content_filter(tab):
  template = env.get_template('tabs/{}.html'.format(tab))
  return markupsafe.Markup(template.render())


def flower_icon_filter(species, color, genes=None):
  is_seed = genes is not None and genes == seeds[species].get(color)
  seed_class = 'seed' if is_seed else ''
  template = env.get_template('flower-icon.html')
  return markupsafe.Markup(template.render(
      species=species, color=color, seed_class=seed_class))


def flower_pass_filter(species, color):
  template = env.get_template('flower-pass.html')
  return markupsafe.Markup(template.render(species=species, color=color))


def title_filter(outcome):
  return outcome.replace('-', ' ').title().strip()


def is_gene(gene):
  return gene.isdigit()  # All digits, non-empty


@jinja2.pass_environment
def hybridize_filter(env, species, genes1, genes2, layout=None, **kwargs):
  if not is_gene(genes1):
    genes1 = seeds[species][genes1]
  if not is_gene(genes2):
    genes2 = seeds[species][genes2]

  results = hybridize(genes1, genes2)
  color1 = phenotypes[species][genes1]
  color2 = phenotypes[species][genes2]
  grouped_results = {}

  for genes, probability in results:
    color = phenotypes[species][genes]
    if color not in grouped_results:
      grouped_results[color] = GroupedResults()
      if color in kwargs:
        grouped_results[color].outcome = kwargs[color]
    grouped_results[color].genes.append((genes, probability))
    grouped_results[color].probability += probability

  show_outcomes = len(kwargs.keys()) > 0

  results_table_template = env.get_template('hybrid-table-results.html')
  results_table = markupsafe.Markup(results_table_template.render(
      results=grouped_results, species=species,
      show_outcomes=show_outcomes))

  # Unfortunate duplication of names from templates/tabs/breeding-layouts.html
  layout_names = {
    'a': 'Hexahole',
    'b': 'Checkerboard',
    'c': 'Isolated Pairs',
  }

  hybrid_table_template = env.get_template('hybrid-table.html')
  hybrid_table = markupsafe.Markup(hybrid_table_template.render(
      results_table=results_table, species=species,
      layout=layout, layout_name=layout_names[layout] if layout else None,
      genes1=genes1, color1=color1,
      genes2=genes2, color2=color2))

  return hybrid_table


@jinja2.pass_environment
def test_filter(env, species, possible_inputs, genes2, max_tries, **kwargs):
  if not is_gene(genes2):
    genes2 = seeds[species][genes2]

  color1 = phenotypes[species][possible_inputs[0]]
  color2 = phenotypes[species][genes2]

  test_table_template = env.get_template('test-table.html')
  test_table = markupsafe.Markup(test_table_template.render(
      species=species,
      possible_inputs=possible_inputs, color1=color1,
      genes2=genes2, color2=color2,
      max_tries=max_tries,
      outcomes=kwargs))

  return test_table


@jinja2.pass_environment
def phenotypes_filter(env, species):
  num_genotypes = len(phenotypes[species].keys())

  grouped_results = {}
  is_seed = {}
  for genes, color in phenotypes[species].items():
    if color not in grouped_results:
      grouped_results[color] = GroupedResults()
    grouped_results[color].probability += 1 / num_genotypes
    grouped_results[color].genes.append(genes)
    is_seed[genes] = (seeds[species].get(color) == genes)

  phenotypes_table_template = env.get_template('phenotypes.html')
  phenotypes_table = markupsafe.Markup(phenotypes_table_template.render(
      results=grouped_results, species=species, is_seed=is_seed,
      show_outcomes=False))

  return phenotypes_table


@jinja2.pass_environment
def layout_filter(env, rows):
  layout_template = env.get_template('layout.html')
  layout = markupsafe.Markup(layout_template.render(
      rows=rows, colors=colors, flower_by_number=flower_by_number))
  return layout


env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates'),
    autoescape=jinja2.select_autoescape())
env.filters['hybridize'] = hybridize_filter
env.filters['test'] = test_filter
env.filters['phenotypes'] = phenotypes_filter
env.filters['flower_icon'] = flower_icon_filter
env.filters['flower_pass'] = flower_pass_filter
env.filters['layout'] = layout_filter
env.filters['title'] = title_filter
env.filters['load_tab_content'] = load_tab_content_filter

template = env.get_template('index.html')
with open('index.html', 'w') as f:
  f.write(template.render())
