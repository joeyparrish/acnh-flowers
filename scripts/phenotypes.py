# Data based on the table at
# https://aiterusawato.github.io/satogu/acnh/flowers/genotypes.html

colors = {
  'r': 'red',
  'o': 'orange',
  'y': 'yellow',
  'p': 'pink',
  'w': 'white',
  'b': 'black',
  'l': 'purple',
  'u': 'blue',
  'g': 'green',
}

def expand3(*args):
  d = {}

  for i0 in (0, 1, 2):
    for i1 in (0, 1, 2):
      for i2 in (0, 1, 2):
        color = args[(i0*3)+i1][i2]
        genes = str(i0) + str(i1) + str(i2)
        d[genes] = colors[color]

  return d

def expand4(*args):
  d = {}

  for i0 in (0, 1, 2):
    for i1 in (0, 1, 2):
      for i2 in (0, 1, 2):
        for i3 in (0, 1, 2):
          color = args[(i0*3)+i1][(i2*3)+i3]
          genes = str(i0) + str(i1) + str(i2) + str(i3)
          d[genes] = colors[color]

  return d


rose = expand4(
  'wwwwwwlll',
  'yyywwwlll',
  'yyyyyywww',
  'rpwrpwrpl',
  'oyyrpwrpl',
  'oyyoyyrpw',
  'brpbrpbrp',
  'ooyrrwbrl',
  'ooyooyurw',
)

tulip = expand3(
  'www',
  'yyw',
  'yyy',
  'ppw',
  'oyy',
  'oyy',
  'brr',
  'brr',
  'lll',
)

pansy = expand3(
  'wwu',
  'yyb',
  'yyy',
  'rru',
  'ooo',
  'yyy',
  'rrl',
  'rrl',
  'ool',
)

cosmo = expand3(
  'www',
  'yyw',
  'yyy',
  'ppp',
  'oop',
  'ooo',
  'rrr',
  'oor',
  'bbr',
)

lily = expand3(
  'www',
  'yww',
  'yyw',
  'rpw',
  'oyy',
  'oyy',
  'brp',
  'brp',
  'oow',
)

hyacinth = expand3(
  'wwu',
  'yyw',
  'yyy',
  'rpw',
  'oyy',
  'oyy',
  'rrr',
  'urr',
  'lll',
)

windflower = expand3(
  'wwu',
  'oou',
  'ooo',
  'rru',
  'ppp',
  'ooo',
  'rrl',
  'rrl',
  'ppl',
)

mum = expand3(
  'wwl',
  'yyw',
  'yyy',
  'ppp',
  'yrp',
  'lll',
  'rrr',
  'llr',
  'ggr',
)

phenotypes = {
  'rose': rose,
  'tulip': tulip,
  'pansy': pansy,
  'cosmo': cosmo,
  'lily': lily,
  'hyacinth': hyacinth,
  'windflower': windflower,
  'mum': mum,
}

seeds = {
  'rose': {
    'white': '0010',
    'yellow': '0020',
    'red': '2001',
  },
  'tulip': {
    'white': '001',
    'yellow': '020',
    'red': '201',
  },
  'pansy': {
    'white': '001',
    'yellow': '020',
    'red': '200',
  },
  'cosmo': {
    'white': '001',
    'yellow': '021',
    'red': '200',
  },
  'lily': {
    'white': '002',
    'yellow': '020',
    'red': '201',
  },
  'hyacinth': {
    'white': '001',
    'yellow': '020',
    'red': '201',
  },
  'windflower': {
    'white': '001',
    'orange': '020',
    'red': '200',
  },
  'mum': {
    'white': '001',
    'yellow': '020',
    'red': '200',
  },
}
