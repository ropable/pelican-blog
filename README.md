Getting started:

1. Create new virtualenv using Python 3.
1. Clone repo.
1. Run `pip install -r requirements.txt`
1. Run `pelican content` to generate static output.
1. Run `pelican --listen --autoreload` to review content at <http://localhost:8000>
1. (Optional) Update SITEURL value in `pelicanconf.py` for publishing.
1. Make any changes to content, regenerate and upload to web host.

Useful commands:

    pelican content
    pelican --listen --autoreload

Links:

- https://docs.getpelican.com/en/stable/content.html
