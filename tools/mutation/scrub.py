"""Replace a Windows or Unix profile folder in captured output with %USERPROFILE%.
The verification scripts pass everything they save through `scrub`, so logs and summaries
committed to a public repository never carry the person's account name.
"""
import re

_PROFILE = re.compile(
    r"(?:(?:[A-Za-z]:(?:\\\\|\\|/)+|/[a-z]/)Users(?:\\\\|\\|/)+|\\?/(?:Users|home)\\?/)"
    r"[^\\/\s\"'<>|:*?]+"
)


def scrub(text: str) -> str:
    return _PROFILE.sub("%USERPROFILE%", text)
