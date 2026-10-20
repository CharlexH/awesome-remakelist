# SPDX-License-Identifier: MIT
"""Regression checks for public-data parsing and review-before-refresh behavior."""
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import sync_from_site as sync


class PublicSyncTests(unittest.TestCase):
    def test_refuses_executable_payload_after_json(self):
        with self.assertRaises(ValueError):
            sync.read_module('export const browserData={}; fetch("https://example.com");')

    def test_changed_requirements_stop_without_replacing_reviewed_data(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'data').mkdir()
            chosen = {'id': 'example', 'stage_fallback_en': 'See docs', 'stage_fallback_zh': '见说明'}
            (root / 'data/selection.json').write_text(json.dumps({'projects': [chosen]}))
            metadata = {'reference_en': 'Original', 'platform': 'Web', 'license_en': 'MIT', 'assets_en': 'No original files.'}
            public = {'items': [{'id': 'example', 'slug': 'example', 'name': 'Example', 'relationship': 'interface-recreation', 'experience_type': 'browser', 'experience_url': 'https://example.com'}], 'itemTranslations': {'example': metadata}}
            page = '<h1>Example</h1><dl><dt>Author</dt><dd>Creator</dd><dt>License</dt><dd><a href="https://example.com/LICENSE">MIT</a></dd></dl><a href="https://example.com/source" aria-label="Source (opens in a new tab)">Source</a><a href="https://example.com/docs" aria-label="Project documentation (opens in a new tab)">Docs</a><time datetime="2026-10-20"></time>'
            def fetch(url):
                return 'export const browserData=' + json.dumps(public) + ';' if url.endswith('.mjs') else page
            with patch.object(sync, 'ROOT', root), patch.object(sync, 'fetch', fetch), contextlib.redirect_stdout(io.StringIO()):
                sync.sync()
                original = (root / 'data/projects.json').read_bytes()
                metadata['assets_en'] = 'Specific original files now required.'
                with self.assertRaisesRegex(ValueError, 'published facts changed'):
                    sync.sync()
                self.assertEqual((root / 'data/projects.json').read_bytes(), original)
                # An explicit review records the new source without any implicit publishing.
                sync.sync(accept_reviewed=True)
                changed = json.loads((root / 'data/projects.json').read_text())
                self.assertEqual(changed['projects'][0]['source_requirements_en'], metadata['assets_en'])


if __name__ == '__main__':
    unittest.main()
