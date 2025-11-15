from algorithms.naive import search as naive
from algorithms.kmp import search as kmp
from algorithms.boyer_moore import search as bm
from algorithms.aho_corasick import search as aho

def test_all():
    print("      TESTING NAIVE")
    print("TEXT: banana bandana | PATTERN: 'ban'  ->", "RESULTS:", naive("banana bandana", "ban"))
    print("TEXT: banana bandana | PATTERN: 'ana'  ->", "RESULTS:",naive("banana bandana", "ana"))
    print("TEXT: aaaaa | PATTERN: 'aa'  ->", "RESULTS:",naive("aaaaa", "aa"))
    print("TEXT: hello world | PATTERN: 'hello'   ->", "RESULTS:",naive("hello world", "hello"))

    print("\n")
    print("       TESTING KMP")
    print("TEXT: banana bandana | PATTERN: 'ban' ->", "RESULTS:",kmp("banana bandana", "ban"))
    print("TEXT: banana bandana | PATTERN: 'ana' ->", "RESULTS:",kmp("banana bandana", "ana"))
    print("TEXT: aaaaa | PATTERN: 'aa'  ->", "RESULTS:",kmp("aaaaa", "aa"))
    print("TEXT: the quick brown fox | PATTERN: 'fox' ->", "RESULTS:",kmp("the quick brown fox", "fox"))

    print("\n")
    print("    TESTING BOYER-MOORE")
    print("TEXT: banana bandana | PATTERN: 'ban'  ->", "RESULTS:",bm("banana bandana", "ban"))
    print("TEXT: banana bandana | PATTERN: 'ana'  ->", "RESULTS:",bm("banana bandana", "ana"))
    print("TEXT: aaaaa | PATTERN: 'aaa'  -> ", "RESULTS:",bm("aaaaa", "aaa"))
    print("TEXT: the quick brown fox | PATTERN: 'the' ->", "RESULTS:",bm("the quick brown fox", "the"))

    print("\n")
    print("    TESTING AHO-CORASICK")
    print("TEXT: banana bandana | PATTERN: ['ban','ana'] ->", "RESULTS:",aho("banana bandana", ["ban", "ana"]))
    print("TEXT: banana bandana | PATTERN: ['ban','ana'] ->", "RESULTS:",aho("banana bandana", ["ban", "ana"]))
    print("TEXT: the quick brown fox jumps the dog | PATTERN: ['the','dog','fox'] ->", "RESULTS:",aho("the quick brown fox jumps the dog", ["the", "dog", "fox"]))
    print("TEXT: aaaaa | PATTERN: ['a','aa','aaa'] ->", "RESULTS:",aho("aaaaa", ["a", "aa", "aaa"]))

test_all()