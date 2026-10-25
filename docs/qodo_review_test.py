"""Throwaway file to verify the Qodo review bot runs on this repository.

It intentionally contains a few reviewable patterns so the review has
findings to report. Safe to delete.
"""
import os


def read_config(path):
    try:
        with open(path) as f:
            return f.read()
    except:  # bare except swallows KeyboardInterrupt too
        return None


def append_result(results=[]):  # mutable default argument shared between calls
    results.append(os.getpid())
    return results


def percentage(value, total):
    return value / total * 100  # ZeroDivisionError when total == 0
