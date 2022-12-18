Getting started:

1. Clone repo.
1. Run `poetry install`
1. Run `poetry run pelican content` to generate static output.
1. Run `poetry run pelican --listen --autoreload` to review content at <http://localhost:8000>
1. (Optional) Update SITEURL value in `pelicanconf.py` for publishing.
1. Make any changes to content, regenerate and upload to web host.

Useful commands:

    pelican content
    pelican --listen --autoreload
    pelican --listen --autoreload --port 8212 --bind 0.0.0.0

Links:

- https://docs.getpelican.com/en/stable/content.html
