#!/usr/bin/env python3
import pytest
from console_renderer import ConsoleRenderer
from colours import Colours
from attempt import Attempt
from exceptions import DictionaryError, StateError


def test_simple_print_one_attempt_all_right(capsys):
    expected = f"{Colours.GREEN}T{Colours.ENDC} {Colours.GREEN}R{Colours.ENDC} {Colours.GREEN}A{Colours.ENDC} {Colours.GREEN}I{Colours.ENDC} {Colours.GREEN}N{Colours.ENDC}\n"
    attempt_list = [Attempt("train", "train")]
    attempt_test(capsys, attempt_list, expected)


def test_simple_print_one_attempt_all_wrong(capsys):
    expected = f"{Colours.RED}E{Colours.ENDC} {Colours.RED}P{Colours.ENDC} {Colours.RED}O{Colours.ENDC} {Colours.RED}X{Colours.ENDC} {Colours.RED}Y{Colours.ENDC}\n"
    attempt_list = [Attempt("train", "epoxy")]
    attempt_test(capsys, attempt_list, expected)


def test_simple_print_one_attempt_all_wrong_place(capsys):
    expected = f"{Colours.YELLOW}L{Colours.ENDC} {Colours.YELLOW}B{Colours.ENDC} {Colours.YELLOW}E{Colours.ENDC} {Colours.YELLOW}A{Colours.ENDC} {Colours.YELLOW}M{Colours.ENDC}\n"
    attempt_list = [Attempt("blame", "lbeam")]
    attempt_test(capsys, attempt_list, expected)


def test_simple_print_mix_1(capsys):
    expected = f"{Colours.GREEN}B{Colours.ENDC} {Colours.GREEN}L{Colours.ENDC} {Colours.RED}X{Colours.ENDC} {Colours.YELLOW}E{Colours.ENDC} {Colours.YELLOW}M{Colours.ENDC}\n"
    attempt_list = [Attempt("blame", "blxem")]
    attempt_test(capsys, attempt_list, expected)


def test_more_complicated_simple_attempt(capsys):
    expected = f"{Colours.YELLOW}N{Colours.ENDC} {Colours.RED}O{Colours.ENDC} {Colours.YELLOW}I{Colours.ENDC} {Colours.RED}S{Colours.ENDC} {Colours.RED}E{Colours.ENDC}\n"
    attempt_list = [Attempt("train", "noise")]
    attempt_test(capsys, attempt_list, expected)


def test_realistic_scenario_part1(capsys):
    expected = f"{Colours.RED}T{Colours.ENDC} {Colours.RED}R{Colours.ENDC} {Colours.RED}U{Colours.ENDC} {Colours.RED}C{Colours.ENDC} {Colours.YELLOW}E{Colours.ENDC}\n"
    attempt_list = [Attempt("epoxy", "truce")]
    attempt_test(capsys, attempt_list, expected)


def test_realistic_scenario_part2(capsys):
    expected = f"{Colours.RED}T{Colours.ENDC} {Colours.RED}R{Colours.ENDC} {Colours.RED}U{Colours.ENDC} {Colours.RED}C{Colours.ENDC} {Colours.YELLOW}E{Colours.ENDC}\n"
    expected = (
        expected
        + f"{Colours.GREEN}E{Colours.ENDC} {Colours.YELLOW}X{Colours.ENDC} {Colours.RED}A{Colours.ENDC} {Colours.RED}M{Colours.ENDC} {Colours.RED}S{Colours.ENDC}\n"
    )
    attempt_list = [Attempt("epoxy", "truce"), Attempt("epoxy", "exams")]
    attempt_test(capsys, attempt_list, expected)


def test_realistic_scenario_part3(capsys):
    expected = f"{Colours.RED}T{Colours.ENDC} {Colours.RED}R{Colours.ENDC} {Colours.RED}U{Colours.ENDC} {Colours.RED}C{Colours.ENDC} {Colours.YELLOW}E{Colours.ENDC}\n"
    expected = (
        expected
        + f"{Colours.GREEN}E{Colours.ENDC} {Colours.YELLOW}X{Colours.ENDC} {Colours.RED}A{Colours.ENDC} {Colours.RED}M{Colours.ENDC} {Colours.RED}S{Colours.ENDC}\n"
    )
    expected = (
        expected
        + f"{Colours.GREEN}E{Colours.ENDC} {Colours.GREEN}P{Colours.ENDC} {Colours.GREEN}O{Colours.ENDC} {Colours.GREEN}X{Colours.ENDC} {Colours.GREEN}Y{Colours.ENDC}\n"
    )
    attempt_list = [
        Attempt("epoxy", "truce"),
        Attempt("epoxy", "exams"),
        Attempt("epoxy", "epoxy"),
    ]
    attempt_test(capsys, attempt_list, expected)


def attempt_test(capsys, attempt_list, expected):
    renderer = ConsoleRenderer()
    renderer.draw_attempts_so_far(attempt_list)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_warn_user_dictionary(capsys):
    message = "Word abcde is not in the dictionary"
    renderer = ConsoleRenderer()
    renderer.warn_user(DictionaryError(message))
    captured = capsys.readouterr()
    assert (
        f"{Colours.RED}{Colours.BOLD}Word abcde is not in the dictionary{Colours.ENDC}\n"
        == captured.out
    )


def state_error(capsys, message, expected):
    renderer = ConsoleRenderer()
    renderer.warn_user(StateError(message))
    captured = capsys.readouterr()
    assert expected == captured.out


def test_warn_user_too_many_attempts(capsys):
    message = "Player has lost and making more attempts"
    expected = f"{Colours.RED}{Colours.BOLD}Player has lost and making more attempts{Colours.ENDC}\n"
    state_error(capsys, message, expected)


def test_warn_user_guess_duplicate(capsys):
    message = "Guess noise already attempted"
    expected = (
        f"{Colours.RED}{Colours.BOLD}Guess noise already attempted{Colours.ENDC}\n"
    )
    state_error(capsys, message, expected)
