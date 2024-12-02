#!/bin/bash

# Redirect all output (stdout and stderr) of the script to log_all.txt
{
    # Check if the input file exists
    INPUT_DIR="./test_string_folder"

    # Iterate over all .g4 files in the g4_folder
    for G4_FILE in ./g4_folder/*.g4; do
        GRAMMAR_NAME=$(basename "$G4_FILE" .g4)
        OUTPUT_DIR="./inter_folder/${GRAMMAR_NAME}"

        echo "Processing grammar: $GRAMMAR_NAME"

        # Create output directory
        mkdir -p "$OUTPUT_DIR"

        # Use ANTLR to generate the parser
        java -jar antlr/antlr-4.13.2-complete.jar -Dlanguage=Python3 "$G4_FILE" -o "$OUTPUT_DIR" 2>&1 | tee -a log_all.txt
        if [ $? -ne 0 ]; then
            echo "Error: Failed to generate parser from $G4_FILE"
            continue
        fi

        # Check if the parser files were generated successfully
        LEXER_FILE="${OUTPUT_DIR}/g4_folder/${GRAMMAR_NAME}Lexer.py"
        PARSER_FILE="${OUTPUT_DIR}/g4_folder/${GRAMMAR_NAME}Parser.py"
        index=$(echo "$GRAMMAR_NAME" | sed 's/[^0-9]*//g')

        if [ ! -f "$LEXER_FILE" ] || [ ! -f "$PARSER_FILE" ]; then
            echo "Error: Parser files not generated successfully for $GRAMMAR_NAME!"
            continue
        fi

        # Call the Python script to match each line in the input file
        INPUT_CODE="${INPUT_DIR}/string${index}.txt"

        if [ ! -f "$INPUT_CODE" ]; then
            echo "Error: Input code file $INPUT_CODE not found!" | tee -a log_all.txt
            exit 1
        fi

        PYTHONPATH="$OUTPUT_DIR" python match_code_all.py "$GRAMMAR_NAME" "$INPUT_CODE"
    done

    echo "Evaluation completed. Results saved to log_all.txt"
} 2>&1 | tee log_all.txt
