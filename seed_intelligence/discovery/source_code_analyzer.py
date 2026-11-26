"""Bounded structural observations from source already read by the normal worker."""
import re

LOOP = re.compile(r"\b(?:while|for)\s*\(")

def source_evidence(source):
    if not isinstance(source, str):
        return {}
    excerpt = source[:16000]
    code_lines = [line.split("//", 1)[0] for line in excerpt.splitlines()]
    loop_lines = [number for number, line in enumerate(code_lines, 1) if LOOP.search(line)]
    return {"sourceStructure": {"scannedLines": len(code_lines), "loopLines": loop_lines[:20]}}
