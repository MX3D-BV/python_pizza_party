def read_file(file_path):
    "read input file"
    with open(file_path, 'r') as file:
        return file.readlines()
    

def write_file(file_path, lines):
    "write output file"
    with open(file_path, 'w') as file:
        file.writelines(lines)


def add_custom_call(lines, procedure='Scan', interval=5):
    """
    This function adds a call to custom Rapid Procedure after every 'interval' welds
    """
    # TODO: Implement this function!
    output = []
    for i, line in enumerate(lines):
        output.append(line)
    return output


if __name__ == "__main__":
    # Read the file
    lines = read_file("toolpath.mod")
    
    lines = add_custom_call(lines)
    
    # Write the file
    write_file("improved_toolpath.mod", lines)
    