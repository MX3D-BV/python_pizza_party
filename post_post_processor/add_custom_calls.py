def read_file(file_path):
    "read input file"
    with open(file_path, 'r') as file:
        return file.readlines()
    

def write_file(file_path, lines):
    "write output file"
    with open(file_path, 'w') as file:
        file.writelines(lines)


def add_custom_call(lines, procedure_name='Scan', interval=1):
    """
    This function adds the a call to a custom Rapid Procedure after every 'interval' welds
    """
    return lines


if __name__ == "__main__":
    # Read the file
    lines = read_file("toolpath.mod")
    
    lines = add_custom_call(lines)
    
    # Write the file
    write_file("improved_toolpath.mod", lines)
    