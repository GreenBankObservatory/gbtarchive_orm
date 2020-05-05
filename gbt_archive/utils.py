from pathlib import Path
import re
import glob

# Stolen from turtlecli
PROJECT_NAME_REGEX = re.compile(
    r"(?P<prefix>(?P<type>[AT])?\w*)(?P<year>\d{2,4})(?P<semester>[ABC])[_\s\-]?(?P<code>\d{,10})[_\s\-]?(?P<session>\d+)?",
    re.IGNORECASE,
)

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
