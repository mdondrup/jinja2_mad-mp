# jinja2_mad-mp

A Jinja2 testbed for adapting Data Management Plans (DMPs).
Renders a generic Markdown template with data supplied in a JSON file.

## Files

| File | Description |
|------|-------------|
| `template.j2` | Generic Jinja2 DMP template (Markdown output) |
| `data.json` | Sample DMP data in JSON format |
| `render.py` | Python script that renders the template with the JSON data |
| `requirements.txt` | Python dependencies |

## Usage

### Install dependencies

```bash
pip install -r requirements.txt
```

### Render the template

```bash
# use jinja-cli
jinja2 template.j2 data.json
# Or use python script; both print to stdout
python3 render.py

# Use custom template and/or data file
python3 render.py template.j2 data.json

# Write output to a file
python3 render.py template.j2 data.json -o output.md
```

### Customise

1. Edit `data.json` with your own project details.
2. Optionally modify `template.j2` to add or remove sections.
3. Run `render.py` to generate the rendered DMP.
