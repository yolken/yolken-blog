#!/usr/bin/env python3
""" create_tag_pages.py """

import logging
import os
import os.path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(message)s',
)

POSTS_DIR = 'site/_posts'
TAG_PAGES_DIR = 'tags'

TAGS_TEMPLATE = """
---
layout: posts-by-tag
title: "Tag: %s"
tag: %s
robots: noindex
---
"""


def main():
    all_tags = set()

    for file_name in os.listdir(POSTS_DIR):
        file_path = os.path.join(POSTS_DIR, file_name)

        with open(file_path) as file_contents:
            for line in file_contents:
                if line.startswith('tags:'):
                    tags = line.strip()[6:].split(' ')
                    for tag in tags:
                        all_tags.add(tag)

    for file_name in os.listdir(TAG_PAGES_DIR):
        file_path = os.path.join(TAG_PAGES_DIR, file_name)
        logging.info('Deleting %s', file_path)
        os.remove(file_path)

    for tag in all_tags:
        file_path = os.path.join(TAG_PAGES_DIR, f'{tag}.html')
        logging.info('Creating %s', file_path)
        with open(file_path, 'w') as tag_file:
            tag_file.write(TAGS_TEMPLATE % (tag, tag))


if __name__ == "__main__":
    main()
