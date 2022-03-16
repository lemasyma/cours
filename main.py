import sys
from argparse import ArgumentParser


def parseLines(lines: list[str], result: list[str], specialTags: list[bool]):
    if not lines:
        if specialTags:
            raise Exception('Found non-ending tag(s) !')
        return

    rawLine = lines.pop(0)
    line = rawLine.strip()
    if line[0:3] != ':::':
        result.append(rawLine)
    else:
        line = line[3:].strip()
        words = [word for word in line.split(' ') if word]
        if not words:
            if not specialTags:
                raise Exception("Found no matching closing separator !")
            specialTag = specialTags.pop()
            if not specialTag:
                result.append('</div>\n')
            else:
                result.append('</details>\n')
        else:
            if words[0] in {'info', 'warning', 'danger', 'success' }:
                result.append(f'<div class="alert alert-{words[0]}" role="alert" markdown="1">\n')
                specialTags.append(False)
            elif words[0] == 'spoiler':
                result.append(f'<details markdown="1"><summary>{" ".join(words[1:])}</summary>\n')
                specialTags.append(True)
            else:
                raise Exception(f'Unrecognised tag `{words[0]}`')
    parseLines(lines, result, specialTags)


def parseFile(source: str):
    result = []
    with open(source, 'r') as f:
        lines = f.readlines()
        parseLines(lines, result, [])
    with open(source, 'w') as f:
        f.write(''.join(result))


if __name__ == '__main__':
    parser = ArgumentParser(description='Parse custom markdown tags')
    parser.add_argument('-s', '--source',
        nargs='+',
        help='Source file(s) in markdown to parse',
        type=str,
        action='store'
    )
    args = parser.parse_args()

    if len(sys.argv) <= 1:
        parser.print_help()
    if args.source:
        for source in args.source:
            parseFile(source)
