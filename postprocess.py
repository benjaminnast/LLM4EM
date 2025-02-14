def clean_code_text(prompt_result):
    lines = prompt_result.split('\n')

    # Find the start and end positions
    start_idx = None
    end_idx = None

    for i, line in enumerate(lines):
        if line.strip().startswith('///////////') and start_idx is None:
            start_idx = i
        if line.strip().startswith('//END'):
            end_idx = i

    # Determine what to cut
    if start_idx is None:
        print("No starting line with '///////////' found.")
        start_idx = 0
    if end_idx is None:
        print("No ending line with '//END' found.")
        end_idx = len(lines) - 1

    # Trim the content
    trimmed_lines = lines[start_idx:end_idx + 1]

    # Return the cleaned text
    return '\n'.join(trimmed_lines)

