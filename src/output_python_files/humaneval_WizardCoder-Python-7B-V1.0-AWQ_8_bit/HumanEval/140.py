def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    return re.sub(r'\s+', lambda x: '-' if len(x.group(0)) > 1 else '_', text)


def fix_spaces_in_dict(d):
    """
    Given a dictionary d, recursively replace all spaces in keys and values with underscores
    """
    if isinstance(d, dict):
        return {fix_spaces(k): fix_spaces_in_dict(v) for k, v in d.items()}
    elif isinstance(d, (list, tuple)):
        return [fix_spaces_in_dict(x) for x in d]
    else:
        return d

def fix_spaces_in_list(lst):
    """
    Given a list, recursively replace all spaces in each element with underscores
    """
    return [fix_spaces_in_dict(x) for x in lst]

def fix_spaces_in_json(json_str):
    """
    Given a JSON string, replace all spaces in it with underscores
    """
    return json.dumps(json.loads(json_str), sort_keys=True, indent=2, default=lambda x: fix_spaces_in_dict(x))

def fix_spaces_in_file(file_path):
    """
    Given a file path, replace all spaces in it with underscores
    """
    with open(file_path, 'r') as f:
        content = f.read()
    fixed_content = fix_spaces_in_json(content)
    with open(file_path, 'w') as f:
        f.write(fixed_content)

def main():
    parser = argparse.ArgumentParser(description='Fix spaces in JSON files')
    parser.add_argument('files', nargs='+', help='Files to fix')
    args = parser.parse_args()

    for file_path in args.files:
        fix_spaces_in_file(file_path)

if __name__ == '__main__':
    main()