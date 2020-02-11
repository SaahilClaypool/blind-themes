import json 
from collections import defaultdict
import typing

f = json.loads(open('./tokens.json', 'r').read())


def parse(tokens):
    scope_map: typing.Dict[str, list] = defaultdict(lambda: [])
    style_map: typing.Dict[str, str] = defaultdict(lambda: "")
    name_map: typing.Dict[str, str] = defaultdict(lambda: "")
    for el in tokens:
        style = " ".join(sorted(el['settings'].values()))
        style_map[style] = el['settings']
        scopes = el['scope']
        print(el)
        if name_map[style] == "" and 'name' in el.keys():
            name_map[style] = el['name']

        if isinstance(scopes, str):
            scopes = [scopes]
        scope_map[style] += scopes

    return (scope_map, style_map, name_map)


def dump(scope_map, style_map, name_map):
    """
    """
    tokens = []
    for style in scope_map.keys():
        tokens.append ({
            "name": name_map[style],
            "scope": scope_map[style],
            "settings": style_map[style]
        })

    st = json.dumps(tokens, indent=4)
    return st

st = dump(*parse(f))
print(st)

with open('tokens_condensed.json', 'w') as outfile:
    outfile.write(st)