def ft_tqdm(lst: range) -> None:
    """A function that outputs the loading bar for a given number.
- The parameter requires range.
"""
    for elem in lst:
        number = elem + 1
        progress_percent = int((number) / len(lst) * 100)
        bar_full_length = 64
        progress_bar_length = int(bar_full_length * (number) / len(lst))
        bar_padding_length = bar_full_length - progress_bar_length
        print(f"\r{progress_percent}%|\
[{'=' * progress_bar_length}>{' ' * bar_padding_length}]|\
 {number}/{len(lst)}", end="")
        yield elem


def main():
    """This is the main statement that is not being used."""
    ft_tqdm(None)


if __name__ == '__main__':
    main()
