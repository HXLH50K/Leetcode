from packaging.version import Version


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = Version(version1)
        v2 = Version(version2)
        return (v1 > v2) - (v1 < v2)
