import intake
import requests
import yaml

from . import _version
__version__ = _version.get_versions()['version']

SEGMENT_REPO = "igmk/flight-phase-separation"
# SEGMENT_REPO = "eurec4a/flight-phase-separation"


class GithubApi:
    def get(self, endpoint):
        url = "https://api.github.com/" + endpoint
        return requests.get(url,
                            headers={
                                "Accept": "application/vnd.github.v3+json",
                            }).json()


github = GithubApi()


def get_flight_segments(version="latest"):
    """
    Download and parse flight segmentation information.

    :param version: optional version (git-tag) of the flight segmentation release
    """
    if version == "latest":
        release_info = github.get(f"repos/{SEGMENT_REPO}/releases/latest")
    else:
        release_info = github.get(f"repos/{SEGMENT_REPO}/releases/tags/{version}")

    all_flights_asset = [a
                         for a in release_info["assets"]
                         if a["name"] == "all_flights.yaml"][0]
    
    all_flights_url = all_flights_asset["browser_download_url"]

    return yaml.load(requests.get(all_flights_url).content, Loader=yaml.SafeLoader)


def get_meta():
    """
    Download and parse general campaign metadata.
    This includes information about platforms, instruments, people, data access etc.
    """
    return yaml.load(requests.get("https://atmos.meteo.uni-koeln.de/ac3/ac3airborne_meta/meta.yaml").content,
                     Loader=yaml.SafeLoader)


def get_intake_catalog():
    """
    Open the intake data catalog.

    The catalog provides access to public AC3 airborne datasets without the need to
    manually specify URLs to the individual datasets.
    """
    return intake.open_catalog("https://raw.githubusercontent.com/igmk/ac3airborne-intake/halo-ac3/catalog.yaml")


__all__ = ["get_flight_segments",
           "get_meta",
           "get_intake_catalog",
           "__version__"]
