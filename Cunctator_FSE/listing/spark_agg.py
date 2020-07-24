lines = sc.textFile("foo")
ws = lines.flatMap(lambda l: l.split())
ws = ws.filter(lambda x: re.match("^[\w]+$", x))
word_count = ws.count()
total_len = ws.map(lambda w: len(w)).sum()
avg_len = total_len / word_count