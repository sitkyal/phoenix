# Store user selected columns (label and features)

import pandas as pd
import sys

def flabel_features(label, features):
	selected_label = pd.Series(label).values
	selected_features = pd.Series(features).values
	return selected_label, selected_features


label = sys.argv[1]
features = sys.argv[2:]

selected_label, selected_features = flabel_features(label, features)
print selected_label, selected_features
#sys.stdout.flush()
