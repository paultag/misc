import textwrap


def nomer(stream):
    for el in stream:
        if el.strip() == '<<Anchor(A)>>':
            yield el
            break
    yield from stream


def lines():
    with open("Glossary.txt") as fd:
        for line in fd:
            yield line.strip()

def print_def(word, block):
    print(":{}:".format(word))
    print("")
    wrapper = textwrap.TextWrapper(
        subsequent_indent="    ",
        initial_indent="    ",
        width=80,
    )
    print("\n".join(wrapper.wrap(block)))
    print("")


word = None
defn = None
for line in nomer(lines()):

    if (
        line.startswith("<<") or
        line.startswith("= ") or
        line.startswith("/*") or
        line == ""
    ):
        continue

    if "::" in line:
        if word and defn:
            print_def(word, defn)
        word, defn = (x.strip() for x in line.split("::", 1))
        continue
    if defn is None:
        raise Exception(line)
    defn += "\n{}".format(line)

print_def(word, defn)
