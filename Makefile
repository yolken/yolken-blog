.PHONY: preview
preview:
	cd site && jekyll serve

.PHONY: publish
publish:
	./scripts/publish_blog.sh

.PHONY: tags
tags:
	./scripts/create_tag_pages.py