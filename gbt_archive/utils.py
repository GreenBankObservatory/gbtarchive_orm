from pathlib import Path
import re
import glob

from turtlecli.filters import PROJECT_NAME_REGEX


def get_archive_path(project_name, session_name):
    match = PROJECT_NAME_REGEX.search(project_name)
    obs_type = match.groupdict().get("type", None)

    if not obs_type or obs_type == "A":
        subarchive = "science-data"
        archiveprefix = "A"
    else:
        subarchive = "test-data"
        archiveprefix = "T"

    path = Path(
        "/home/archive/{subarchive}/{year}{semester}/"
        "{archiveprefix}GBT{year}{semester}_{code}_{_session}".format(
            subarchive=subarchive,
            _session=session_name,
            archiveprefix=archiveprefix,
            **match.groupdict(),
        )
    )
    return path
