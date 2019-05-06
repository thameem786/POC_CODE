import re

content="ne7/Y0TRFRPN .[MYWIZ_TAhkjj5768G_SLIDE_20]Accenture Distribut"


# filtered_summary = re.sub('\[[A-Z]+_.*\d+\]', "", content)
filtered_summary = re.sub('\[[A-Z]+_*\d+\]', "", content)
# updated_filename = re.sub('[^A-Za-z0-9_.]+', "_", filename)
filtered_summary = re.sub('\W', "", content)

print(filtered_summary)