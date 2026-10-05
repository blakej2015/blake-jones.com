import re
path = '/Users/stuartblakejones/CascadeProjects/website-migration-clean/src/content/pages/webshop.md'
with open(path, encoding='utf-8') as f:
    lines = f.readlines()
out = []
skip_blank = False
for i, line in enumerate(lines):
    s = line.rstrip('\n')
    m = re.match(r'^(\s+)- (<span.*</span>)$', s)
    if m:
        indent, inner = m.group(1), m.group(2)
        inner = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', inner)
        inner = re.sub(r'\[(<u>[^<]+</u>)\]\(([^)]+)\)', r'<a href="\2">\1</a>', inner)
        out.append(indent + '<li>' + inner + '</li>\n')
        skip_blank = True
        continue
    if skip_blank and s.strip() == '':
        out.append('        </ul>\n')
        skip_blank = False
        continue
    skip_blank = False
    m2 = re.match(r'^(\s*)### (.+)$', s)
    if m2:
        out.append(m2.group(1) + '<h3>' + m2.group(2) + '</h3>\n')
        continue
    if out and out[-1].rstrip('\n').endswith('</h3>') and s.strip() and not s.strip().startswith('<') and not s.strip().startswith('---'):
        indent = len(s) - len(s.lstrip())
        out.append(' '*indent + '<p>' + s.strip() + '</p>\n')
        continue
    if '[<u>' in line:
        line = re.sub(r'\[(<u>[^<]+</u>)\]\(([^)]+)\)', r'<a href="\2">\1</a>', line)
    out.append(line)
with open(path, 'w', encoding='utf-8') as f:
    f.writelines(out)
print('Done!')
