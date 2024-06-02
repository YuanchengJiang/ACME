

target_reports = ['xDiff-1200','xDiff-2400','xDiff-3600']

def parse_report(report):
    griffin_data = report.split("io.questdb.griffin</a>")[1].split("alt=\"")[2].split('"/>')[0].replace(',','')
    print(griffin_data)
    cairo_data = report.split("io.questdb.cairo</a>")[1].split("alt=\"")[2].split('"/>')[0].replace(',','')
    print(cairo_data)
    std_data = report.split("io.questdb.std</a>")[1].split("alt=\"")[2].split('"/>')[0].replace(',','')
    print(std_data)
    jit_data = report.split("io.questdb.jit</a>")[1].split("alt=\"")[2].split('"/>')[0].replace(',','')
    print(jit_data)
    overall_data = report.split(" of 630,514")[0].split('>')[-1].replace(',','')
    overall_data = 630514-int(overall_data)
    print(overall_data)
    return griffin_data, cairo_data, std_data, jit_data, overall_data


griffins = []
cairos = []
stds = []
jits = []
overalls = []

for each_report in target_reports:
    f = open(f"./report-html-{each_report}/index.html","r")
    report = f.read()
    f.close()
    griffin_data, cairo_data, std_data, jit_data, overall_data = parse_report(report)
    griffins.append(griffin_data)
    cairos.append(cairo_data)
    stds.append(std_data)
    jits.append(jit_data)
    overalls.append(overall_data)

print("griffin")
for each in griffins:
    print(each)

print("cairo")
for each in cairos:
    print(each)

print("std")
for each in stds:
    print(each)

print("jit")
for each in jits:
    print(each)

print("overall")
for each in overalls:
    print(each)

