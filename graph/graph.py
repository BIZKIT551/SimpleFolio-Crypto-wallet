import math
import pandas as pd
import pylab as pl
import numpy as np
import json
import datetime

usd_data = pd.read_json('https://goo.gl/dhPu2N', orient='columns')
# gbp_data = pd.read_json('https://goo.gl/dwjs17', orient='columns')
Mdata = pd.read_json(usd_data['name'].to_json(), orient='index')
# data = pd.read_json(gbp_data['name'].to_json(), orient='index')

time = pd.Series(None, index=usd_data.index, name='changes')
Mdata = Mdata.join(time)