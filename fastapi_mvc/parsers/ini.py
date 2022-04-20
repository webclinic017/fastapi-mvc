"""FastAPI MVC ini parser implementation."""
import os
import logging
import configparser

from fastapi_mvc.exceptions import FileError


class IniParser(object):
    """Project fastapi-mvc.ini file parser class definition."""

    __slots__ = (
        "_log",
        "_project_root",
        "_config",
    )

    def __init__(self, project_root=None):
        """Initialize IniParser class object instance.

        Args:
            project_root (str): A fastapi-mvc project root path.

        Raises:
             FileError: If fastapi-mvc.ini does not exist or not readable.

        """
        self._log = logging.getLogger(self.__class__.__name__)
        self._log.debug("Initialize fastapi-mvc.ini parser.")

        if not project_root:
            self._project_root = os.getcwd()
        else:
            self._project_root = project_root

        ini_file = os.path.join(self._project_root, "fastapi-mvc.ini")
        self._log.debug("Begin parsing: {0:s}".format(ini_file))

        if not os.path.exists(ini_file):
            msg = "{0:s}/fastapi-mvc.ini does not exist.".format(
                self._project_root
            )
            self._log.debug(msg)
            raise FileError(msg)
        elif not os.path.isfile(ini_file):
            msg = "{0:s}/fastapi-mvc.ini is not a file.".format(
                self._project_root
            )
            self._log.debug(msg)
            raise FileError(msg)
        elif not os.access(ini_file, os.R_OK):
            msg = "{0:s}/fastapi-mvc.ini is not readable.".format(
                self._project_root
            )
            self._log.debug(msg)
            raise FileError(msg)

        self._config = configparser.ConfigParser()
        self._config.read(ini_file)

    @property
    def project_root(self):
        """Object instance project root path property.

        Returns:
            Path to project root from which object `fastapi-mvc.ini` was parsed.

        """
        return self._project_root

    @property
    def folder_name(self):
        """Object instance folder name property.

        Returns:
            Folder name value read from a fastapi-mvc.ini file.

        """
        return self._config["project"]["folder_name"]

    @property
    def package_name(self):
        """Object instance package name property.

        Returns:
            Package name value read from a fastapi-mvc.ini file.

        """
        return self._config["project"]["package_name"]

    @property
    def script_name(self):
        """Object instance script name property.

        Returns:
            Script name value read from a fastapi-mvc.ini file.

        """
        return self._config["project"]["script_name"]

    @property
    def redis(self):
        """Object instance Redis property.

        Returns:
            Redis value read from a fastapi-mvc.ini file.

        """
        return self._config["project"]["redis"]

    @property
    def github_actions(self):
        """Object instance GitHub actions property.

        Returns:
            GitHub actions value read from a fastapi-mvc.ini file.

        """
        return self._config["project"]["github_actions"]

    @property
    def aiohttp(self):
        """Object instance Aiohttp property.

        Returns:
            Aiohttp value read from a fastapi-mvc.ini file.

        """
        return self._config["project"]["aiohttp"]

    @property
    def vagrantfile(self):
        """Object instance Vagrantfile property.

        Returns:
            Vagrantfile value read from a fastapi-mvc.ini file.

        """
        return self._config["project"]["vagrantfile"]

    @property
    def helm(self):
        """Object instance Helm property.

        Returns:
            Helm value read from a fastapi-mvc.ini file.

        """
        return self._config["project"]["helm"]

    @property
    def version(self):
        """Object instance fastapi-mvc version property.

        Returns:
            Fastapi-mvc version value read from a fastapi-mvc.ini file.

        """
        return self._config["fastapi-mvc"]["version"]
