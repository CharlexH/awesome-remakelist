# SPDX-License-Identifier: MIT
import contextlib
import copy
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import sync_from_site as sync


class PublicSyncTests(unittest.TestCase):
    def source(self):
        return json.loads((sync.ROOT/'data/projects.json').read_text())

    def test_invalid_hash_never_overwrites_the_last_good_snapshot(self):
        source=self.source();bad=copy.deepcopy(source);bad['projects'][0]['localized']['en']['summary']='unverified changed content'
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);(root/'data').mkdir();target=root/'data/projects.json';target.write_text('prior reviewed data')
            with patch.object(sync,'ROOT',root),patch.object(sync,'fetch_feed',return_value=bad):
                with self.assertRaisesRegex(ValueError,'hash'):sync.sync()
            self.assertEqual(target.read_text(),'prior reviewed data')

    def test_new_updates_and_removals_follow_a_valid_published_source(self):
        source=self.source();one=copy.deepcopy(source['projects'][0]);one['id']='new-project';one['site_url']='https://remakelist.com/remakes/new-project/';one['site_url_zh']='https://remakelist.com/zh/remakes/new-project/';one['localized']['en']['summary']='Updated website text'
        source['projects']=[one];source['featured_ids']=[];source['content_sha256']=sync.digest(source)
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);(root/'data').mkdir();target=root/'data/projects.json';target.write_text('{}')
            with patch.object(sync,'ROOT',root),patch.object(sync,'fetch_feed',return_value=source),contextlib.redirect_stdout(io.StringIO()):sync.sync()
            self.assertEqual(json.loads(target.read_text())['projects'],[one])

    def test_valid_hash_does_not_allow_an_unsafe_project_url(self):
        source=self.source();source['projects'][0]['official_url']='javascript:alert(1)';source['content_sha256']=sync.digest(source)
        with self.assertRaisesRegex(ValueError,'unsafe'):sync.validate_feed(source)


if __name__=='__main__':unittest.main()
