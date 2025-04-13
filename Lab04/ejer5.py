import re

def is_html_balanced(html):
    stack = []
    tags = re.findall(r'</?[^<>]+?>', html)    # Encuentra <etiqueta> o </etiqueta>

    for tag in tags:
        if not tag.startswith('</'):
            # Etiqueta de apertura
            tag_name = tag[1:-1].split()[0]     # saca el nombre, ignora atributos
            stack.append(tag_name)
        else:
            # Etiqueta de cierre
            tag_name = tag[2:-1]
            if not stack:
                return False, f"Extra closing tag </{tag_name}> found!"
            last_open = stack.pop()
            if last_open != tag_name:
                return False, f"Mismatched tag: expected </{last_open}> but found </{tag_name}>"
            
    if stack:
        return False, f"Missing closing tag(s) for: {stack}"
    
    return True, "All tags are balanced!"
tests = [
    ("<html><body><h1>Hello</h1></body></html>", True),
    ("<div><p>Hi</p></div>", False),
    ("<ul><li>Item 1</li>Item 2</li></ul>", False),
    ("<a><b></b></a>", True),
    ("<div><span>Hello</span>", False),
    ("<div>Hi</div></div>", False),
    ("<br>", True),     # una etiqueta que no se cierra
]

for html, expected in tests:
    result, message = is_html_balanced(html)
    print(f"HTML: {html}\nBalanced? {result} - {message}\n")