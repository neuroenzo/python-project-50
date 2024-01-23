import argparse


def main():
    diff = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    diff.add_argument('first_file')
    diff.add_argument('second_file')

    diff.parse_args()


if __name__ == '__main__':
    main()
