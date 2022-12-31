countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}


#countries = {"BOL"}
#northAm = {"CA"}
#centralAm = {"MX"}
#southAm = {"COL"}

new_set = set()
# Escribe tu solución 👇
new_set = countries.union(northAm).union(centralAm).union(southAm)

print(new_set)