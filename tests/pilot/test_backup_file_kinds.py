"""Backup archives are recognised by filename, locally and in S3 metadata."""

from __future__ import annotations

import pytest

from admin.backend.providers.backups import BackupProvider
from pilot.integrations.s3.backups import _file_type

ARCHIVES = [
    ("20261101_193312-site_local-database.sql.gz", "database", "database"),
    ("20261101_193312-site_local-files.tar", "public-file", "files"),
    ("20261101_193312-site_local-private-files.tar", "private-file", "private_files"),
    ("20261101_193312-site_local-server-scripts.tar", "server-scripts", "server_scripts"),
    ("20261101_193312-site_local-site_config_backup.json", "site_config", "site_config"),
]


@pytest.mark.parametrize(("filename", "kind", "_"), ARCHIVES)
def test_local_backup_kind_by_filename(filename: str, kind: str, _: str) -> None:
    assert BackupProvider.get_file_kind(filename) == kind


@pytest.mark.parametrize(("filename", "_", "file_type"), ARCHIVES)
def test_offsite_file_type_by_filename(filename: str, _: str, file_type: str) -> None:
    assert _file_type(filename) == file_type
