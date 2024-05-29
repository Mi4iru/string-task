#!/usr/bin/env python3

"""
Suffix tree to search in dictionary
"""

from typing import List
from suffix_tree import Tree


class SSet:
    """String set. Should be based on Suffix tree"""

    def __init__(self, fname: str) -> None:
        """Saves filename of a dictionary file"""
        self.fname = fname
        self.words = None
        self.tree = Tree()

    def load(self) -> None:
        """
        Loads words from a dictionary file.
        Each line contains a word.
        File is not sorted.
        """
        self.words = []
        i = 0
        with open(self.fname, 'r') as f:
            for line in f:
                word = line.rstrip()
                self.words.append(word)
                self.tree.add(i, word)
                i += 1

    def search(self, substring: str) -> List[str]:
        """Returns all words that contain substring."""
        words = []
        for id_, path in self.tree.find_all(substring):
            words.append(self.words[int(id_)])

        return words
