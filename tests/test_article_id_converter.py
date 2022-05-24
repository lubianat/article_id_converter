#!/usr/bin/env python

"""Tests for `article_id_converter` package."""

from article_id_converter.article_id_converter import convert_ids


def test_converter():
    dois = "10.1093/NAR/GKAB991 10.7554/ELIFE.52614 10.1177/1534508417745627".split()
    pmcids = ["8689886", "7077981", ""]

    result_pmcids = convert_ids(dois, input_id="DOI", output_id="PMCID")
    assert result_pmcids == pmcids


def test_converter_2():
    dois = "10.1093/NAR/GKAB991 10.7554/ELIFE.52614 10.1177/1534508417745627".split()
    qids = ["Q109348309", "Q87830400", "Q99704255"]

    result_qids = convert_ids(dois, input_id="DOI", output_id="QID")
    assert result_qids == qids


def test_converter_3():
    pmcids = ["8689886", "7077981"]
    qids = ["Q109348309", "Q87830400"]

    result_qids = convert_ids(pmcids, input_id="PMCID", output_id="QID")
    assert result_qids == qids


def test_converter_4():
    pmids = ["34718729", "32180547"]
    qids = ["Q109348309", "Q87830400"]

    result_qids = convert_ids(pmids, input_id="PMID", output_id="QID")
    assert result_qids == qids
