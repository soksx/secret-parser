import os, re, argparse


def parser(filename, secrets_dictionary):
    """
    Parse the UTF-8 file and replace secret references with values from secrets dictionary.
    """
    print("Attempting to parse file: " + filename)
    with open('/github/workspace/' + filename, 'r') as fd: 
        contents = fd.read()

    for key in secrets_dictionary:
        contents = re.sub(rf'\${{{{.*secrets\.{key}.*}}}}', secrets_dictionary[key], contents)

    with open('/github/workspace/' + filename, 'w') as fd:
        fd.write(contents)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser("Parse GitHub Actions secrets")
    argparser.add_argument('filename', help='file to parse')
    argparser.add_argument('secrets_dictionary', help='dicitonary with names and values to replace')
    args = argparser.parse_args()
    parse_dict = {str_prs.split(':')[0]: ':'.join(str(x) for x in str_prs.split(':')[1:]) for str_prs in args.secrets_dictionary.splitlines()} # First ':' split is array key, others are joined to generate value
    parser(args.filename, parse_dict)