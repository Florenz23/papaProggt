#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import argparse

from dictcc import Dict, AVAILABLE_LANGUAGES


LINE_LENGTH = 60


def ensure_unicode(string):
    if hasattr(string, "decode"):
        return string.decode("utf-8")
    return string


def parse_args():
    parser = argparse.ArgumentParser(description="Unoficial CLI for dict.cc. "\
        "It supports translations between the following languages: {}".format(
        ", ".join(AVAILABLE_LANGUAGES)))
    parser.add_argument("input_language", type=str, help="Input language",
        choices=AVAILABLE_LANGUAGES.keys())
    parser.add_argument("output_language", type=str, help="Output language",
        choices=AVAILABLE_LANGUAGES.keys())
    parser.add_argument("word",
                         type=ensure_unicode,
                         help=("Word to translate (use quotation marks for "
                               "phrases like \"free beer\")."))
    parser.add_argument("--max-results", type=int, default=10)
    args = parser.parse_args()

    if args.input_language == args.output_language:
        raise ValueError("Please choose different languages")

    return args


def print_header(from_lang, to_lang):
    print(u"{}{}{}\n{}{}{}".format(
        from_lang,
        " "*(LINE_LENGTH-len(from_lang)),
        to_lang,
        "="*len(from_lang),
        " "*(LINE_LENGTH-len(from_lang)),
        "="*len(to_lang),
    ))


def print_translation(input_word, output_word):
    print(u"{}{}{}".format(input_word,
                          "."*(LINE_LENGTH-len(input_word)),
                          output_word))



def run():
    args = parse_args()
    # args.word = "hallo"
    # args.input_language = "de"
    # args.output_language = "pt"

    result = Dict.translate(args.word,
                            args.input_language,
                            args.output_language)
    for i, (input_word, output_word) in enumerate(result.translation_tuples):
            print(output_word)
            if i == args.max_results:
                break
    return

    if not result.n_results:
        print("No results found for {} ({} <-> {}).".format(
            args.word, args.input_language, args.output_language))
        return
    else:
        print("Showing {} of {} result(s)\n".format(
            min(args.max_results, result.n_results), result.n_results))

    print_header(result.from_lang, result.to_lang)

    for i, (input_word, output_word) in enumerate(result.translation_tuples):
        print_translation(input_word, output_word)
        if i == args.max_results:
            break


if __name__ == "__main__":
    run()
