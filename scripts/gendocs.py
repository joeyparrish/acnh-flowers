#!/usr/bin/env python

import jinja2
import markupsafe

from hybridize import hybridize
from phenotypes import phenotypes, seeds

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
  template = ''.join([
      '<div class="icon">',
      '<img src="icons/{species}/{color}.png">',
      '<img class="overlay {seed_class}">',
      '</img>',
      '</div>',
  ])
  return markupsafe.Markup(template.format(
      seed_class=seed_class, species=species, color=color))


@jinja2.pass_environment
def hybridize_filter(env, species, genes1, genes2, **kwargs):
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

  results_table_template = env.get_template('hybrid-table-results.html')
  results_table = markupsafe.Markup(results_table_template.render(
      results=grouped_results, species=species))

  hybrid_table_template = env.get_template('hybrid-table.html')
  hybrid_table = markupsafe.Markup(hybrid_table_template.render(
      results_table=results_table, species=species,
      genes1=genes1, color1=color1,
      genes2=genes2, color2=color2))

  return hybrid_table


env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates'),
    autoescape=jinja2.select_autoescape())
env.filters['hybridize'] = hybridize_filter
env.filters['flower_icon'] = flower_icon_filter
env.filters['load_tab_content'] = load_tab_content_filter

template = env.get_template('index.html')
with open('index.html', 'w') as f:
  f.write(template.render(tabs={
      'overview': 'Overview',
      'windflowers': 'Windflowers',
      'mums': 'Mums',
  }))
